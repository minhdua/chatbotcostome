import os
import pdb

from app_factory import app
from flask import request
from flask_restful import Resource, reqparse
from models.common.response import CommonResponse
from models.enum import ColorEnum, SizeEnum
from models.order_product_model import OrderProduct
from models.product_attribute_model import ProductAttributes
from models.product_category_model import ProductCategories
from models.product_model import (
    Product,
    ProductColorEnum,
    ProductFilter,
    ProductFilterByAttributePrediction,
    ProductFilterByCategory,
    ProductFilterByCategoryPrediction,
    ProductFilterByColor,
    ProductFilterByPrice,
    ProductFilterBySize,
    ProductFilterByTag,
    ProductSizeEnum,
)
from models.product_tag_model import ProductTag
from models.tag_model import Tag
from resources.cnn.search_image import extract_features
from resources.validators import (
    validate_category,
    validate_color,
    validate_product_name,
    validate_size,
)
from utils import DEFAULT_PRODUCT_IMAGE_URL, allowed_file, if_not_none
from werkzeug.utils import secure_filename


class ProductResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=validate_product_name, nullable=True)
    parser.add_argument("price", type=int)
    parser.add_argument("quantity", type=int)
    parser.add_argument("category_id", type=validate_category)
    parser.add_argument("sizes", type=list,location='json')
    parser.add_argument("colors", type=list,location='json')
    parser.add_argument("tags", type=list,location='json')
    parser.add_argument("description", type=str)

    def get(self, product_id):
        """
        Get product by id
        ---
        tags:
            - Product
        parameters:
            -   in: path
                name: product_id
                type: integer
                required: true
                description: The product id
        responses:
            200:
                description: The product data
                content:
                    application/json:
                        schema: ProductSchema
            404:
                description: Product not found
                content:
                    application/json:
                        schema: CommonResponse
        """
        product = Product.find_by_id(product_id)
        if product:
            return CommonResponse.ok("Product found.", product.json(include_relations=True))
        return CommonResponse.not_found(f"Product with id {product_id} not found.")
    # post image for product
    def post(self, product_id):
        """
        Upload image for product
        ---
        tags:
            - Product
        parameters:
            -   in: path
                name: product_id
                type: integer
                required: true
                description: The product id
            -   in: formData
                name: image
                type: file
                required: true
                description: The image file
                accept: image/png, image/jpeg, image/jpg
        responses:
            200:
                description: The product data
                content:
                    application/json:
                        schema: ProductSchema
            404:
                description: Product not found
                content:
                    application/json:
                        schema: CommonResponse
        """
        product = Product.find_by_id(product_id)
        if product:
            image = request.files['image']
            file_path = DEFAULT_PRODUCT_IMAGE_URL
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                file_path_save = os.path.join(app.config['UPLOAD_FOLDER'], 'products/', filename)
                image.save(file_path_save)
                attributes, categories = extract_features(file_path_save)
                if len(attributes) > 0:
                    ProductAttributes.delete_by_product_id(product_id)
                    for attribute in attributes:
                        product_attribute = ProductAttributes(product_id=product.id, attribute_predict_id=attribute.id)
                        product_attribute.save_to_db()
                if len(categories) > 0:
                    ProductCategories.delete_by_product_id(product_id)
                    for category in categories:
                        image_category = ProductCategories(product_id=product.id, category_predict_id=category.id)
                        image_category.save_to_db()
                file_path = os.path.join('products/', filename)
            if os.path.exists(product.image_url):
                try:
                    os.remove(product.image_url)
                except:
                    pass
            product.image_url = os.path.join(app.config['IMAGE_DEFAULT_URL'], file_path)
            product.save_to_db()
            data_response = product.json()
            data_response['categories_predict'] = [category.name for category in categories]
            data_response['attributes_predict'] = [attribute.name for attribute in attributes]
            return CommonResponse.ok("Product image uploaded.", product.json())
        return CommonResponse.not_found(f"Product with id {product_id} not found.")
    
    def put(self, product_id):
        """
        Update a product
        ---
        tags:
            - Product
        parameters:
            - in: path
              name: product_id
              type: integer
              required: true
              description: The product id
            - in: body
              name: body
              schema: 
                    $ref: '#/definitions/Product'
              required: true
              description: The product to update
        responses:
            200:
                description: The product data
                content:
                    application/json:
                        schema: ProductSchema
            400:
                description: An error occurred while updating the product.
                content:
                    application/json:
                        schema: CommonResponse
            404:
                description: Product not found
                content:
                    application/json:
                        schema: CommonResponse
        definitions:
            Product:
                type: object
                properties:
                    name:
                        type: string
                    price:
                        type: integer
                    quantity:
                        type: integer
                    category_id:
                        type: integer
                    sizes:
                        type: array
                        items:
                            type: enum
                            enum: [S, M, L, XL, XXL]
                    colors:
                        type: array
                        items:
                            type: enum
                            enum: [Red, Blue, Green, Yellow, Black, White]
                    image_url:
                        type: string
                    tags:
                        type: array
                        items:
                            type: string
        """
        data = ProductResource.parser.parse_args()
        product = Product.find_by_id(product_id)
        if product:
            product.name = if_not_none(data["name"], product.name)
            product.price = if_not_none(data["price"], product.price)
            product.quantity = if_not_none(data["quantity"], product.quantity)
            product.category_id = data["category_id"]
            product.description = if_not_none(data["description"], product.description)
            try:
                product.update_to_db()
                # validate sizes, colors, tags
                if data["sizes"]:
                    ProductSizeEnum.delete_by_product_id(product_id)
                    for size in data["sizes"]:
                        product_size_enum = validate_size(size)
                        product_size = ProductSizeEnum(product_id=product.id, size=product_size_enum)
                        product_size.save_to_db()

                if data["colors"]:
                    ProductColorEnum.delete_by_product_id(product_id)
                    for color in data["colors"]:
                        product_color_enum = validate_color(color)
                        product_color = ProductColorEnum(product_id=product.id, color=product_color_enum)
                        product_color.save_to_db()

                if data["tags"]:
                    ProductTag.delete_by_product_id(product_id)
                    for tag in data["tags"]:
                        if not isinstance(tag, str):
                            return CommonResponse.bad_request("Invalid tag.")
                        
                        new_tag = Tag.find_by_name(tag)
                        if not new_tag:
                            new_tag = Tag(tag)
                            new_tag.save_to_db()
                        product_tag = ProductTag(product_id=product.id, tag_id=new_tag.id)
                        product_tag.save_to_db()

            except Exception as e:
                return CommonResponse.bad_request("An error occurred while updating the product {}.".format(e))
            return CommonResponse.ok("Product updated.", product.json())
        return CommonResponse.not_found(f"Product with id {product_id} not found.")
    
    def delete(self, product_id):
        """
        Delete a product
        ---
        tags:
            - Product
        parameters:
            - in: path
              name: product_id
              type: integer
              required: true
              description: The product id
        responses:
            200:
                description: The product data
                content:
                    application/json:
                        schema: ProductSchema
            404:
                description: Product not found
                content:
                    application/json:
                        schema: CommonResponse
        """
        product = Product.find_by_id(product_id)
        if product:
            

            # delete sizes, colors, tags
            ProductSizeEnum.delete_by_product_id(product_id)
            ProductColorEnum.delete_by_product_id(product_id)
            ProductTag.delete_by_product_id(product_id)
            OrderProduct.delete_by_product_id(product_id)
            # delete image
            if product.image_url != DEFAULT_PRODUCT_IMAGE_URL:
                upload_folder = app.config['UPLOAD_FOLDER']
                image_url_display = app.config['IMAGE_DEFAULT_URL']
                image_url = product.image_url.replace(image_url_display, upload_folder)
                app.config['IMAGE_DEFAULT_URL']
                if os.path.exists(image_url):
                    try:
                        os.remove(image_url)
                    except:
                        pass

           

            # delete product
            product.delete_from_db()

            return CommonResponse.ok("Product deleted.", product.json())
        return CommonResponse.not_found(f"Product with id {product_id} not found.")
    
class ProductListCreateResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=validate_product_name, required=True, help="This field cannot be blank.")
    parser.add_argument("price", type=int, required=True, help="This field cannot be blank.")
    parser.add_argument("quantity", type=int, required=True, help="This field cannot be blank.")
    parser.add_argument("category_id", type=validate_category, required=True, help="This field cannot be blank.")
    parser.add_argument("sizes", type=list,location='json', default=[])
    parser.add_argument("colors", type=list,location='json', default=[])
    parser.add_argument("tags", type=list,location='json', default=[])
    parser.add_argument("description", type=str, required=False)
    def get(self):
        """
        Get all products
        ---
        tags:
            - Product
        parameters:
            - in: query
              name: page
              schema:
                  type: integer
              description: Page number for pagination
            - in: query
              name: per_page                                                                                                                            `````````````````````` 
              schema:
                  type: integer
              description: Number of items per page
            - in: query
              name: sort_fild
              schema:
                  type: string
              description: Field to sort by
            - in: query
              name: sort_order
              schema:
                  type: string
                  enum: [asc, desc]
              description: Sort order (asc or desc)
            - in: query
              name: category
              schema:
                  type: string
              description: List of categories for filtering (e.g. 1,2,3)
            - in: query
              name: price_min
              schema:
                  type: integer
              description: Minimum price filter
            - in: query
              name: price_max
              schema:
                  type: integer    
              description: Maximum price filter
            - in: query
              name: color
              schema:
                  type: string 
                  enum: [Red, Blue, Green, Yellow, Black, White]
              description: Color filter( Red, Blue, Green, Yellow, Black, White)
            - in: query
              name: size
              schema:
                  type: string
                  enum: [S, M, L, XL, XXL]
              description: Size filter( S, M, L, XL, XXL)
            - in: query
              name: tags
              schema:
                  type: string
              description: Tags filter
        responses:
            200:
                description: The product data
                content:
                    application/json:
                        schema: ProductSchema
        """
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', -1))
        sort_field = request.args.get('sort_field', 'id')
        sort_order = request.args.get('sort_order')
        category_filter = request.args.get('category', '')
        price_min_filter = int(request.args.get('price_min', 0))
        price_max_filter = int(request.args.get('price_max', 1000000))
        color_filter = request.args.get('color')
        size_filter = request.args.get('size')
        if size_filter:
            try:
                size_filter = SizeEnum[size_filter.upper()]
            except:
                return CommonResponse.bad_request("Invalid size filter.")
        if color_filter:
            try:
                color_filter = ColorEnum[color_filter.upper()]
            except:
                return CommonResponse.bad_request("Invalid color filter.")
        tags_filter = request.args.get('tags')
        attributes_predict_filter = request.args.get('attributes_predict','')
        categories_predict_filter = request.args.get('categories_predict','')
        products = Product.get_all()

        # Apply category filter
        categories_filter = [int(id.strip()) for id in category_filter.split(',') if id.strip()]
        attributes_predict_filter = [int(id.strip()) for id in attributes_predict_filter.split(',') if id.strip()]
        categories_predict_filter = [int(id.strip()) for id in categories_predict_filter.split(',') if id.strip()]
        category_strategy = ProductFilterByCategory(categories_filter)
        price_strategy = ProductFilterByPrice(price_min_filter, price_max_filter)
        color_strategy = ProductFilterByColor(color_filter)
        size_strategy = ProductFilterBySize(size_filter)
        tags_strategy = ProductFilterByTag(tags_filter)
        attributes_predict_strategy = ProductFilterByAttributePrediction(attributes_predict_filter)
        categories_predict_strategy = ProductFilterByCategoryPrediction(categories_predict_filter)
        
        product_filter = ProductFilter(products, category_strategy).and_(price_strategy).and_(color_strategy).and_(size_strategy).and_(tags_strategy).and_(attributes_predict_strategy).and_(categories_predict_strategy)
        products = product_filter.filter()

        # Apply sorting
        if sort_order:
            if sort_order == 'asc' :
                products.sort(key=lambda product: getattr(product, sort_field))
            else:
                products.sort(key=lambda product: getattr(product, sort_field), reverse=True)

        # Calculate pagination indices
        if per_page == -1:
            per_page = len(products)
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        paginated_products = products[start_index:end_index]
        product_list = [product.json() for product in paginated_products]

        return CommonResponse.ok("Products retrieved successfully.", product_list, len(products), page, per_page)

    def post(self):
        """
        Create a product
        ---
        tags:
            - Product
        parameters:
            - in: body
              name: body
              schema: 
                    $ref: '#/definitions/Product'
              required: true
              description: The product to create
        responses:
            201:
                description: The product data
                content:
                    application/json:
                        schema: ProductSchema
            400:
                description: An error occurred while creating the product.
                content:
                    application/json:
                        schema: CommonResponse
        definitions:
            Product:
                type: object
                properties:
                    name:
                        type: string
                    price:
                        type: integer
                    quantity:
                        type: integer
                    category_id:
                        type: integer
                    sizes:
                        type: array
                        items:
                            type: string
                            enum: [S, M, L, XL, XXL]
                    colors:
                        type: array
                        items:
                            type: string
                            enum: [Red, Blue, Green, Yellow, Black, White]
                    tags:
                        type: array
                        items:
                            type: string
                    description:
                        type: string
        """
        data = self.parser.parse_args()
        product = Product(
            data["name"],
            data["price"],
            data["quantity"],
            data["category_id"],
            description=data["description"]
        )
       

        try:
            product.save_to_db()
            # validate sizes, colors, tags
            for size in data["sizes"]:
                product_size_enum = validate_size(size)
                product_size = ProductSizeEnum(product_id=product.id, size=product_size_enum)
                product_size.save_to_db()

            for color in data["colors"]:
                product_color_enum = validate_color(color)
                product_color = ProductColorEnum(product_id=product.id, color=product_color_enum)
                product_color.save_to_db()

            for tag in data["tags"]:
                if not isinstance(tag, str):
                    return CommonResponse.bad_request("Invalid tag.")
                
                new_tag = Tag.find_by_name(tag)
                if not new_tag:
                    new_tag = Tag(tag)
                    new_tag.save_to_db()
                product_tag = ProductTag(product_id=product.id, tag_id=new_tag.id)
                product_tag.save_to_db()
        except Exception as e:
            return CommonResponse.bad_request("An error occurred while creating the product. {}".format(e))
        return CommonResponse.created("Product created.", product.json())
    
class ProductCNNResource(Resource):
    def post(self):
        """
        Update all attributes and categories prediction for product
        ---
        tags:
            - CNN
        responses:
            200:
                description: The product data
                content:
                    application/json:
                        schema: ProductSchema

        """
        products = Product.get_all()
        for product in products:
            try:
                default_image_url = os.path.join(app.config['UPLOAD_FOLDER'], DEFAULT_PRODUCT_IMAGE_URL)
                file_path = product.image_url.replace(app.config['IMAGE_DEFAULT_URL'], app.config['UPLOAD_FOLDER'])
                if not os.path.exists(file_path) or file_path == default_image_url:
                    continue
                attributes, categories = extract_features(file_path)
                if len(attributes) > 0:
                    ProductAttributes.delete_by_product_id(product.id)
                    for attribute in attributes:
                        product_attribute = ProductAttributes(product_id=product.id, attribute_predict_id=attribute.id)
                        product_attribute.save_to_db()
                if len(categories) > 0:
                    ProductCategories.delete_by_product_id(product.id)
                    for category in categories:
                        image_category = ProductCategories(product_id=product.id, category_predict_id=category.id)
                        image_category.save_to_db()
            except Exception as e:
                print(e)
                pass
        return CommonResponse.ok("Product updated.", {})