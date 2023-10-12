from app_factory import db
from models.base_mixin import BaseMixin


class Response(db.Model, BaseMixin):
    __tablename__ = "response"  # Custom tên bảng snake_case

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    response_text = db.Column(
        db.String(255), nullable=False, name="response_text"
    )  # Custom tên cột snake_case
    intent_id = db.Column(db.Integer, db.ForeignKey("intent.id"), nullable=False)
    # intent = db.relationship("Intent", backref="responses", lazy=True)

    def __init__(self, response_text, intent_id):
        self.response_text = response_text
        self.intent_id = intent_id

    def __repr__(self):
        return f"Response({self.id}, {self.response_text}, {self.intent_id})"
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self, response: dict):
        update = db.session.query(Response).get(response['id'])
        for key, value in response.items():
            setattr(update, key, value)
        db.session.commit()
        db.session.flush()

    def json(self):
        return {
            "id": self.id,
            "response_text": self.response_text,
            "intent_id": self.intent_id,
        }
