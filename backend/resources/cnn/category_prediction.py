from flask_restful import Resource, reqparse
from models.category_prediction import (
    CategoryPrediction,  # Thay thế 'category_prediction' bằng tên thực tế của module
)
from models.common.response import CommonResponse

# class CategoryPredictionResource(Resource):
# 	parser = reqparse.RequestParser()
# 	parser.add_argument("name", type=str, required=True, help="This field cannot be blank.")

# 	def get(self, prediction_id):
# 		"""
# 		Find a category prediction by its ID.
# 		---
# 		tags:
# 			- CNN
# 			- Category Prediction
# 		parameters:
# 		  - name: prediction_id
# 		    in: path
# 		    type: integer
# 		    required: true
# 		    description: The category prediction ID
# 		"""
# 		prediction = CategoryPrediction.find_by_id(prediction_id)  # Sửa hàm tìm kiếm dự đoán theo ID tương ứng
# 		if prediction:
# 			return CommonResponse.ok(message="Category prediction found.", data=prediction.json())
# 		return CommonResponse.not_found(message="Category prediction not found.")

# 	def put(self, prediction_id):
# 		"""
# 		Update a category prediction by its ID.
# 		---
# 		tags:
# 			- CNN
# 			- Category Prediction
# 		parameters:
# 		  - name: prediction_id
# 		    in: path
# 		    type: integer
# 		    required: true
# 		    description: The category prediction ID
# 		  - name: name
# 		    in: path
# 		    type: string
# 		    required: true
# 		    description: The category prediction name
# 		"""
# 		data = CategoryPredictionResource.parser.parse_args()
# 		prediction = CategoryPrediction.query.get(prediction_id)  # Sửa hàm truy vấn dự đoán theo ID tương ứng
# 		if prediction:
# 			prediction.name = data["name"]
# 			prediction.save_to_db()
# 			return CommonResponse.ok(message="Category prediction updated.", data=prediction.json())
# 		return CommonResponse.not_found(message="Category prediction not found.")

# 	def delete(self, prediction_id):
# 		"""
# 		Delete a category prediction by its ID.
# 		---
# 		tags:
# 			- CNN
# 			- Category Prediction
# 		parameters:
# 		  - name: prediction_id
# 		    in: path
# 		    type: integer
# 		    required: true
# 		    description: The category prediction ID
# 		"""
# 		prediction = CategoryPrediction.query.get(prediction_id)  # Sửa hàm truy vấn dự đoán theo ID tương ứng
# 		if prediction:
# 			prediction.delete_from_db()
# 			return CommonResponse.ok(message="Category prediction deleted.", data=prediction.json())
# 		return CommonResponse.not_found(message="Category prediction not found.")

class CategoryPredictionCreateListResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("name", type=str, required=True, help="This field cannot be blank.")

	# def post(self):
	# 	"""
	# 	Create a list of category predictions.
	# 	---
	# 	tags:
	# 		- CNN
	# 		- Category Prediction
	# 	parameters:
	# 	  - name: name
	# 	    in: body
	# 	    type: string
	# 	    required: true
	# 	    description: The category prediction name
	# 	"""
	# 	data = CategoryPredictionCreateListResource.parser.parse_args()
	# 	prediction = CategoryPrediction(**data)  # Thêm các trường dữ liệu khác cho đối tượng dự đoán
	# 	prediction.save_to_db()
	# 	return CommonResponse.created(message="Category prediction created.", data=prediction.json())

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