import pdb
from copy import deepcopy

from app_factory import db
from models.base_mixin import BaseMixin
from models.enum import ColorEnum, SizeEnum, serialize_enum, serialize_enum_list
from models.order_model import Order
from models.order_product_model import OrderProduct
from models.product_attribute_model import ProductAttributes
from models.product_category_model import ProductCategories
from models.product_tag_model import ProductTag
from models.tag_model import Tag
from utils import DEFAULT_PRODUCT_IMAGE_URL


class ProductSizeEnum(BaseMixin, db.Model):
    __tablename__ = "product_size_enum"
    extend_existing=True

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), primary_key=True)
    size = db.Column(db.Enum(SizeEnum), primary_key=True)

    def __init__(self, product_id, size):
        self.product_id = product_id
        self.size = size

    @classmethod
    def delete_by_product_id(cls, product_id):
        cls.query.filter_by(product_id=product_id).delete()
        db.session.commit()
        

# Lớp liên kết giữa Product và ColorEnum
class ProductColorEnum(BaseMixin, db.Model):
    __tablename__ = "product_color_enum"

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), primary_key=True)
    color = db.Column(db.Enum(ColorEnum), primary_key=True)

    def __init__(self, product_id, color):
        self.product_id = product_id
        self.color = color

    @classmethod
    def delete_by_product_id(cls, product_id):
        cls.query.filter_by(product_id=product_id).delete()
        db.session.commit()



class Product(db.Model, BaseMixin):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, name="name")
    price = db.Column(db.Integer, nullable=False, name="price")
    quantity = db.Column(db.Integer, nullable=False, name="quantity")
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    image_url = db.Column(db.String(255), nullable=False, name="image_url")
    sizes = db.relationship("ProductSizeEnum", backref="product")
    colors = db.relationship("ProductColorEnum", backref="product")
    description = db.Column(db.String(255), nullable=True, name="description")
    tags = db.relationship(
        "Tag",
        secondary=ProductTag.__tablename__,
        lazy="subquery",
        backref=db.backref("associated_products", lazy=True),  # Use a unique name
       
    )
    orders = db.relationship("Order", secondary=OrderProduct.__tablename__
                             , lazy=True)
    attributes_prediciton = db.relationship("AttributePrediction", secondary=ProductAttributes.__tablename__,
    lazy="subquery", backref=db.backref("associated_products", lazy=True))
    categories_prediction = db.relationship("CategoryPrediction", secondary=ProductCategories.__tablename__,
    lazy="subquery", backref=db.backref("associated_products", lazy=True))

    def __init__(
        self,
        name,
        price,
        quantity,
        category_id,
        description="",
        image_url = DEFAULT_PRODUCT_IMAGE_URL,
        sizes = [],
        colors = [],
        tags = [],
        orders = [],
        attributes_prediciton = [],
        categories_prediction = []
    ):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category_id = category_id
        self.image_url = image_url
        self.description = description
        self.sizes = sizes
        self.colors = colors
        self.tags = tags
        self.orders = orders
        self.attributes_prediciton = attributes_prediciton
        self.categories_prediction = categories_prediction
    def __repr__(self):
        sizes_str = "[" + ", ".join(serialize_enum_list([e.size for e in self.sizes])) + "]"
        colors_str = "[" + ", ".join(serialize_enum_list([e.color for e in self.colors])) + "]"
    
        return f"Product({self.id}, {self.name}, {self.price}, {self.quantity}, {self.category_id}, {sizes_str}, {colors_str}, {self.tags}, {self.orders})"

    def json(self, include_relations=False):
        
        product_response =  {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category_id": self.category_id,
            "sizes": serialize_enum_list([e.size for e in self.sizes]),
            "colors": serialize_enum_list([e.color for e in self.colors]),
            "description": self.description,
            "image_url": self.image_url,
            "tags": [tag.json() for tag in self.tags],
            # "orders": [order.json() for order in self.orders],
            "attributes_prediciton": [attribute_prediction.name for attribute_prediction in self.attributes_prediciton],
            "categories_prediction": [category_prediction.name for category_prediction in self.categories_prediction],
        }

        if include_relations:
            product_response["products_relations"] = [product.json() for product in self.products_relations()]
        
        return product_response

    def update_to_db(self, **kwargs):
        self.name = kwargs.get("name", self.name)
        self.price = kwargs.get("price", self.price)
        self.quantity = kwargs.get("quantity", self.quantity)
        self.category_id = kwargs.get("category_id", self.category_id)
        self.description = kwargs.get("description", self.description)
        self.sizes = kwargs.get("sizes", self.sizes)
        self.colors = kwargs.get("colors", self.colors)
        self.tags = kwargs.get("tags", self.tags)
        self.attributes_prediciton = kwargs.get("attributes_prediciton", self.attributes_prediciton)
        self.categories_prediction = kwargs.get("categories_prediction", self.categories_prediction)
        db.session.commit()

        # update sizes
        if kwargs.get("sizes"):
            old_sizes = ProductSizeEnum.query.filter_by(product_id=self.id).all()
            for old_size in old_sizes:
                db.session.delete(old_size)
                db.session.commit()
            for size in self.sizes:
                product_size_enum = ProductSizeEnum(product_id=self.id, size=size)
                db.session.add(product_size_enum)
                db.session.commit()

        # update colors
        if kwargs.get("colors"):
            old_colors = ProductColorEnum.query.filter_by(product_id=self.id).all()
            for old_color in old_colors:
                db.session.delete(old_color)
                db.session.commit()
            for color in self.colors:
                product_color_enum = ProductColorEnum(product_id=self.id, color=color)
                db.session.add(product_color_enum)
                db.session.commit()

        # update tags
        if kwargs.get("tags"):
            old_tags = ProductTag.query.filter_by(product_id=self.id).all()
            for old_tag in old_tags:
                db.session.delete(old_tag)
                db.session.commit()
            for tag in self.tags:
                product_tag = ProductTag(product_id=self.id, tag_id=tag.id)
                db.session.add(product_tag)
                db.session.commit()

    def delete_from_db(self):
        ProductSizeEnum.delete_by_product_id(self.id)
        ProductColorEnum.delete_by_product_id(self.id)
        ProductTag.delete_by_product_id(self.id)
        OrderProduct.delete_by_product_id(self.id)
        ProductAttributes.delete_by_product_id(self.id)
        ProductCategories.delete_by_product_id(self.id)
        super().delete_from_db()

    def products_relations(self):
        # Query products with the same category
        related_products = Product.find_by_category(self.category_id)
        
        # Exclude the current product from the list
        related_products = [product for product in related_products if product.id != self.id]
        return related_products

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_category(cls, category_id):
        return cls.query.filter_by(category_id=category_id).all()
    

    @classmethod
    def find_by_image_url(cls, image_url):
        products = cls.query.all()
        for product in products:
            product_image_url = product.image_url.split("/")[-3:]
            product_image_url = "/".join(product_image_url)

            image_url = image_url.split("/")[-3:]
            image_url = "/".join(image_url)

            if product_image_url == image_url:
                return product
        return None
    
# Lớp cơ sở cho chiến lược filter
class ProductFilterStrategy:
    def filter(self, products):
        raise NotImplementedError("You should implement this method")


# Lớp cụ thể cho chiến lược filter
class ProductFilterByPrice(ProductFilterStrategy):
    def __init__(self, min_price=None, max_price=None):
        self.min_price = min_price
        self.max_price = max_price

    def filter(self, products):
        if self.min_price is None and self.max_price is None:
            return products

        filtered_products = products

        if self.min_price is not None:
            filtered_products = list(filter(lambda p: p.price >= self.min_price, filtered_products))

        if self.max_price is not None:
            filtered_products = list(filter(lambda p: p.price <= self.max_price, filtered_products))

        return filtered_products


class ProductFilterByCategory(ProductFilterStrategy):
    def __init__(self, category_ids):
        self.category_ids = category_ids

    def filter(self, products):
        if not self.category_ids:
            return products
        return list(filter(lambda p: p.category_id in map(int, self.category_ids), products))



class ProductFilterBySize(ProductFilterStrategy):
    def __init__(self, size):
        self.size = size

    def filter(self, products):
        if self.size is None:
            return products
        return list(filter(lambda p: serialize_enum(self.size) in [serialize_enum(e.size) for e in p.sizes], products))


class ProductFilterByColor(ProductFilterStrategy):
    def __init__(self, color):
        self.color = color

    def filter(self, products):
        if self.color is None:
            return products
        return list(filter(lambda p: serialize_enum(self.color) in [serialize_enum(e.color) for e in p.colors], products))


class ProductFilterByTag(ProductFilterStrategy):
    def __init__(self, tag):
        self.tag = tag

    def filter(self, products):
        if self.tag is None:
            return products
        return list(filter(lambda p: self.tag in p.tags, products))

class ProductFilterByAttributePrediction(ProductFilterStrategy):
    def __init__(self, attributes_prediction):
        self.attributes_prediction = attributes_prediction
        self.threshold = 0.5

    def set_threshold(self, threshold):
        self.threshold = threshold
        return self

    def filter(self, products):
        if self.attributes_prediction is None or self.attributes_prediction == []:
            return products

        product_attributes = ProductAttributes.query.with_entities(ProductAttributes.product_id).filter(ProductAttributes.attribute_predict_id.in_(self.attributes_prediction)).all()
        product_ids = [product_attribute[0] for product_attribute in product_attributes]

        # Filter products based on the threshold for attribute prediction matching percentage
        filtered_products = []
        for product in products:
            if product.id in product_ids:
                matching_percentage = product.attributes_prediction.count(self.attributes_prediction) / len(self.attributes_prediction)
                if matching_percentage >= self.threshold:
                    filtered_products.append(product)

        sorted_result = sorted(filtered_products, key=lambda p: p.attributes_prediction.count(self.attributes_prediction), reverse=True)

        return sorted_result


class ProductFilterByCategoryPrediction(ProductFilterStrategy):
    def __init__(self, categories_prediction):
        self.categories_prediction = categories_prediction

    def filter(self, products):
        if self.categories_prediction is None or self.categories_prediction == []:
            return products
        product_categories = ProductCategories.query.with_entities(ProductCategories.product_id).filter(ProductCategories.category_predict_id.in_(self.categories_prediction)).all()
        product_ids = [product_category[0] for product_category in product_categories]
        filter_result = list(filter(lambda p: p.id in product_ids , products))
        sorted_result = sorted(filter_result, key=lambda p: p.categories_prediction.count(self.categories_prediction), reverse=True)
        return sorted_result

class ProductFilterByCategoryPredictionAndAttributePrediction(ProductFilterStrategy):
    def __init__(self, categories_prediction, attributes_prediction):
        self.categories_prediction = categories_prediction
        self.attributes_prediction = attributes_prediction
        self.threshold = 0

    def set_threshold(self, threshold):
        self.threshold = threshold
        return self

    def filter(self, products):
        if self.categories_prediction is None:
            self.categories_prediction = []

        # Loop through all categories prediction, find all products that have the same category prediction. after count the number of products that have the same attribute prediction and sort the result by the number of products that have the same attribute prediction
        result = []
        for category_prediction in self.categories_prediction:
            product_categories = ProductCategories.query.with_entities(ProductCategories.product_id).filter(ProductCategories.category_predict_id == category_prediction).all()
            product_ids = [product_category[0] for product_category in product_categories]
            filter_result = list(filter(lambda p: p.id in product_ids , products))
            sorted_result = sorted(filter_result, key=lambda p: p.attributes_prediction.count(self.attributes_prediction), reverse=True)
            products = sorted_result

        # Filter products based on the threshold for attribute prediction matching percentage
        filtered_products = []
        for product in products:
            if product.id in product_ids:
                matching_percentage = product.attributes_prediction.count(self.attributes_prediction) / len(self.attributes_prediction)
                if matching_percentage >= self.threshold:
                    filtered_products.append(product)

        sorted_result = sorted(filtered_products, key=lambda p: p.attributes_prediction.count(self.attributes_prediction), reverse=True)



# Lớp thực hiện việc filter sản phẩm
class ProductFilter:
    def __init__(self, products, strategy):
        self.products = products
        self.strategy = strategy
        self.filters = [self.strategy.filter]

    def filter(self):
        result = self.products
        for filter_func in self.filters:
            result = filter_func(result)
        return result

    def and_(self, strategy):
        self.filters.append(strategy.filter)
        return self

    def or_(self, strategy):
        combined_filter = lambda products: list(set(self.strategy.filter(products) + strategy.filter(products)))
        self.filters.append(combined_filter)
        return self

# Lớp cơ sở cho chiến lược sort
class ProductSortStrategy:
    def sort(self, products):
        pass


# Lớp cụ thể cho chiến lược sort
class ProductSortByName(ProductSortStrategy):
    def sort(self, products):
        return sorted(products, key=lambda p: p.name)


class ProductSortByPrice(ProductSortStrategy):
    def sort(self, products):
        return sorted(products, key=lambda p: p.price)


class ProductSortByQuantity(ProductSortStrategy):
    def sort(self, products):
        return sorted(products, key=lambda p: p.quantity)


class ProductSortByCategory(ProductSortStrategy):
    def sort(self, products):
        return sorted(products, key=lambda p: p.category_id)

class ProductSortBySize(ProductSortStrategy):
    def sort(self, products):
        return sorted(products, key=lambda p: p.size)


class ProductSortByColor(ProductSortStrategy):
    def sort(self, products):
        return sorted(products, key=lambda p: p.color)


# Lớp thực hiện việc sort sản phẩm
class ProductSort:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, products):
        return self.strategy.sort(products)
