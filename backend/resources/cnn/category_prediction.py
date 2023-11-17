from flask_restful import Resource, reqparse
from models.category_prediction_model import (
    CategoryPrediction,  # Thay thế 'category_prediction' bằng tên thực tế của module
)
from models.common.response import CommonResponse


class CategoryPredictionCreateListResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("name", type=str, required=True, help="This field cannot be blank.")

	def get(self):
		"""
		Get a list of category predictions.
		---
		tags:
			- CNN
			- Category Prediction

		responses:
		  200:
		    description: Category predictions found
		    schema:
		      id: CategoryPrediction
		      properties:
		        status:
		          type: string
		          description: The status of the category predictions
		          default: success
		        message:
		          type: string
		          description: The message of the category predictions
		          default: Category predictions found.
		        data:
		          type: array
		          description: The category predictions data
		          default: []
		  404:
		    description: Category predictions not found
		    schema:
		      id: CategoryPrediction
		      properties:
		        status:
		          type: string
		          description: The status of the category predictions
		          default: error
		        message:
		          type: string
		          description: The message of the category predictions
		          default: Category predictions not found.
		definitions:
			CategoryPrediction:
				type: object
				properties:
					id:
						type: integer
						description: The category prediction ID
					name:
						type: string
						description: The category prediction name
		"""
		predictions = CategoryPrediction.get_all()  # Sửa hàm truy vấn để lấy danh sách tất cả dự đoán
		return CommonResponse.ok(message="Category predictions found.", data=[prediction.json() for prediction in predictions])