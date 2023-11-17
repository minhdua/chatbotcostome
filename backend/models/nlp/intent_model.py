from app_factory import db
from models.base_mixin import BaseMixin
from models.nlp.pattern_model import Pattern
from models.nlp.response_model import Response
from sqlalchemy import update


class Intent(db.Model, BaseMixin):
    __tablename__ = "intent"  # Custom tên bảng snake_case

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(
        db.String(100), nullable=False, name="tag"
    )  # Custom tên cột snake_case
    description = db.Column(db.String(255), nullable=True, name="description")
    patterns = db.relationship("Pattern", backref="intent", lazy=True)
    responses = db.relationship("Response", backref="intent", lazy=True)

    def __init__(self, tag, description=None):
        self.tag = tag
        self.description = description

    def __repr__(self):
        return f"Intent({self.id}, {self.tag}, {self.description})"
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self, intent: dict):
        update = db.session.query(Intent).get(intent['id'])
        for key, value in intent.items():
            setattr(update, key, value)
        db.session.commit()
        db.session.flush()

    def json(self):
        return {
            "id": self.id,
            "tag": self.tag,
            "description": self.description,
            "patterns": [pattern.json() for pattern in self.patterns],
            "responses": [response.json() for response in self.responses],
        }

    @classmethod
    def find_by_tag(cls, tag):
        return cls.query.filter_by(tag=tag).first()
