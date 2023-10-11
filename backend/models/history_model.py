from db import db
from models.base_mixin import BaseMixin


class History(db.Model, BaseMixin):
    __tablename__ = "histories"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_user = db.Column(db.String(255), nullable=False, name="session_user")
    user_say = db.Column(db.Text, nullable=False, name="user_say")
    chat_response = db.Column(db.Text, nullable=False, name="chat_response")
    concepts = db.Column(db.Text, nullable=False, name="concepts")
    message_type = db.Column(db.Text, nullable=False, name="message_type")

    def __init__(self, session_user, user_say, chat_response, concepts, message_type):
        self.session_user = session_user
        self.user_say = user_say
        self.chat_response = chat_response
        self.concepts = concepts
        self.message_type = message_type

    def __repr__(self):
        return f"Distories({self.id}, {self.session_user}, {self.user_say}, {self.chat_response}, {self.concepts}, {self.message_type})"

    def json(self): 
        return {
            "id": self.id, 
            "session_user": self.session_user, 
            "user_say": self.user_say,
            "chat_response": self.chat_response,
            "concepts": self.concepts,
            "message_type": self.message_type
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_session(cls, session_id):
        return cls.query.filter_by(session_user=session_id).all()