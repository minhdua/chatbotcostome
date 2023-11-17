import pdb

import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from models.clothing_image_features_model import (
    ClothingImageFeatures,  # Thay thế 'clothing_image_features' bằng tên thực tế của module
)
from models.common.response import CommonResponse
from models.fashionet_model import FashionNetModel
from resources.cnn.fashion_net import (
    build_model,
    change_stage,
    cnn_training,
    compute_test_accuracy,
    load_modelfile,
)


class ClothingImageFeaturesResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("image_name", type=str, required=True, help="This field cannot be blank.")

	def get(self, feature_id):
		"""
		Find clothing image features by ID.
		---
		tags:
			- CNN
			- Clothing Image Features
		parameters:
		  - name: feature_id
		    in: path
		    type: integer
		    required: true
		    description: The ID of the clothing image features
		"""
		feature = ClothingImageFeatures.find_by_id(feature_id)  # Sửa hàm tìm kiếm tính năng theo ID tương ứng
		if feature:
			return CommonResponse.ok(message="Clothing image features found.", data=feature.json())
		return CommonResponse.not_found(message="Clothing image features not found.")
	def put(self, feature_id):
		"""
		Update clothing image features by ID.
		---
		tags:
			- CNN
			- Clothing Image Features
		parameters:
		  - name: feature_id
		    in: path
		    type: integer
		    required: true
		    description: The ID of the clothing image features
		  - name: image_name
		    in: body
		    type: string
		    required: true
		    description: The image name
		"""
		data = ClothingImageFeaturesResource.parser.parse_args()
		feature = ClothingImageFeatures.query.get(feature_id)  # Sửa hàm truy vấn tính năng theo ID tương ứng
		if feature:
			feature.image_name = data["image_name"]
			feature.save_to_db()
			return CommonResponse.ok(message="Clothing image features updated.", data=feature.json())
		return CommonResponse.not_found(message="Clothing image features not found.")
	def delete(self, feature_id):
		"""
		Delete clothing image features by ID.
		---
		tags:
			- CNN
			- Clothing Image Features
		parameters:
		  - name: feature_id
		    in: path
		    type: integer
		    required: true
		    description: The ID of the clothing image features
		"""
		feature = ClothingImageFeatures.query.get(feature_id)  # Sửa hàm truy vấn tính năng theo ID tương ứng
		if feature:
			feature.delete_from_db()
			return CommonResponse.ok(message="Clothing image features deleted.", data=feature.json())
		return CommonResponse.not_found(message="Clothing image features not found.")

class ClothingImageFeaturesCreateListResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("image_name", type=str, required=True, help="This field cannot be blank.")

	def post(self):
		"""
		Create clothing image features.
		---
		tags:
			- CNN
			- Clothing Image Features
		parameters:
		  - name: image_name
		    in: body
		    type: string
		    required: true
		    description: The image name
		"""
		data = ClothingImageFeaturesCreateListResource.parser.parse_args()
		feature = ClothingImageFeatures(**data)  # Thêm các trường dữ liệu khác cho đối tượng tính năng
		feature.save_to_db()
		return CommonResponse.created(message="Clothing image features created.", data=feature.json())

	def get(self):
		"""
		Get a list of clothing image features.
		---
		tags:
			- CNN
			- Clothing Image Features
		parameters:
		  - name: page
		    in: query
		    type: integer
		    required: false
		    description: The page number
		  - name: per_page
		    in: query
		    type: integer
		    required: false
		    description: The number of items per page
		  - name: sort_field
		    in: query
		    type: string
		    required: false
		    description: The field to sort by
		  - name: sort_order
		    in: query
		    type: string
		    required: false
		    description: The sort order (asc or desc)
		responses:
			200:
				description: A list of clothing image features
				schema:
				id: ClothingImageFeaturesList
				properties:
					data:
					type: array
					items:
						$ref: '#/definitions/ClothingImageFeatures'
					total:
						type: integer
						description: The total number of clothing image features
					current_page:
						type: integer
						description: The current page number
					per_page:
						type: integer
						description: The number of items per page
			404:
				description: Clothing image features not found

		definitions:
			ClothingImageFeatures:
				properties:
					id:
						type: integer
						description: The clothing image features ID
					image_name:
						type: string
						description: The image name
					item_id:
						type: integer
						description: The item ID
					evaluation_status:
						type: string
						description: The evaluation status
					landmark_visibility_1:
						type: integer
						description: The landmark visibility 1
					landmark_visibility_2:
						type: integer
						description: The landmark visibility 2
					landmark_visibility_3:
						type: integer
						description: The landmark visibility 3
					landmark_visibility_4:
						type: integer
						description: The landmark visibility 4
					landmark_visibility_5:
						type: integer
						description: The landmark visibility 5
					landmark_visibility_6:
						type: integer
						description: The landmark visibility 6
					landmark_visibility_7:
						type: integer
						description: The landmark visibility 7
					landmark_visibility_8:
						type: integer
						description: The landmark visibility 8
					landmark_location_x_1:
						type: float
						description: The landmark location x 1
					landmark_location_x_2:
						type: float
						description: The landmark location x 2
					landmark_location_x_3:
						type: float
						description: The landmark location x 3
					landmark_location_x_4:	
						type: float
						description: The landmark location x 4	
					landmark_location_x_5:
						type: float
						description: The landmark location x 5
					landmark_location_x_6:
						type: float
						description: The landmark location x 6
					landmark_location_x_7:
						type: float
						description: The landmark location x 7
					landmark_location_x_8:
						type: float
						description: The landmark location x 8
					landmark_location_y_1:
						type: float
						description: The landmark location y 1
					landmark_location_y_2:
						type: float
						description: The landmark location y 2
					landmark_location_y_3:
						type: float
						description: The landmark location y 3
					landmark_location_y_4:
						type: float
						description: The landmark location y 4
					landmark_location_y_5:
						type: float
						description: The landmark location y 5
					landmark_location_y_6:
						type: float
						description: The landmark location y 6
					landmark_location_y_7:
						type: float
						description: The landmark location y 7
					landmark_location_y_8:
						type: float
						description: The landmark location y 8
					category_label:
						type: string
						description: The category label
					attribute_labels:
						type: string
						description: The attribute labels
					gender:
						type: integer
						description: -1 if women , 1 if men else 0
		"""
		page = int(request.args.get('page', 1))
		per_page = int(request.args.get('per_page', -1))
		sort_field = request.args.get('sort_field', 'id')
		sort_order = request.args.get('sort_order')
		features = ClothingImageFeatures.get_all()
		features_2 = ClothingImageFeatures.get_feature_group_by_item_id()
		  # Sửa hàm truy vấn để lấy danh sách tất cả tính năng
		# features = [feature for feature in features if feature.image_name.contains('_5_')]
		if per_page < 0:
			per_page = len(features)
		start_index = (page - 1) * per_page
		end_index = start_index + per_page
		features_paginated = features[start_index:end_index]
		if sort_order == 'desc':
			features_paginated = sorted(features_paginated, key=lambda feature: getattr(feature, sort_field), reverse=True)
		else:
			features_paginated = sorted(features_paginated, key=lambda feature: getattr(feature, sort_field))
		
		data=[feature.json() for feature in features_paginated]
		return CommonResponse.ok(message="Clothing image features found.", data=[feature.json() for feature in features_paginated], total=len(features), current_page=page, per_page=per_page)
	
class ClothingImageFeaturesNewIdResource(Resource):
	def get(self):
		"""
		Get the new item ID for clothing image features.
		---
		tags:
			- CNN
			- Clothing Image Features
		responses:
			200:
				description: The new ID for clothing image features
				schema:
				id: ClothingImageFeaturesNewId
				properties:
					data:
						type: string
						description: The new item ID for clothing image features
		"""
		new_id = ClothingImageFeatures.get_new_id()
		return CommonResponse.ok(message="New ID for clothing image features found.", data={"new_id": new_id})


class CNNTrainingResource(Resource):
	def get(self):
		"""
		Get a list of CNN training.
		---
		tags:
			- CNN
			- Training
		parameters:
		  - name: page
		    in: query
		    type: integer
		    required: false
		    description: The page number
		  - name: per_page
		    in: query
		    type: integer
		    required: false
		    description: The number of items per page
		  - name: sort_field
		    in: query
		    type: string
		    required: false
		    description: The field to sort by
		  - name: sort_order
		    in: query
		    type: string
		    required: false
		    description: The sort order (asc or desc)
		responses:
			200:
				description: A list of CNN training
				schema:
				id: CNNTrainingList
				properties:
					data:
					type: array
					items:
						$ref: '#/definitions/CNNTraining'
					total:
						type: integer
						description: The total number of CNN training
					current_page:
						type: integer
						description: The current page number
					per_page:
						type: integer
						description: The number of items per page
			404:
				description: CNN training not found

		definitions:
			CNNTraining:
				properties:
					id:
						type: integer
						description: The CNN training ID
					model_file:
						type: string
						description: The model file
					epochs:
						type: integer
						description: The number of epochs
					batch_size:
						type: integer
						description: The batch size
					lr:
						type: number
						description: The learning rate
					stage:
						type: integer
						description: The stage
					save_interval:
						type: integer
						description: The save interval
					created_at:
						type: string
						description: The created at
		"""
		page = int(request.args.get('page', 1))
		per_page = int(request.args.get('per_page', -1))
		sort_field = request.args.get('sort_field', 'id')
		sort_order = request.args.get('sort_order')
		training = FashionNetModel.get_all()
		if per_page < 0:
			per_page = len(training)
		start_index = (page - 1) * per_page
		end_index = start_index + per_page
		training_paginated = training[start_index:end_index]
		if sort_order == 'desc':
			training_paginated = sorted(training_paginated, key=lambda training: getattr(training, sort_field), reverse=True)
		else:
			training_paginated = sorted(training_paginated, key=lambda training: getattr(training, sort_field))
		return CommonResponse.ok(message="CNN training found.", data=[training.json() for training in training_paginated], total=len(training), current_page=page, per_page=per_page)
	
	def post(self):
		"""
		Train the CNN model.
		---
		tags:
			- CNN
			- Training
		parameters:
			- in: query
			  name: model_file
			  type: string
			  description: Tên tệp mô hình để lưu hoặc nạp
			- in: query
			  name: epochs
			  default: 1
			  type: integer
			  description: Số epoch để huấn luyện mô hình
			- in: query
			  name: batch_size
			  default: 64
			  type: integer
			  description: Kích thước batch cho huấn luyện
			- in: query
			  name: lr
			  type: number
			  default: 0.0003
			  description: Tỷ lệ học tập
			- in: query
			  name: stage
			  default: 1
			  type: integer
			  description: Giai đoạn huấn luyện (1 hoặc 2)
			- in: query
			  name: save_interval
			  default: 1
			  type: integer
			  description: Khoảng cách để lưu mô hình
		responses:
			200:
				description: Training started
				schema:
				id: CNNTraining
				properties:
					data:
						type: string
						description: Training started
		"""
		args = request.args
		model_file = args.get('model_file')
		epochs = int(args.get('epochs', '1'))
		batch_size = int(args.get('batch_size', '64'))
		lr = float(args.get('lr', '0.0003'))
		stage = int(args.get('stage', '1'))
		save_interval = int(args.get('save_interval', '1'))
		# Gọi hàm huấn luyện với các tham số được truyền vào
		cnn_training(model_file, epochs, batch_size, lr, stage, save_interval)
		return CommonResponse.ok(message="Training started.")
	
	
class UpdateAccuracyResource(Resource):
	def post(self):
		"""
		Update the accuracy of the CNN model.
		---
		tags:
			- CNN
			- Training
		responses:
			200:
				description: Accuracy updated
				schema:
				id: CNNTraining
				properties:
					data:
						type: string
						description: Accuracy updated
		"""
		models = FashionNetModel.get_all()
		test_data = ClothingImageFeatures.get_all()
		filtered_test_data = [data for data in test_data if data.evaluation_status == "gallery"]

		# Convert the filtered data into a DataFrame
		test_df = pd.DataFrame([data.json() for data in filtered_test_data])
		error_count = 0
		for saved_model in models:
			model_file = saved_model.model_file
			lr = saved_model.lr
			stage = saved_model.stage
			batch_size = saved_model.batch_size
			model_source, model_blue = build_model()
			model = load_modelfile(model_source, model_file)
			model = change_stage(model, lr, stage)
			blue_cates_acc, blue_lands_acc, red_green_cates_acc, red_green_attrs_acc, test_accuracy = compute_test_accuracy(model, test_df, batch_size)
			
			saved_model.blue_cates_acc = blue_cates_acc
			saved_model.blue_lands_acc = blue_lands_acc
			saved_model.red_green_cates_acc = red_green_cates_acc
			saved_model.red_green_attrs_acc = red_green_attrs_acc
			saved_model.test_accuracy = test_accuracy
			try:
				saved_model.update_to_db()
			except:
				error_count += 1
				
		if error_count > 0:
			return CommonResponse.ok(message="Accuracy updated but some errors occurred.")
		return CommonResponse.ok(message="Accuracy updated.")


			
