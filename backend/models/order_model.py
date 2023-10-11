import pdb
from copy import deepcopy

from db import db
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from models.base_mixin import BaseMixin
from models.enum import OrderStatusEnum
from models.order_product_model import OrderProduct
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property
from utils import if_not_none


class OrderAdminView(ModelView):
    column_list = ['id', 'email', 'phone', 'address', 'fullname', 'status']

    @property
    def total_price(self):
        return self.model.total_price  # Đảm bảo total_price là một trường trong model Order

    form_columns = ['order_date', 'email', 'phone', 'address', 'fullname', 'total_price']

    # Sử dụng form_edit_rules để chỉ hiển thị trường total_price dưới dạng chỉ đọc
    form_edit_rules = [
        'email', 'phone', 'address', 'fullname'
    ]

    # Sử dụng form_create_rules để chỉ hiển thị trường total_price dưới dạng chỉ đọc
    form_create_rules = [
        'email', 'phone', 'address', 'fullname'
    ]
class Order(db.Model, BaseMixin):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    email = db.Column(db.String(255), nullable=False, name="customer_email")
    phone = db.Column(db.String(255), nullable=False, name="customer_phone")
    address = db.Column(db.String(255), nullable=False, name="customer_address")
    fullname = db.Column(db.String(255), nullable=False)  # Thêm cột fullname
    total_price = db.Column(db.Float, nullable=True, name="total_price")
    # status = db.Column(db.String(255), nullable=False, default="PENDING", name="status")
    status = db.Column(db.Enum(OrderStatusEnum), nullable=False, default=OrderStatusEnum.PENDING, name="status")
    products = db.relationship("Product", secondary=OrderProduct.__tablename__, lazy=True)
    
    @hybrid_property
    def readonly_order_date(self):
        return self.order_date
   
   
    def __init__(
        self,
        order_date,
        email,
        phone,
        address,
        fullname,
        total_price,
        status,
        products=[],
    ):
        self.order_date = order_date
        self.email = email
        self.phone = phone
        self.address = address
        self.fullname = fullname
        self.total_price = total_price
        self.status = status
        self.products = products

    def __repr__(self):
        return f"Order({self.id}, {self.order_date}, {self.email}, {self.phone}, {self.address}, {self.fullname}, {self.total_price}, {self.status}, {self.products})"

    def json(self):
        product_infos = []
        order_products = OrderProduct.query.filter_by(order_id=self.id).all()

        for order_product in order_products:
            product = order_product.product
            product_info = product.json()

            # Lấy thông tin từ order_product
            product_info["quantity"] = order_product.quantity
            product_info["order_size"] = order_product.order_size.value
            product_info["order_color"] = order_product.order_color.value
        
            product_infos.append(product_info)
        return {
            "id": self.id,
            "order_date": self.order_date,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "fullname": self.fullname,
            "total_price": self.total_price,
            "status": self.status.value,
            "products": product_infos,
        }
    
    
    def save_to_db(self):
        new_order = Order(
            order_date=self.order_date,
            email=self.email,
            phone=self.phone,
            address=self.address,
            fullname=self.fullname,
            total_price=self.total_price,
            status=self.status
        )

        db.session.add(new_order)
        db.session.commit()
        for product in self.products:
            order_product = OrderProduct(
                order_id=new_order.id,
                product_id=product["product_id"],
                quantity=product["quantity"],
                order_size=product["order_size"],
                order_color=product["order_color"]
            )
            order_product.save_to_db()

        return new_order
    
    def update_to_db(self,**kwargs):
        email = if_not_none(kwargs.get("email"), self.email)
        phone = if_not_none(kwargs.get("phone"), self.phone)
        address = if_not_none(kwargs.get("address"), self.address)
        fullname = if_not_none(kwargs.get("fullname"), self.fullname)
        total_price = if_not_none(kwargs.get("total_price"), self.total_price)
        status = if_not_none(kwargs.get("status"), self.status)
        new_products = kwargs.get("products")
        old_products = OrderProduct.query.filter_by(order_id=self.id).all()
       

        self.email = email
        self.phone = phone
        self.address = address
        self.fullname = fullname
        self.total_price = total_price
        self.status = status
    
        db.session.commit()
        # self.products = old_products
        if new_products is not None:
            for old_product in old_products:
                OrderProduct.delete_from_db(old_product)

            for product in new_products:
                order_product = OrderProduct(
                    order_id=self.id,
                    product_id=product["product_id"],
                    quantity=product["quantity"],
                    order_size=product["order_size"],
                    order_color=product["order_color"]
                )
                order_product.save_to_db()
            # self.products = new_products
     
        return self
    
    def update(self, order_id, status_value):
        update = db.session.query(Order).get(order_id)
        
        if status_value == OrderStatusEnum.PENDING.value:
            status_value = OrderStatusEnum.PENDING
            
        elif status_value == OrderStatusEnum.CONFIRMED.value:
            status_value = OrderStatusEnum.CONFIRMED
            
        elif status_value == OrderStatusEnum.SHIPPING.value:
            status_value = OrderStatusEnum.SHIPPING
            
        elif status_value == OrderStatusEnum.DELIVERED.value:
            status_value = OrderStatusEnum.DELIVERED
            
        else:
            status_value = OrderStatusEnum.CANCELLED
            
        setattr(update, 'status', status_value)
        db.session.commit()
        db.session.flush()

    def delete_from_db(self, order_id):
        OrderProduct.delete_by_order_id(order_id)
        super().delete_from_db()


class OrderFilterStrategy:

    def filter(self, orders):
        raise NotImplementedError("Subclasses must implement this method")

class OrderFilterByStatus(OrderFilterStrategy):
    def __init__(self, status):
        if status:
            self.status = status.capitalize()
        else:
            self.status = "All"

    def filter(self, orders):
        if self.status == "All":
            return orders
        return list(filter(lambda order: order.status.value == self.status, orders))


class OrderFilter(OrderFilterStrategy):
    def __init__(self, orders, strategy):
        self.orders = orders
        self.strategy = strategy
        self.filters = [self.strategy.filter]

    def filter(self):
        result = self.orders
        for filter_func in self.filters:
            result = filter_func(result)
        return result

    def and_(self, strategy):
        self.filters.append(strategy.filter)
        return self

    def or_(self, strategy):
        combined_filter = lambda orders: list(set(self.strategy.filter(orders) + strategy.filter(orders)))
        self.filters.append(combined_filter)
        return self


    
