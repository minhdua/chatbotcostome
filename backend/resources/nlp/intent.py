
from app_factory import swagger
from flask_restful import Resource, reqparse
from models.base_mixin import CommonResponse
from models.nlp.intent import Intent
from models.nlp.pattern import Pattern
from models.nlp.response import Response


class IntentResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("tag", type=str, required=True, help="This field cannot be blank.")
	parser.add_argument("description", type=str, required=True, help="This field cannot be blank.")
	parser.add_argument("patterns", type=list,  help="This field can be blank.", nullable=True, default=[])
	parser.add_argument("responses", type=list,  help="This field can be blank.", nullable=True, default=[])

	def get(self, tag):
		"""
		Get intent by tag
		---
		tags:
			- Intent
		parameters:
			- in: path
			  name: tag
			  type: string
			  required: true
			  description: The tag of the intent

		definitions:
			Intent:
				type: object
				properties:
					id:
						type: integer
						description: The intent ID
					tag:
						type: string
						description: The intent tag
					description:
						type: string
						description: The intent description
					patterns:
						type: array
						items:
							$ref: '#/definitions/Pattern'
					responses:
						type: array
						items:
							$ref: '#/definitions/Response'
			Pattern:
				type: object
				properties:
					id:
						type: integer
						description: The pattern ID
					pattern_text:
						type: string
						description: The pattern text
					intent_id:
						type: integer
						description: The intent ID
			Response:
				type: object
				properties:
					id:
						type: integer
						description: The response ID
					response_text:
						type: string
						description: The response text
					intent_id:
						type: integer
						description: The intent ID
		responses:
			200:
				description: The intent
				schema:
					id: Intent
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
						data:
							$ref: '#/definitions/Intent'
				examples:
					application/json: {
						"status": "success",
						"message": "Intent found.",
						"data": {
							"id": 1,
							"tag": "greeting",
							"description": "Greeting intent",
							"patterns": [
								{
									"id": 1,
									"pattern_text": "Hi",
									"intent_id": 1
								},
								{
									"id": 2,
									"pattern_text": "Hello",
									"intent_id": 1
								}
							],
							"responses": [
								{
									"id": 1,
									"response_text": "Hello, how are you?",
									"intent_id": 1
								},
								{
									"id": 2,
									"response_text": "Good to see you again.",
									"intent_id": 1
								}
							]
						}
					}
			404:
				description: The intent not found
				schema:
					id: IntentNotFound
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
				examples:
					application/json: {
						"status": "error",
						"message": "Intent not found."
					}

		"""
		intent = Intent.find_by_tag(tag)
		if intent:
			return CommonResponse(status="success", message="Intent found.", data=intent.json()).json(), 200
		return CommonResponse(status="error", message="Intent not found.").json(), 404
	
	def post(self, tag):
		"""
		Create intent
		---
		tags:
			- Intent
		parameters:
			- in: path
			  name: tag
			  type: string
			  required: true
			  description: The tag of the intent
			- in: path
			  name: description
			  type: string
			  required: true
			  description: The description of the intent
			- in: body  
			  name: patterns
			  type: array
			  required: false
			  description: The patterns of the intent
			- in: body  
			  name: responses
			  type: array
			  required: false
			  description: The responses of the intent
		definitions:
			Intent:
				type: object
				properties:
					tag:
						type: string
						description: The intent tag
					description:
						type: string
						description: The intent description
					patterns:
						type: array
						items:
							$ref: '#/definitions/Pattern'
					responses:
						type: array
						items:
							$ref: '#/definitions/Response'
			Pattern:
				type: object
				properties:
					pattern_text:
						type: string
						description: The pattern text
			Response:
				type: object
				properties:
					response_text:
						type: string
						description: The response text
		responses:
			200:
				description: The intent
				schema:
					id: Intent
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
						data:
							$ref: '#/definitions/Intent'
				examples:
					application/json: {
						"status": "success",
						"message": "Intent created successfully.",
						"data": {
							"id": 1,
							"tag": "greeting",
							"description": "Greeting intent",
							"patterns": [
								{
									"id": 1,
									"pattern_text": "Hi",
									"intent_id": 1
								},
								{
									"id": 2,
									"pattern_text": "Hello",
									"intent_id": 1
								}
							],
							"responses": [
								{
									"id": 1,
									"response_text": "Hello, how are you?",
									"intent_id": 1
								},
								{
									"id": 2,
									"response_text": "Good to see you again.",
									"intent_id": 1
								}
							]
						}
					}
			400:
				description: The intent already exists
				schema:
					id: IntentAlreadyExists
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
				examples:
					application/json: {
						"status": "error",
						"message": "An intent with tag 'greeting' already exists."
					}
			500:
				description: An error occurred while creating the intent
				schema:
					id: IntentCreationError
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response	
				examples:
					application/json: {
						"status": "error",
						"message": "An error occurred while creating the intent."
					}
		"""
		if Intent.find_by_tag(tag):
			return CommonResponse(status="error", message="An intent with tag '{}' already exists.".format(tag)).json(), 400
		
		data = IntentResource.parser.parse_args()

		patterns = data.pop("patterns")
		responses = data.pop("responses")

		intent = Intent(tag, **data)
		try:
			intent.save_to_db()

			# Lưu patterns
			for pattern in patterns:
				parttern = Pattern(pattern, intent.id)
				parttern.save_to_db()

			# Lưu responses
			for response in responses:
				response = Response(response, intent.id)
				response.save_to_db()

		except:
			return CommonResponse(status="error", message="An error occurred while creating the intent.").json(), 500
		
		return CommonResponse(status="success", message="Intent created successfully.", data=intent.json()).json(), 201
	
	def delete(self, tag):
		"""
		Delete intent
		---
		tags:
			- Intent
		parameters:
			- in: path
			  name: tag
			  type: string
			  required: true
			  description: The tag of the intent
		responses:
			200:
				description: The intent
				schema:
					id: Intent
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
				examples:
					application/json: {
						"status": "success",
						"message": "Intent deleted successfully."
					}
			404:
				description: The intent not found
				schema:
					id: IntentNotFound
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
				examples:
					application/json: {
						"status": "error",
						"message": "Intent not found."
					}
		"""
		intent = Intent.find_by_tag(tag)
		if intent:
			intent.delete_from_db()
			return CommonResponse(status="success", message="Intent deleted successfully.").json(), 200
		return CommonResponse(status="error", message="Intent not found.").json(), 404
	
	def put(self, tag):
		"""
		Update intent
		---
		tags:
			- Intent
		parameters:
			- in: path
			  name: tag
			  type: string
			  required: true
			  description: The tag of the intent
			- in: path
			  name: description
			  type: string
			  required: true
			  description: The description of the intent
			- in: body
			  name: patterns
			  type: array
			  required: false
			  description: The patterns of the intent
			- in: body
			  name: responses
			  type: array
			  required: false
			  description: The responses of the intent
		definitions:
			Intent:
				type: object
				properties:
					tag:
						type: string
						description: The intent tag
					description:
						type: string
						description: The intent description
					patterns:
						type: array
						items:
							$ref: '#/definitions/Pattern'
					responses:
						type: array
						items:
							$ref: '#/definitions/Response' 
			Pattern:
				type: object
				properties:
					pattern_text:
						type: string
						description: The pattern text
			Response:
				type: object
				properties:
					response_text:
						type: string
						description: The response text
		responses:
			200:
				description: The intent
				schema:
					id: Intent
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
						data:
							$ref: '#/definitions/Intent'
				examples:
					application/json: {
						"status": "success",
						"message": "Intent updated successfully.",
						"data": {
							"id": 1,
							"tag": "greeting",
							"description": "Greeting intent",
							"patterns": [
								{
									"id": 1,
									"pattern_text": "Hi",
									"intent_id": 1
								},
								{
									"id": 2,
									"pattern_text": "Hello",
									"intent_id": 1
								}
							],
							"responses": [
								{
									"id": 1,
									"response_text": "Hello, how are you?",
									"intent_id": 1
								},
								{
									"id": 2,
									"response_text": "Good to see you again.",
									"intent_id": 1
								}
							]
						}
					}
			400:
				description: The intent already exists
				schema:
					id: IntentAlreadyExists
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
				examples:
					application/json: {
						"status": "error",
						"message": "An intent with tag 'greeting' already exists."
					}
			500:
				description: An error occurred while updating the intent
				schema:
					id: IntentUpdateError
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
				examples:
					application/json: {
						"status": "error",
						"message": "An error occurred while updating the intent."
					}
			404:
				description: The intent not found
				schema:
					id: IntentNotFound	
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
				examples:
					application/json: {
						"status": "error",
						"message": "Intent not found."
					}
		"""
		data = IntentResource.parser.parse_args()
		patterns = data.pop("patterns")
		responses = data.pop("responses")
		intent = Intent.find_by_tag(tag)
		
		if intent is None:
			intent = Intent(tag, **data)
		else:
			intent.description = data["description"]
			
			# Xóa các pattern cũ
			for pattern in intent.patterns:
				pattern.delete_from_db()

			# Xóa các response cũ
			for response in intent.responses:
				response.delete_from_db()
		try:
			intent.save_to_db()

			# Lưu patterns
			for pattern in patterns:
				pattern = Pattern(pattern, intent.id)
				pattern.save_to_db()

			# Lưu responses
			for response in responses:
				response = Response(response, intent.id)
				response.save_to_db()
		except:
			return CommonResponse(status="error", message="An error occurred while updating the intent.").json(), 500

		return CommonResponse(status="success", message="Intent updated successfully.", data=intent.json()).json(), 200
	
class IntentListResource(Resource):
	def get(self):
		"""
		Get all intents
		---
		tags:
			- Intent
		responses:
			200:
				description: The intents
				schema:
					id: Intents
					type: object
					properties:
						status:
							type: string
							description: The status of the response
						message:
							type: string
							description: The message of the response
						data:
							type: array
							items:
								$ref: '#/definitions/Intent'
				examples:
					application/json: {
						"status": "success",
						"message": "Intents found.",
						"data": [
							{
								"id": 1,
								"tag": "greeting",
								"description": "Greeting intent",
								"patterns": [
									{
										"id": 1,
										"pattern_text": "Hi",
										"intent_id": 1
									},
									{
										"id": 2,
										"pattern_text": "Hello",
										"intent_id": 1
									}
								],
								"responses": [
									{
										"id": 1,
										"response_text": "Hello, how are you?",
										"intent_id": 1
									},
									{
										"id": 2,
										"response_text": "Good to see you again.",
										"intent_id": 1
									}
								]
							},
							{
								"id": 2,
								"tag": "goodbye",
								"description": "Goodbye intent",
								"patterns": [
									{
										"id": 3,
										"pattern_text": "Goodbye",
										"intent_id": 2
									},
									{
										"id": 4,
										"pattern_text": "Bye",
										"intent_id": 2
									}
								],
								"responses": [
									{
										"id": 3,
										"response_text": "See you later.",
										"intent_id": 2
									},
									{
										"id": 4,
										"response_text": "Have a nice day.",
										"intent_id": 2
									}
								]
							}
						]
					}
		"""
		data = [intent.json() for intent in Intent.get_all()]
		return CommonResponse(status="success", message="Intents found.", data=data).json(), 200