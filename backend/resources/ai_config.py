from flask_restful import Resource, reqparse
from models.ai_config_model import AiConfig
from models.common.response import CommonResponse
from models.fashionet_model import FashionNetModel


class AiConfigResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("config_name", type=str, required=True, help="This field cannot be blank.")
	parser.add_argument("description", type=str, required=False, help="This field cannot be blank.")
	parser.add_argument("string_value", type=str, required=False, help="This field cannot be blank.")
	parser.add_argument("int_value", type=int, required=False, help="This field cannot be blank.")
	parser.add_argument("float_value", type=float, required=False, help="This field cannot be blank.")
	parser.add_argument("bool_value", type=bool, required=False, help="This field cannot be blank.")

	def get(self, config_name):
		"""
		Find a ai_config by its name.
		---
		tags:
			- AiConfig
		parameters:
		  - name: config_name
		    in: path
		    type: string
		    required: true
		    description: The ai_config name
		responses:
		  200:
		    description: AiConfig found
		    schema:
		      id: AiConfig
		      properties:
		        status:
		          type: string
		          description: The status of the ai_config
		          default: success
		        message:
		          type: string
		          description: The message of the ai_config
		          default: AiConfig found.
		        data:
		          type: object
		          description: The ai_config data
		          default: {}
		  404:
		    description: AiConfig not found
		    schema:
		      id: AiConfig
		      properties:
		        status:
		          type: string
		          description: The status of the ai_config
		          default: error
		        message:
		          type: string
		          description: The message of the ai_config
		          default: AiConfig not found.
		"""
		ai_config = AiConfig.find_by_name(config_name)
		if ai_config:
			return CommonResponse.ok(message="AiConfig found.", data=ai_config.json())
		return CommonResponse.not_found(message="AiConfig not found.")

	def post(self):
		"""
		Create a new ai_config.
		---
		tags:
			- AiConfig
		parameters:
			- in: body
			  name: body
			  schema:
				$ref: '#/definitions/AiConfig'
			  examples:
				application/json:
				  config_name: new_config
				  description: new config
				  string_value: new config
				  int_value: 1
				  float_value: 1.0
		responses:
			200:
				description: AiConfig created
				schema:
				$ref: '#/definitions/AiConfig'
			400:
				description: AiConfig already exists
		
		definitions:
			AiConfig:
				type: object
				properties:
					config_name:
						type: string
						description: The ai_config name
						default: new_config
					description:
						type: string
						description: The ai_config description
					string_value:
						type: string
						description: The ai_config string_value
					int_value:
						type: integer
						description: The ai_config int_value
					float_value:
						type: float
						description: The ai_config float_value
					bool_value:
						type: boolean
						description: The ai_config bool_value
		"""
		data = AiConfigResource.parser.parse_args()
		ai_config = AiConfig.find_by_name(data["config_name"])
		if ai_config:
			return CommonResponse.bad_request(message="AiConfig already exists.")
		ai_config = AiConfig(**data)
		ai_config.save_to_db()
		return CommonResponse.ok(message="AiConfig created.", data=ai_config.json())
	
	def put(self):
		"""
		Update an ai_config.
		---
		tags:
			- AiConfig
		parameters:
			- in: body
			  name: body
			  schema:
				$ref: '#/definitions/AiConfig'
			  examples:
				application/json:
				  config_name: new_config
				  description: new config
				  string_value: new config
				  int_value: 1
				  float_value: 1.0
		responses:
			200:
				description: AiConfig updated
				schema:
				$ref: '#/definitions/AiConfig'
			404:
				description: AiConfig not found
		
		definitions:
			AiConfig:
				type: object
				properties:
					config_name:
						type: string
						description: The ai_config name
						default: new_config
					description:
						type: string
						description: The ai_config description
					string_value:
						type: string
						description: The ai_config string_value
					int_value:
						type: integer
						description: The ai_config int_value
					float_value:
						type: float
						description: The ai_config float_value
					bool_value:
						type: boolean
						description: The ai_config bool_value
		"""
		data = AiConfigResource.parser.parse_args()
		ai_config = AiConfig.find_by_name(data["config_name"])
		if not ai_config:
			return CommonResponse.not_found(message="AiConfig not found.")
		ai_config.update(**data)
		return CommonResponse.ok(message="AiConfig updated.", data=ai_config.json())
	
	def delete(self, config_name):
		"""
		Delete an ai_config.
		---
		tags:
			- AiConfig
		parameters:
		  - name: config_name
		    in: path
		    type: string
		    required: true
		    description: The ai_config name
		responses:
		  200:
		    description: AiConfig deleted
		    schema:
		      id: AiConfig
		      properties:
		        status:
		          type: string
		          description: The status of the ai_config
		          default: success
		        message:
		          type: string
		          description: The message of the ai_config
		          default: AiConfig deleted.
		        data:
		          type: object
		          description: The ai_config data
		          default: {}
		  404:
		    description: AiConfig not found
		    schema:
		      id: AiConfig
		      properties:
		        status:
		          type: string
		          description: The status of the ai_config
		          default: error
		        message:
		          type: string
		          description: The message of the ai_config
		          default: AiConfig not found.
		"""
		ai_config = AiConfig.find_by_name(config_name)
		if not ai_config:
			return CommonResponse.not_found(message="AiConfig not found.")
		ai_config.delete_from_db()
		return CommonResponse.ok(message="AiConfig deleted.", data=ai_config.json())

class BestCNNModelUpdateResource(Resource):
	def get(self):
		"""
		Get best cnn model.
		---
		tags:
			- AiConfig
		responses:
			200:
				description: Best cnn model found
				schema:
				$ref: '#/definitions/AiConfig'
			404:
				description: Best cnn model not found
				schema:
				$ref: '#/definitions/AiConfig'
		definitions:
			AiConfig:
				type: object
				properties:
					config_name:
						type: string
						description: The ai_config name
						default: best_cnn_model
					description:
						type: string
						description: The ai_config description
					string_value:
						type: string
						description: The ai_config string_value
		"""
		models = FashionNetModel.get_all()
		models.sort(key=lambda x: x.test_accuracy, reverse=True)
		if len(models) > 0:
			best_model = models[0]
			ai_config = AiConfig.find_by_name("cnn_model_name")
			if not ai_config:
				ai_config = AiConfig(config_name="cnn_model_name", description="Best CNN model", string_value=best_model.model_file)
				ai_config.save_to_db()
			return CommonResponse.ok(message="Best cnn model found.", data=ai_config.json())
	
	def put(self):
		"""
		Update best cnn model.
		---
		tags:
			- AiConfig
		responses:
			200:
				description: Best cnn model updated
				schema:
				$ref: '#/definitions/AiConfig'
			404:
				description: Best cnn model not found
		definitions:
			AiConfig:
				type: object
				properties:
					config_name:
						type: string
						description: The ai_config name
						default: best_cnn_model
					description:
						type: string
						description: The ai_config description
					string_value:
						type: string
						description: The ai_config string_value
		"""
		models = FashionNetModel.get_all()
		models.sort(key=lambda x: x.test_accuracy, reverse=True)
		if len(models) > 0:
			best_model = models[0]
			ai_config = AiConfig.find_by_name("cnn_model_name")
			if not ai_config:
				ai_config = AiConfig(config_name="cnn_model_name", description="Best CNN model", string_value=best_model.model_file)
				ai_config.save_to_db()
			else:
				ai_config.update(string_value=best_model.model_file)
			return CommonResponse.ok(message="Best cnn model updated.", data=ai_config.json())

