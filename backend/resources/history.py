from flask_restful import Resource, reqparse
from models.history import History
from models.common.response import CommonResponse

class HistoryListResource(Resource):
    def get(self):
        """
        Get all histories.
        ---
        tags:
            - History
        responses:
          200:
            description: Histories found
            schema:
              id: History
              properties:
                status:
                  type: string
                  description: The status of the history
                  default: success
                message:
                  type: string
                  description: The message of the history
                  default: Categories found.
                data:
                  type: object
                  description: The history data
                  default: {}
        """
        histories = History.get_all()
        return CommonResponse.ok(message="Histories found.", data=[history.json() for history in histories])


class HistoryBySessionResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("session_user", type=str, required=True, help="This field cannot be blank.")
    
    def get(self, session_user):
        """
        Get histories by session user.
        ---
        tags:
            - History
        parameters:
            - name: session_user
              in: path
              type: string
              required: true
              description: The session user
        responses:
          200:
            description: Histories found
            schema:
              id: History
              properties:
                status:
                  type: string
                  description: The status of the history
                  default: success
                message:
                  type: string
                  description: The message of the history
                  default: Categories found.
                data:
                  type: object
                  description: The history data
                  default: {}
        """
        histories = [history.json() for history in History.find_by_session(session_user)]
        return CommonResponse.ok(message="Histories found.", data=histories)