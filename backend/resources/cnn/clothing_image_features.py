import json
import os
import pdb

import pandas as pd
from models.enum import MessageType, ResponseMessage, ResponseURL
from models.history_model import History
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
from resources.cnn.data_preprocessing import data_preprocessing, get_preprocessing_info
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
from resources.cnn.search_image import extract_features
from werkzeug.utils import secure_filename
from app_factory import app

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


class PreProcessingResource(Resource):
	def get(self):
		"""
		Get Information about Data Pre-processing.
		---
		tags:
			- CNN
			- Training
		responses:
			200:
				description: Information about Data Pre-processing
				schema:
				id: CNNTraining
				properties:
					data:
						type: string
						description: Information about Data Pre-processing
		"""
		# Gọi hàm tiền xử lý
		data = get_preprocessing_info()
		return CommonResponse.ok(message="Information about Data Pre-processing.", data=data)
	
	def post(self):
		"""
		Pre-process the data.
		---
		tags:
			- CNN
			- Training
		responses:
			200:
				description: Pre-processing started
				schema:
				id: CNNTraining
				properties:
					data:
						type: string
						description: Pre-processing started
		"""
		# Gọi hàm tiền xử lý
		data = data_preprocessing()
		return CommonResponse.ok(message="Pre-processing successful.", data=data)

class CNNPredictResource(Resource):
	def get(self):
		"""
		Predict the category of the image.
		---
		tags:
			- CNN
			- Training
		parameters:
			- in: formData
			  name: image
			  type: file
			  required: true
			  description: The image file
		responses:
			200:
				description: Category predicted
				schema:
				id: CNNPredict
				properties:
					data:
						type: string
						description: Category predicted
		"""
		args = request.args
		image_path = args.get('image_path')
		# Gọi hàm dự đoán
		predictions = extract_features(image_path)
		return CommonResponse.ok(message="Category predicted.", data=predictions)
	
class UploadImageResource(Resource):
    """
    Upload image resource
    ---
    tags:
      - CNN
    parameters:
        - in: formData
            name: image
            type: file
            required: true
            description: The file to upload.
    responses:
        200:
            description: The image has been uploaded successfully.
        400:
            description: The image has not been uploaded.
    """
    def post(self):
        if 'file_image' in request.files:
            return self.upload_image(request)

    def upload_image(self, request):
        file = request.files['file_image']
        session_user = request.form.get('session_user')
        
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            attributes, category = self.extract_features(file_path)
            attribute_ids = ','.join([str(attribute.id) for attribute in attributes])
            category_ids = ','.join([str(cate.id) for cate in category])
            
            product_url = ResponseURL.URL_IMAGE.value.format(attributes=attribute_ids, categories=category_ids)
            
            response_chatbot = ""
            if len(attributes) > 0 or len(category) > 0:
                response_chatbot += ResponseURL.TAG_A.value.format(url=product_url, text_user=ResponseMessage.MESSAGE_RESPONSE.value)
            else:
                response_chatbot = ResponseMessage.MESSAGE_NOTFOUND.value
            
            user_say_image_url = f"{request.host_url}static/uploads/{filename}"
            
            history = History(
                session_user=session_user,
                user_say=user_say_image_url,
                chat_response=response_chatbot,
                concepts=json.dumps([]),
                message_type=MessageType.IMAGE.value
            )
            history.save()
            
            return jsonify({
                "answer": response_chatbot
            })
        else:
            return jsonify({
                "message": "Các loại hình ảnh được phép là -> png, jpg, jpeg, gif",
                "url": request.url,
                "attributes": attributes,
                "categories": category,
            })
