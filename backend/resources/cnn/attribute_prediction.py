from flask_restful import Resource, reqparse
from models.attribute_prediction import AttributePrediction
from models.category import Category
from models.common.response import CommonResponse

# class AttributePredictionResource(Resource):
# 	parser = reqparse.RequestParser()
# 	parser.add_argument("name", type=str, required=True, help="This field cannot be blank.")

# 	arser = reqparse.RequestParser()
# 	parser.add_argument("name", type=str, required=True, help="This field cannot be blank.")

# 	def get(self, prediction_id):
# 		"""
# 		Find an attribute prediction by its ID.
# 		---
# 		tags:
# 			- CNN
# 			- Attribute Prediction
# 		parameters:
# 		  - name: prediction_id
# 		    in: path
# 		    type: integer
# 		    required: true
# 		    description: The attribute prediction ID
# 		"""
# 		prediction = AttributePrediction.find_by_id(prediction_id)
# 		if prediction:
# 			return CommonResponse.ok(message="Attribute prediction found.", data=prediction.json())
# 		return CommonResponse.not_found(message="Attribute prediction not found.")

# 	def put(self, prediction_id):
# 		"""
# 		Update an attribute prediction by its ID.
# 		---
# 		tags:
# 			- CNN
# 			- Attribute Prediction
# 		parameters:
# 		  - name: prediction_id
# 		    in: path
# 		    type: integer
# 		    required: true
# 		    description: The attribute prediction ID
# 		  - name: name
# 		    in: path
# 		    type: string
# 		    required: true
# 		    description: The attribute prediction name
# 		"""
# 		data = AttributePredictionResource.parser.parse_args()
# 		prediction = AttributePrediction.query.get(prediction_id)
# 		if prediction:
# 			prediction.name = data["name"]
# 			prediction.save_to_db()
# 			return CommonResponse.ok(message="Attribute prediction updated.", data=prediction.json())
# 		return CommonResponse.not_found(message="Attribute prediction not found.")

# 	def delete(self, prediction_id):
# 		"""
# 		Delete an attribute prediction by its ID.
# 		---
# 		tags:
# 			- CNN
# 			- Attribute Prediction
# 		parameters:
# 		  - name: prediction_id
# 		    in: path
# 		    type: integer
# 		    required: true
# 		    description: The attribute prediction ID
# 		"""
# 		prediction = AttributePrediction.query.get(prediction_id)
# 		if prediction:
# 			prediction.delete_from_db()
# 			return CommonResponse.ok(message="Attribute prediction deleted.", data=prediction.json())
# 		return CommonResponse.not_found(message="Attribute prediction not found.")

class AttributePredictionCreateListResource(Resource):
	# parser = reqparse.RequestParser()
	# parser.add_argument("name", type=str, required=True, help="This field cannot be blank.")

	# def post(self):
	# 	"""
	# 	Create a list of attribute predictions.
	# 	---
	# 	tags:
	# 		- CNN
	# 		- Attribute Prediction
	# 	parameters:
	# 	  - name: name
	# 	    in: body
	# 	    type: string
	# 	    required: true
	# 	    description: The attribute prediction name
	# 	"""
	# 	data = AttributePredictionCreateListResource.parser.parse_args()
	# 	prediction = AttributePrediction(**data)
	# 	prediction.save_to_db()
	# 	return CommonResponse.created(message="Attribute prediction created.", data=prediction.json())

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