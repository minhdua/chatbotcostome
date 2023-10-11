from flask_restful import Resource, reqparse
from models.attribute_prediction_model import AttributePrediction
from models.category_model import Category
from models.common.response import CommonResponse


class AttributePredictionCreateListResource(Resource):
	
	def get(self):
		"""
		Get a list of attribute predictions.
		---
		tags:
			- CNN
			- Attribute Prediction

		responses:
			200:
				description: A list of attribute predictions
				schema:
					id: AttributePredictionList
					properties:
						status:
							type: string
							description: The response status
						message:
							type: string
							description: The response message
						data:
							type: array
							items:
								$ref: '#/definitions/AttributePrediction'
			404:
				description: Attribute predictions not found
				schema:
					id: AttributePredictionList
					properties:
						status:
							type: string
							description: The response status
						message:
							type: string
							description: The response message
		definitions:
			AttributePrediction:
				properties:
					id:
						type: integer
						description: The attribute prediction ID
					name:
						type: string
						description: The attribute prediction name
		"""
		predictions = AttributePrediction.get_all()
		return CommonResponse.ok(message="Attribute predictions found.", data=[prediction.json() for prediction in predictions])