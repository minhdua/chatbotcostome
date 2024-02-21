from app_factory import db
from models.base_mixin import BaseMixin


class HistoryNLU(db.Model, BaseMixin):
    __tablename__ = "history_nlu"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), nullable=False, name="user_id")
    user_say = db.Column(db.Text, nullable=False, name="user_say")
    intent = db.Column(db.String(255), nullable=False, name="intent")
    slots = db.Column(db.Text, nullable=False, name="slots")

    def __init__(self, user_id, user_say, intent, slots):
        self.user_id = user_id
        self.user_say = user_say
        self.intent = intent
        self.slots = slots

    def __repr__(self):
        return f"HistoryNLU({self.id}, {self.user_id}, {self.user_say}, {self.intent}, {self.slots})"

    def json(self): 
        return {
            "id": self.id, 
            "user_id": self.user_id, 
            "user_say": self.user_say,
            "intent": self.intent,
            "slots": self.slots
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_session(cls, session_id):
        return cls.query.filter_by(user_id=session_id).all()