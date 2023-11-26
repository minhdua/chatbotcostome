from flask_restful import Resource, reqparse
from models.dictionary_model import Dictionary
from models.common.response import CommonResponse

class DictionaryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("word", type=str, required=True, help="This field cannot be blank.")
    parser.add_argument("synonyms", type=list, required=True, help="This field cannot be blank.")

    def get(self, word):
        """
        Retrieve information about a specific dictionary entry by word.
        ---
        tags:
          - NLP
        parameters:
          - name: word
            in: path
            type: string
            required: true
            description: The word to search for in the dictionary
        responses:
          200:
            description: Dictionary found
            schema:
              id: Dictionary
              properties:
                status:
                  type: string
                  description: The status of the dictionary
                  default: success
                message:
                  type: string
                  description: The message of the dictionary
                  default: Dictionary found.
                data:
                  type: object
                  description: The dictionary data
                  default: {}
          404:
            description: Dictionary not found
            schema:
              id: Dictionary
              properties:
                status:
                  type: string
                  description: The status of the dictionary
                  default: error
                message:
                  type: string
                  description: The message of the dictionary
                  default: Dictionary not found.
        """
        dictionary = Dictionary.find_by_word(word)
        if dictionary:
            return CommonResponse.ok(message="Dictionary found.", data=dictionary.json()).json(), 200
        return CommonResponse.not_found(message="Dictionary not found.")

    def post(self):
        """
        Create a new dictionary entry.
        ---
        tags:
          - NLP
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                word:
                  type: string
                  description: The word for the new dictionary entry
                synonyms:
                  type: array
                  items:
                    type: string
                  description: The synonyms for the new dictionary entry
        responses:
          201:
            description: Dictionary created
            schema:
              id: Dictionary
              properties:
                status:
                  type: string
                  description: The status of the dictionary
                  default: success
                message:
                  type: string
                  description: The message of the dictionary
                  default: Dictionary created.
                data:
                  type: object
                  description: The dictionary data
                  default: {}
          409:
            description: Dictionary already exists
            schema:
              id: Dictionary
              properties:
                status:
                  type: string
                  description: The status of the dictionary
                  default: error
                message:
                  type: string
                  description: The message of the dictionary
                  default: Dictionary already exists.
        """
        data = DictionaryResource.parser.parse_args()
        word = data["word"]
        if Dictionary.find_by_word(word):
            return CommonResponse.conflict(message=f"Dictionary with word '{word}' already exists.")

        dictionary = Dictionary(word=word, synonyms=data["synonyms"])
        dictionary.save()
        return CommonResponse.created(message="Dictionary created.", data=dictionary.json())

    def delete(self, word):
        """
        Delete a dictionary entry by word.
        ---
        tags:
          - NLP
        parameters:
          - name: word
            in: path
            type: string
            required: true
            description: The word to delete from the dictionary
        responses:
          200:
            description: Dictionary deleted
            schema:
              id: Dictionary
              properties:
                status:
                  type: string
                  description: The status of the dictionary
                  default: success
                message:
                  type: string
                  description: The message of the dictionary
                  default: Dictionary deleted.
                data:
                  type: object
                  description: The dictionary data
                  default: {}
          404:
            description: Dictionary not found
            schema:
              id: Dictionary
              properties:
                status:
                  type: string
                  description: The status of the dictionary
                  default: error
                message:
                  type: string
                  description: The message of the dictionary
                  default: Dictionary not found.
        """
        dictionary = Dictionary.find_by_word(word)
        if dictionary:
            dictionary.delete_from_db()
            return CommonResponse.ok(message="Dictionary deleted.", data=dictionary.json())
        return CommonResponse.not_found(message="Dictionary not found.")

    def put(self, word):
        """
        Update a dictionary entry by word.
        ---
        tags:
          - NLP
        parameters:
          - name: word
            in: path
            type: string
            required: true
            description: The word to update in the dictionary
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                word:
                  type: string
                  description: The updated word for the dictionary entry
                synonyms:
                  type: array
                  items:
                    type: string
                  description: The updated synonyms for the dictionary entry
        responses:
          200:
            description: Dictionary updated
            schema:
              id: Dictionary
              properties:
                status:
                  type: string
                  description: The status of the dictionary
                  default: success
                message:
                  type: string
                  description: The message of the dictionary
                  default: Dictionary updated.
                data:
                  type: object
                  description: The dictionary data
                  default: {}
          404:
            description: Dictionary not found
            schema:
              id: Dictionary
              properties:
                status:
                  type: string
                  description: The status of the dictionary
                  default: error
                message:
                  type: string
                  description: The message of the dictionary
                  default: Dictionary not found.
        """
        data = DictionaryResource.parser.parse_args()
        dictionary = Dictionary.find_by_word(word)
        if dictionary:
            dictionary.word = data["word"]
            dictionary.synonyms = data["synonyms"]
            dictionary.save()
            return CommonResponse.ok(message="Dictionary updated.", data=dictionary.json())
        return CommonResponse.not_found(message="Dictionary not found.")

class DictionaryListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("dictionaries", type=list, location='json', required=True, help="This field cannot be blank.")

    def get(self):
        """
        Get a list of all dictionaries.
        ---
        tags:
          - NLP
        responses:
          200:
            description: List of dictionaries retrieved
            schema:
              id: DictionaryList
              properties:
                status:
                  type: string
                  description: The status of the request
                  default: success
                message:
                  type: string
                  description: The message of the request
                  default: Dictionaries found.
                data:
                  type: array
                  description: List of dictionaries
                  items:
                    type: object
                    $ref: '#/definitions/Dictionary'
          404:
            description: No dictionaries found
            schema:
              id: DictionaryList
              properties:
                status:
                  type: string
                  description: The status of the request
                  default: error
                message:
                  type: string
                  description: The message of the request
                  default: No dictionaries found.
                data:
                  type: array
                  description: Empty array
                  items:
                    type: object
                    default: {}
        """
        dictionaries = Dictionary.query.all()
        if dictionaries:
            return CommonResponse.ok(message="Dictionaries found.", data=[dictionary.json() for dictionary in dictionaries]).json(), 200
        return CommonResponse.not_found(message="No dictionaries found.")

    def post(self):
        """
        Create multiple new dictionary entries.
        ---
        tags:
          - NLP
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                dictionaries:
                  type: array
                  items:
                    $ref: '#/definitions/Dictionary'
        responses:
          201:
            description: Dictionaries created
            schema:
              id: DictionaryList
              properties:
                status:
                  type: string
                  description: The status of the request
                  default: success
                message:
                  type: string
                  description: The message of the request
                  default: Dictionaries created.
                data:
                  type: array
                  description: List of created dictionaries
                  items:
                    type: object
                    $ref: '#/definitions/Dictionary'
          409:
            description: One or more dictionaries already exist
            schema:
              id: DictionaryList
              properties:
                status:
                  type: string
                  description: The status of the request
                  default: error
                message:
                  type: string
                  description: The message of the request
                  default: One or more dictionaries already exist.
                data:
                  type: array
                  description: List of dictionaries that already exist
                  items:
                    type: object
                    $ref: '#/definitions/Dictionary'

        definitions:
            Dictionary:
                type: object
                properties:
                    word:
                        type: string
                        description: The word of the dictionary
                    synonyms:
                        type: array
                        items:
                            type: string
                            description: The synonyms of the dictionary
        """
        data = DictionaryListResource.parser.parse_args()
        dictionaries_data = data.get("dictionaries", [])

        created_dictionaries = []
        conflicting_dictionaries = []

        for dictionary_data in dictionaries_data:
            word = dictionary_data.get("word")
            if Dictionary.find_by_word(word):
                conflicting_dictionaries.append({"word": word, "message": f"Dictionary with word '{word}' already exists."})
            else:
                dictionary = Dictionary(word=word, synonyms=dictionary_data.get("synonyms", []))
                dictionary.save()
                created_dictionaries.append(dictionary.json())

        if created_dictionaries:
            return CommonResponse.created(message="Dictionaries created.", data=created_dictionaries).json(), 201
        elif conflicting_dictionaries:
            return CommonResponse.conflict(message="One or more dictionaries already exist.", data=conflicting_dictionaries).json(), 409
        else:
            return CommonResponse.not_found(message="No dictionaries provided for creation.").json()