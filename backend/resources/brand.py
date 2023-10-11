
from flask_restful import Resource, reqparse
from models.brand import Brand
from models.common.response import CommonResponse


class BrandResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("brand_name", type=str, required=True, help="This field cannot be blank.")

	def get(self, brand_name):
		"""
		Find a brand by its name.
		---
		tags:
			- Brand
		parameters:
		  - name: brand_name
		    in: path
		    type: string
		    required: true
		    description: The brand name
		responses:
		  200:
		    description: Brand found
		    schema:
		      id: Brand
		      properties:
		        status:
		          type: string
		          description: The status of the brand
		          default: success
		        message:
		          type: string
		          description: The message of the brand
		          default: Brand found.
		        data:
		          type: object
		          description: The brand data
		          default: {}
		  404:
		    description: Brand not found
		    schema:
		      id: Brand
		      properties:
		        status:
		          type: string
		          description: The status of the brand
		          default: error
		        message:
		          type: string
		          description: The message of the brand
		          default: Brand not found.
		"""
		brand = Brand.find_by_brand_name(brand_name)
		if brand:
			return CommonResponse(status="success", message="Brand found.", data=brand.json()).json(), 200
		return CommonResponse(status="error", message="Brand not found.").json(), 404
    
	def post(self, brand_name):
		"""
		Create a brand.
		---
		tags:
			- Brand
		parameters:
		  - name: brand_name
		    in: path
		    type: string
		    required: true
		    description: The brand name
		responses:
		  201:
		    description: Brand created
		    schema:
		      id: Brand
		      properties:
		        status:
		          type: string
		          description: The status of the brand
		          default: success
		        message:
		          type: string
		          description: The message of the brand
		          default: Brand created.
		        data:
		          type: object
		          description: The brand data
		          default: {}
		  400:
		    description: Brand already exists
		    schema:
		      id: Brand
		      properties:
		        status:
		          type: string
		          description: The status of the brand
		          default: error
		        message:
		          type: string
		          description: The message of the brand
		          default: Brand already exists.
		"""
		if Brand.find_by_brand_name(brand_name):
			return CommonResponse(status="error", message="Brand already exists.").json(), 400
		brand = Brand(brand_name)
		brand.save_to_db()
		return CommonResponse(status="success", message="Brand created.", data=brand.json()).json(), 201
    
	def delete(self, brand_name):
		"""
		Delete a brand by its name.
		---
		tags:
			- Brand
		parameters:
		  - name: brand_name
		    in: path
		    type: string
		    required: true
		    description: The brand name
		responses:
		  200:
		    description: Brand deleted
		    schema:
		      id: Brand
		      properties:
		        status:
		          type: string
		          description: The status of the brand
		          default: success
		        message:
		          type: string
		          description: The message of the brand
		          default: Brand deleted.
		        data:
		          type: object
		          description: The brand data
		          default: {}
		  404:
		    description: Brand not found
		    schema:
		      id: Brand
		      properties:
		        status:
		          type: string
		          description: The status of the brand
		          default: error
		        message:
		          type: string
		          description: The message of the brand
		          default: Brand not found.
		"""
		brand = Brand.find_by_brand_name(brand_name)
		if brand:
			brand.delete_from_db()
			return CommonResponse(status="success", message="Brand deleted.", data=brand.json()).json(), 200
		return CommonResponse(status="error", message="Brand not found.").json(), 404
    
	def put(self, brand_name):
		"""
		Update a brand by its name.
		---
		tags:
			- Brand
		parameters:
		  - name: brand_name
		    in: path
		    type: string
		    required: true
		    description: The brand name
		responses:
		  200:
		    description: Brand updated
		    schema:
		      id: Brand
		      properties:
		        status:
		          type: string
		          description: The status of the brand
		          default: success
		        message:
		          type: string
		          description: The message of the brand
		          default: Brand updated.
		        data:
		          type: object
		          description: The brand data
		          default: {}
		  404:
		    description: Brand not found
		    schema:
		      id: Brand
		      properties:
		        status:
		          type: string
		          description: The status of the brand
		          default: error
		        message:
		          type: string
		          description: The message of the brand
		          default: Brand not found.
		"""
		data = BrandResource.parser.parse_args()
		brand = Brand.find_by_brand_name(brand_name)
		if brand:
			brand.brand_name = data["brand_name"]
			brand.save_to_db()
			return CommonResponse(status="success", message="Brand updated.", data=brand.json()).json(), 200
		return CommonResponse(status="error", message="Brand not found.").json(), 404
    
class BrandListResource(Resource):
	def get(self):
		"""
		Get all brands.
		---
		tags:
			- Brand
		responses:
		  200:
		    description: Brands found
		    schema:
		      id: Brand
		      properties:
		        status:
		          type: string
		          description: The status of the brand
		          default: success
		        message:
		          type: string
		          description: The message of the brand
		          default: Brands found.
		        data:
		          type: object
		          description: The brand data
		          default: {}
		"""
		return CommonResponse(status="success", message="Brands found.", data={"brands": [brand.json() for brand in Brand.query.all()]}).json(), 200
	