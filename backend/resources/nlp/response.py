from app_factory import swagger
from flask_restful import Resource, reqparse
from models.common.response import CommonResponse
from models.nlp.response_model import Response


class ResponseResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("response_text", type=str, required=True, help="This field cannot be blank.")
	parser.add_argument("intent_id", type=int, required=True, help="This field cannot be blank.")

	def get(self, response_text):
		"""
		Find a response by its text.
		---
		tags:
			- Response
		parameters:
		  - name: response_text
		    in: path
		    type: string
		    required: true
		    description: The response text
		responses:
		  200:
		    description: Response found
		    schema:
		      id: Response
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: success
		        message:
		          type: string
		          description: The message of the response
		          default: Response found.
		        data:
		          type: object
		          description: The response data
		          default: {}
		  404:
		    description: Response not found
		    schema:
		      id: Response
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: error
		        message:
		          type: string
		          description: The message of the response
		          default: Response not found.
		"""
		response = Response.find_by_response_text(response_text)
		if response:
			return CommonResponse(status="success", message="Response found.", data=response.json()).json(), 200
		return CommonResponse(status="error", message="Response not found.").json(), 404
	
	def post(self, response_text):
		"""
		Create a new response.
		---
		tags:
			- Response
		parameters:
		  - name: response_text
		    in: path
		    type: string
		    required: true
		    description: The response text
		responses:
		  200:
		    description: Response created
		    schema:
		      id: Response
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: success
		        message:
		          type: string
		          description: The message of the response
		          default: Response created.
		        data:
		          type: object
		          description: The response data
		          default: {}
		  400:
		    description: Response already exists
		    schema:
		      id: Response
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: error
		        message:
		          type: string
		          description: The message of the response
		          default: Response already exists.
		"""
		data = ResponseResource.parser.parse_args()
		if Response.find_by_response_text(data["response_text"]):
			return CommonResponse(status="error", message="Response already exists.").json(), 400
		response = Response(**data)
		response.save_to_db()
		return CommonResponse(status="success", message="Response created.", data=response.json()).json(), 200
	
	def put(self, response_text):
		"""
		Update a response.
		---
		tags:
			- Response
		parameters:
		  - name: response_text
		    in: path
		    type: string
		    required: true
		    description: The response text
		responses:
		  200:
		    description: Response updated
		    schema:
		      id: Response
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: success
		        message:
		          type: string
		          description: The message of the response
		          default: Response updated.
		        data:
		          type: object
		          description: The response data
		          default: {}
		  400:
		    description: Response already exists
		    schema:
		      id: Response
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: error
		        message:
		          type: string
		          description: The message of the response
		          default: Response already exists.
		"""
		data = ResponseResource.parser.parse_args()
		response = Response.find_by_response_text(response_text)
		if response:
			response.response_text = data["response_text"]
			response.intent_id = data["intent_id"]
		else:
			response = Response(**data)
		response.save_to_db()
		return CommonResponse(status="success", message="Response updated.", data=response.json()).json(), 200
	
	def delete(self, response_text):
		"""
		Delete a response.
		---
		tags:
			- Response
		parameters:
		  - name: response_text
		    in: path
		    type: string
		    required: true
		    description: The response text
		responses:
		  200:
		    description: Response deleted
		    schema:
		      id: Response
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: success
		        message:
		          type: string
		          description: The message of the response
		          default: Response deleted.
		        data:
		          type: object
		          description: The response data
		          default: {}
		  404:
		    description: Response not found
		    schema:
		      id: Response
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: error
		        message:
		          type: string
		          description: The message of the response
		          default: Response not found.
		"""
		response = Response.find_by_response_text(response_text)
		if response:
			response.delete_from_db()
			return CommonResponse(status="success", message="Response deleted.", data=response.json()).json(), 200
		return CommonResponse(status="error", message="Response not found.").json(), 404
	
class ResponseListResource(Resource):
	
	def get(self):
		"""
		Get all responses.
		---
		tags:
			- Response
		responses:
			200:
			description: Responses found
			schema:
				id: Response
				properties:
				status:
					type: string
					description: The status of the response
					default: success
				message:
					type: string
					description: The message of the response
					default: Responses found.
				data:
					type: object
					description: The responses data
					default: {}
			404:
			description: Responses not found
			schema:
				id: Response
				properties:
				status:
					type: string
					description: The status of the response
					default: error
				message:
					type: string
					description: The message of the response
					default: Responses not found.
		"""
		responses = [response.json() for response in Response.query.all()]
		if responses:
			return CommonResponse(status="success", message="Responses found.", data=responses).json(), 200
		return CommonResponse(status="error", message="Responses not found.").json(), 404