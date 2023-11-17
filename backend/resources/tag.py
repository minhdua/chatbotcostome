from flask_restful import Resource, reqparse
from models.common.response import CommonResponse
from models.tag import Tag


class TagResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("tag_name", type=str, required=True, help="This field cannot be blank.")

	def get(self, tag_name):
		"""
		Find a tag by its name.
		---
		tags:
			- Tag
		parameters:
		  - name: tag_name
		    in: path
		    type: string
		    required: true
		    description: The tag name
		responses:
		  200:
		    description: Tag found
		    schema:
		      id: Tag
		      properties:
		        status:
		          type: string
		          description: The status of the tag
		          default: success
		        message:
		          type: string
		          description: The message of the tag
		          default: Tag found.
		        data:
		          type: object
		          description: The tag data
		          default: {}
		  404:
		    description: Tag not found
		    schema:
		      id: Tag
		      properties:
		        status:
		          type: string
		          description: The status of the tag
		          default: error
		        message:
		          type: string
		          description: The message of the tag
		          default: Tag not found.
		"""
		tag = Tag.find_by_tag_name(tag_name)
		if tag:
			return CommonResponse(status="success", message="Tag found.", data=tag.json()).json(), 200
		return CommonResponse(status="error", message="Tag not found.").json(), 404
    
	def post(self, tag_name):
		"""
		Create a new tag.
		---
		tags:
			- Tag
		parameters:
		  - name: tag_name
		    in: path
		    type: string
		    required: true
		    description: The tag name
		responses:
		  200:
		    description: Tag created
		    schema:
		      id: Tag
		      properties:
		        status:
		          type: string
		          description: The status of the tag
		          default: success
		        message:
		          type: string
		          description: The message of the tag
		          default: Tag created.
		        data:
		          type: object
		          description: The tag data
		          default: {}
		  400:
		    description: Tag already exists
		    schema:
		      id: Tag
		      properties:
		        status:
		          type: string
		          description: The status of the tag
		          default: error
		        message:
		          type: string
		          description: The message of the tag
		          default: Tag already exists.
		"""
		tag = Tag.find_by_tag_name(tag_name)
		if tag:
			return CommonResponse(status="error", message="Tag already exists.").json(), 400
		tag = Tag(tag_name)
		tag.save_to_db()
		return CommonResponse(status="success", message="Tag created.", data=tag.json()).json(), 200
    
	def delete(self, tag_name):
		"""
		Delete a tag by its name.
		---
		tags:
			- Tag
		parameters:
		  - name: tag_name
		    in: path
		    type: string
		    required: true
		    description: The tag name
		responses:
		  200:
		    description: Tag deleted
		    schema:
		      id: Tag
		      properties:
		        status:
		          type: string
		          description: The status of the tag
		          default: success
		        message:
		          type: string
		          description: The message of the tag
		          default: Tag deleted.
		        data:
		          type: object
		          description: The tag data
		          default: {}
		  404:
		    description: Tag not found
		    schema:
		      id: Tag
		      properties:
		        status:
		          type: string
		          description: The status of the tag
		          default: error
		        message:
		          type: string
		          description: The message of the tag
		          default: Tag not found.
		"""
		tag = Tag.find_by_tag_name(tag_name)
		if tag:
			tag.delete_from_db()
			return CommonResponse(status="success", message="Tag deleted.", data=tag.json()).json(), 200
		return CommonResponse(status="error", message="Tag not found.").json(), 404
    
	def put(self, tag_name):
		"""
		Update a tag by its name.
		---
		tags:
			- Tag
		parameters:
		  - name: tag_name
		    in: path
		    type: string
		    required: true
		    description: The tag name
		  - name: tag_name
		    in: body
		    type: string
		    required: true
		    description: The tag name
		responses:
		  200:
		    description: Tag updated
		    schema:
		      id: Tag
		      properties:
		        status:
		          type: string
		          description: The status of the tag
		          default: success
		        message:
		          type: string
		          description: The message of the tag
		          default: Tag updated.
		        data:
		          type: object
		          description: The tag data
		          default: {}
		  404:
		    description: Tag not found
		    schema:
		      id: Tag
		      properties:
		        status:
		          type: string
		          description: The status of the tag
		          default: error
		        message:
		          type: string
		          description: The message of the tag
		          default: Tag not found.
		"""
		data = TagResource.parser.parse_args()
		tag = Tag.find_by_tag_name(tag_name)
		if tag:
			tag.tag_name = data["tag_name"]
			tag.save_to_db()
			return CommonResponse(status="success", message="Tag updated.", data=tag.json()).json(), 200
		return CommonResponse(status="error", message="Tag not found.").json(), 404
    
class TagListResource(Resource):
	def get(self):
		"""
		Find all tags.
		---
		tags:
			- Tag
		responses:
		  200:
		    description: Tags found
		    schema:
		      id: Tag
		      properties:
		        status:
		          type: string
		          description: The status of the tag
		          default: success
		        message:
		          type: string
		          description: The message of the tag
		          default: Tags found.
		        data:
		          type: object
		          description: The tag data
		          default: {}
		"""
		return CommonResponse(status="success", message="Tags found.", data={"tags": [tag.json() for tag in Tag.query.all()]}).json(), 200
    