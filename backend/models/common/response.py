from flask import jsonify, make_response


class CommonResponse:
    def __init__(self, status, message, data=None):
        self.status = status
        self.message = message
        self.data = data

    def json(self, status_code, total=None, current_page=None, per_page=None):
        response_data = {
            "status": self.status,
            "message": self.message,
            "data": self.data
        }
        if isinstance(self.data, list):
            response_data["total"] = total
            if current_page is not None:
                response_data["current_page"] = current_page
            if per_page is not None:
                response_data["per_page"] = per_page
            
        return make_response(jsonify(response_data), status_code)

    @classmethod
    def success(cls, message, data=None, current_page=None, per_page=None):
        return cls("Success", message, data).json(200, current_page, per_page)

    @classmethod
    def bad_request(cls, message):
        return cls("Bad Request", message).json(400)

    @classmethod
    def not_found(cls, message):
        return cls("Not Found", message).json(404)

    @classmethod
    def internal_server_error(cls, message, data=None):
        return cls("Internal Server Error", message, data).json(500)
    
    @classmethod
    def conflict(cls, message):
        return cls("Conflict", message).json(409)

    @classmethod
    def created(cls, message, data=None):
        return cls("Created", message, data).json(201)

    @classmethod
    def no_content(cls, message):
        return cls("No Content", message).json(204)
    
    @classmethod
    def ok(cls, message, data=None, total=None, current_page=None, per_page=None):
        return cls("OK", message, data).json(200, total, current_page, per_page)
    
    @classmethod
    def accepted(cls, message, data=None):
        return cls("Accepted", message, data).json(202)