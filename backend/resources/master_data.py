from flask_restful import Resource
from models.common.response import CommonResponse
from models.enum import (
    ClothingParts,
    ColorEnum,
    EvaluationStatus,
    Gender,
    LandMarkStatus,
    OrderStatusEnum,
    Perspective,
    SizeEnum,
)


class SizeResourceList(Resource):
	def get(self):
		"""
		List all sizes
		---
		tags:
		  - Master Data
		responses:
		  200:
			description: List all sizes
			schema:
				type: object
				properties:
				message:
					type: string
				data:
					type: array
					items:
					type: string
				total:
					type: integer
		"""
		data = [size.value for size in SizeEnum]
		return CommonResponse.ok("Get sizes successfully", data, len(data))
	
class ColorResourceList(Resource):
	def get(self):
		"""
		List all colors
		---
		tags:
		  - Master Data
		responses:
		  200:
			description: List all colors
			schema:
				type: object
				properties:
				message:
					type: string
				data:
					type: array
					items:
					type: string
				total:
					type: integer
		"""
		data = [color.value for color in ColorEnum]
		return CommonResponse.ok("Get colors successfully", data, len(data))
	
class OrderStatusResourceList(Resource):
	def get(self):
		"""
		List all order status
		---
		tags:
		  - Master Data
		responses:
		  200:
			description: List all order status
			schema:
				type: object
				properties:
				message:
					type: string
				data:
					type: array
					items:
					type: string
				total:
					type: integer
		"""
		data = [status.value for status in OrderStatusEnum]
		return CommonResponse.ok("Get order status successfully", data, len(data))
	
class PerspectiveListResource(Resource):
	def get(self):
		"""
		List all perspectives
		---
		tags:
		  - Master Data
		responses:
		  200:
			description: List all perspectives
			schema:
				type: object
				properties:
				message:
					type: string
				data:
					type: array
					items:
					type: string
				total:
					type: integer
		"""
		data = [item.value.json() for item in Perspective]
		return CommonResponse.ok("Get perspectives successfully", data, len(data))

class GenderListResource(Resource):
	def get(self):
		"""
		List all gender
		---
		tags:
		  - Master Data
		responses:
			200:
				description: List all perspectives
			schema:
				type: object
				properties:
				message:
					type: string
				data:
					type: array
					items:
					type: string
				total:
					type: integer
		"""
		data = [item.value.json() for item in Gender]
		return CommonResponse.ok("Get perspectives successfully", data, len(data))
	
class LandMarkStatusListResource(Resource):
	def get(self):
		"""
		List all landmark status
		---
		tags:
		  - Master Data
		responses:
			200:
				description: List all landmark status
			schema:
				type: object
				properties:
				message:
					type: string
				data:
					type: array
					items:
					type: string
				total:
					type: integer
		"""
		data = [item.value.json() for item in LandMarkStatus]
		return CommonResponse.ok("Get landmark status successfully", data, len(data))
	
class ClothingPartsListResource(Resource):
	def get(self):
		"""
		List all clothing parts
		---
		tags:
		  - Master Data
		responses:
			200:
				description: List all clothing parts
			schema:
				type: object
				properties:
				message:
					type: string
				data:
					type: array
					items:
					type: string
				total:
					type: integer
		"""
		data = [item.value.json() for item in ClothingParts]
		return CommonResponse.ok("Get clothing parts successfully", data, len(data))

class EvaluationStatusListResource(Resource):
	def get(self):
		"""
		List all evaluation status
		---
		tags:
		  - Master Data
		responses:
			200:
				description: List all evaluation status
			schema:
				type: object
				properties:
				message:
					type: string
				data:
					type: array
					items:
					type: string
				total:
					type: integer
		"""
		data = [ item.value.json() for item in EvaluationStatus]
		return CommonResponse.ok("Get evaluation status successfully", data, len(data))