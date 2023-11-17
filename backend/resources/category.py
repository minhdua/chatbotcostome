from flask_restful import Resource, reqparse
from models.category_model import Category
from models.common.response import CommonResponse


class CategoryResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("category_name", type=str, required=True, help="This field cannot be blank.")

	def get(self, category_name):
		"""
		Find a category by its name.
		---
		tags:
			- Category
		parameters:
		  - name: category_name
		    in: path
		    type: string
		    required: true
		    description: The category name
		responses:
		  200:
		    description: Category found
		    schema:
		      id: Category
		      properties:
		        status:
		          type: string
		          description: The status of the category
		          default: success
		        message:
		          type: string
		          description: The message of the category
		          default: Category found.
		        data:
		          type: object
		          description: The category data
		          default: {}
		  404:
		    description: Category not found
		    schema:
		      id: Category
		      properties:
		        status:
		          type: string
		          description: The status of the category
		          default: error
		        message:
		          type: string
		          description: The message of the category
		          default: Category not found.
		"""
		category = Category.find_by_name(category_name)
		if category:
			return CommonResponse.ok(message="Category found.", data=category.json()).json(), 200
		return CommonResponse.not_found(message="Category not found.")
    
	def post(self):
		"""
		Create a new category.
		---
		tags:
			- Category
		parameters:
		  - name: category_name
		    in: body
		    type: string
		    required: true
		    description: The category name
		responses:
		  200:
		    description: Category created
		    schema:
		      id: Category
		      properties:
		        status:
		          type: string
		          description: The status of the category
		          default: success
		        message:
		          type: string
		          description: The message of the category
		          default: Category created.
		        data:
		          type: object
		          description: The category data
		          default: {}
		  400:
		    description: Category already exists
		    schema:
		      id: Category
		      properties:
		        status:
		          type: string
		          description: The status of the category
		          default: error
		        message:
		          type: string
		          description: The message of the category
		          default: Category already exists.
		"""
		data = CategoryResource.parser.parse_args()
		if Category.find_by_name(data["category_name"]):
			return CommonResponse.conflict(message="Category already exists.")
		category = Category(category_name=data["category_name"])
		category.save_to_db()
		return CommonResponse.created(message="Category created.", data=category.json())
    
	def delete(self, category_name):
		"""
		Delete a category by its name.
		---
		tags:
			- Category
		parameters:
		  - name: category_name
		    in: path
		    type: string
		    required: true
		    description: The category name
		responses:
		  200:
		    description: Category deleted
		    schema:
		      id: Category
		      properties:
		        status:
		          type: string
		          description: The status of the category
		          default: success
		        message:
		          type: string
		          description: The message of the category
		          default: Category deleted.
		        data:
		          type: object
		          description: The category data
		          default: {}
		  404:
		    description: Category not found
		    schema:
		      id: Category
		      properties:
		        status:
		          type: string
		          description: The status of the category
		          default: error
		        message:
		          type: string
		          description: The message of the category
		          default: Category not found.
		"""
		category = Category.find_by_name(category_name)
		if category:
			category.delete_from_db()
			return CommonResponse.ok(message="Category deleted.", data=category.json())
		return CommonResponse.not_found(message="Category not found.")
    
	def put(self, category_name):
		"""
		Update a category by its name.
		---
		tags:
			- Category
		parameters:
		  - name: category_name
		    in: path
		    type: string
		    required: true
		    description: The category name
		  - name: category_name
		    in: body
		    type: string
		    required: true
		    description: The category name
		responses:
		  200:
		    description: Category updated
		    schema:
		      id: Category
		      properties:
		        status:
		          type: string
		          description: The status of the category
		          default: success
		        message:
		          type: string
		          description: The message of the category
		          default: Category updated.
		        data:
		          type: object
		          description: The category data
		          default: {}
		  404:
		    description: Category not found
		    schema:
		      id: Category
		      properties:
		        status:
		          type: string
		          description: The status of the category
		          default: error
		        message:
		          type: string
		          description: The message of the category
		          default: Category not found.
		"""
		data = CategoryResource.parser.parse_args()
		category = Category.find_by_name(category_name)
		if category:
			category.category_name = data["category_name"]
			category.save_to_db()
			return CommonResponse.ok(message="Category updated.", data=category.json())
		return CommonResponse.not_found(message="Category not found.")
    
class CategoryListResource(Resource):
	def get(self):
		"""
		Get all categories.
		---
		tags:
			- Category
		responses:
		  200:
		    description: Categories found
		    schema:
		      id: Category
		      properties:
		        status:
		          type: string
		          description: The status of the category
		          default: success
		        message:
		          type: string
		          description: The message of the category
		          default: Categories found.
		        data:
		          type: object
		          description: The category data
		          default: {}
		"""
		categories = Category.get_all()
		return CommonResponse.ok(message="Categories found.", data=[category.json() for category in categories])