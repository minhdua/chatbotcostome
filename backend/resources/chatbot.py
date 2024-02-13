from flask_restful import Resource, reqparse
import requests
from models.enum import URL
from constants import PATH_FILE_DOMAIN, PATH_FILE_NLU, RASA_API_URL
from models.common.normalize_text import normalize_text
from models.nlp.intent_model import Intent
from models.common.response import CommonResponse

class ChatBotResponseResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("question", type=str, required=True, help="This field cannot be blank.")
    parser.add_argument("session_user", type=str, required=True, help="This field cannot be blank.")
    def post(self):
        """
        Chatbot Resource
        ---
        tags:
            - Chatbot Resource
        parameters:
            -   in: body
                name: information
                type: string
                required: true
                description: Information from user
                schema:
                    id: information
                    properties:
                        question:
                            type: string
                            description: Question from user input
                        session_user:
                            type: string
                            description: SessionId of user input
        responses:
            200:
                description: Chatbot response
                schema:
                    id: response
                    properties:
                        response:
                            type: string
                            description: Chatbot response
            400:
                description: Bad request
            500:
                description: Internal server error
        """
        data = self.parser.parse_args()
        user_message = data['question']
        session_user = data['session_user']
        
        if not user_message:
            return CommonResponse.bad_request("Message is required")
    
        rasa_response = requests.post(RASA_API_URL, json={"message": user_message, "session_user": session_user})
        
        try:
            rasa_response_json = rasa_response.json()
            bot_response = rasa_response_json[0]['text'] if rasa_response_json else "Dữ liệu của tôi chưa được cập nhật"
            
            payload = {
                "user_say": data['question'],
                "session_user": data['session_user'],
                "chat_response": bot_response
            }
            add_history_api(payload)
            
            return CommonResponse.chat(message="Chatbot responsed", data=bot_response)
        except ValueError:
            return CommonResponse.internal_server_error("Failed to decode JSON response from Chatbot")


class ChatBotResource(Resource):
    parser = reqparse.RequestParser()

    def post(self):
        """
        Create file nlu.yml and fill data from database.
        ---
        tags:
          - NLU
        responses:
            200:
                description: Create file
                content:
                    application/json:
                        schema: ProductSchema
        """
        intents = Intent.get_all()
        
        # Save to nlu.yml file
        nlu_content = generate_nlu_content(intents)
        write_file(nlu_content, PATH_FILE_NLU)
            
        # Save to domain.yml file
        domain_content = generate_domain_content(intents)
        write_file(domain_content, PATH_FILE_DOMAIN)

        return CommonResponse.created(message="File nlu.yml created.", data="File nlu.yml")


def generate_domain_content(intents):
    intent_list = [normalize_text(intent.tag) for intent in intents]
    text  = 'version: "3.1"\n\n'
    text += 'intents:\n'
    formatted_intents = '\n'.join(['  - ' + sentence for sentence in intent_list])
    text += '{}\n'.format(formatted_intents)
    text += 'responses:\n'
    
    for intent in intents:
        text += '  utter_{}:\n'.format(normalize_text(intent.tag))
        formatted_responses = '\n'.join(['    - text: "' + response.response_text + '"' for response in intent.responses])
        text += '{}\n'.format(formatted_responses)

    text += '\n\n'
    text += 'session_config:\n'
    text += '  session_expiration_time: 600 \n'
    text += '  carry_over_slots_to_new_session: true \n'
    
    return text


def generate_nlu_content(intents):
    text  = 'version: "3.1"\n\n'
    text += 'nlu:\n'
    
    for intent in intents:
        patterns = [pattern.pattern_text for pattern in intent.patterns]
        formatted_list = "\n".join(["    - " + sentence for sentence in patterns])
        text += '- intent: {}\n'.format(normalize_text(intent.tag))
        text += '  examples: |\n'
        text += '{}\n'.format(formatted_list)
        
    return text


def write_file(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def add_history_api(payload):
    requests.post(f"{URL.API_ADD_HISTORY.value}", json=payload)
