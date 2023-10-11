
from app_factory import swagger
from flask_restful import Resource, reqparse
from models.base_mixin import CommonResponse
from models.nlp.pattern_model import Pattern


class PatternResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("pattern_text", type=str, required=True, help="This field cannot be blank.")
	parser.add_argument("intent_id", type=int, required=True, help="This field cannot be blank.")

	def get(self, pattern_text):
		"""
		Find a pattern by its text.
		---
		tags:
		  - Pattern
		parameters:
		  - name: pattern_text
		    in: path
		    type: string
		    required: true
		    description: The pattern text
		responses:
		  200:
		    description: Pattern found
		    schema:
		      id: Pattern
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: success
		        message:
		          type: string
		          description: The message of the response
		          default: Pattern found.
		        data:
		          type: object
		          description: The pattern data
		          default: {}
		  404:
		    description: Pattern not found
		    schema:
		      id: Pattern
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: error
		        message:
		          type: string
		          description: The message of the response
		          default: Pattern not found.
		"""
		pattern = Pattern.find_by_pattern_text(pattern_text)
		if pattern:
			return CommonResponse(status="success", message="Pattern found.", data=pattern.json()).json(), 200
		return CommonResponse(status="error", message="Pattern not found.").json(), 404
	
	def post(self, pattern_text):
		"""
		Create a new pattern.
		---
		tags:
		  - Pattern
		parameters:
		  - name: pattern_text
		    in: path
		    type: string
		    required: true
		    description: The pattern text
		  - name: intent_id
		    in: formData
		    type: integer
		    required: true
		    description: The intent id
		responses:
		  201:
		    description: Pattern created
		    schema:
		      id: Pattern
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: success
		        message:
		          type: string
		          description: The message of the response
		          default: Pattern created.
		        data:
		          type: object
		          description: The pattern data
		          default: {}
		  400:
		    description: Pattern already exists
		    schema:
		      id: Pattern
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: error
		        message:
		          type: string
		          description: The message of the response
		          default: Pattern already exists.
		"""
		data = PatternResource.parser.parse_args()
		if Pattern.find_by_pattern_text(pattern_text):
			return CommonResponse(status="error", message="Pattern already exists.").json(), 400
		pattern = Pattern(pattern_text, data["intent_id"])
		pattern.save_to_db()
		return CommonResponse(status="success", message="Pattern created.", data=pattern.json()).json(), 201
	
	def put(self, pattern_text):
		"""
		Update a pattern.
		---
		tags:
		  - Pattern
		parameters:
		  - name: pattern_text
		    in: path
		    type: string
		    required: true
		    description: The pattern text
		  - name: intent_id
		    in: formData
		    type: integer
		    required: true
		    description: The intent id
		responses:
		  200:
		    description: Pattern updated
		    schema:
		      id: Pattern
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: success
		        message:
		          type: string
		          description: The message of the response
		          default: Pattern updated.
		        data:
		          type: object
		          description: The pattern data
		          default: {}
		  404:
		    description: Pattern not found
		    schema:
		      id: Pattern
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: error
		        message:
		          type: string
		          description: The message of the response
		          default: Pattern not found.
		"""
		data = PatternResource.parser.parse_args()
		pattern = Pattern.find_by_pattern_text(pattern_text)
		if pattern:
			pattern.pattern_text = data["pattern_text"]
			pattern.intent_id = data["intent_id"]
			pattern.save_to_db()
			return CommonResponse(status="success", message="Pattern updated.", data=pattern.json()).json(), 200
		return CommonResponse(status="error", message="Pattern not found.").json(), 404
	
	def delete(self, pattern_text):
		"""
		Delete a pattern.
		---
		tags:
		  - Pattern
		parameters:
		  - name: pattern_text
		    in: path
		    type: string
		    required: true
		    description: The pattern text
		responses:
		  200:
		    description: Pattern deleted
		    schema:
		      id: Pattern
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: success
		        message:
		          type: string
		          description: The message of the response
		          default: Pattern deleted.
		        data:
		          type: object
		          description: The pattern data
		          default: {}
		  404:
		    description: Pattern not found
		    schema:
		      id: Pattern
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: error
		        message:
		          type: string
		          description: The message of the response
		          default: Pattern not found.
		"""
		pattern = Pattern.find_by_pattern_text(pattern_text)
		if pattern:
			pattern.delete_from_db()
			return CommonResponse(status="success", message="Pattern deleted.", data=pattern.json()).json(), 200
		return CommonResponse(status="error", message="Pattern not found.").json(), 404
	
class PatternListResource(Resource):
	def get(self):
		"""
		Get all patterns.
		---
		tags:
		  - Pattern
		responses:
		  200:
		    description: Patterns found
		    schema:
		      id: Pattern
		      properties:
		        status:
		          type: string
		          description: The status of the response
		          default: success
		        message:
		          type: string
		          description: The message of the response
		          default: Patterns found.
		        data:
		          type: object
		          description: The pattern data
		          default: {}
		"""
		return CommonResponse(status="success", message="Patterns found.", data={"patterns": [pattern.json() for pattern in Pattern.query.all()]}).json(), 200
