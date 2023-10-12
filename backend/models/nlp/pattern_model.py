from app_factory import db
from models.base_mixin import BaseMixin


class Pattern(db.Model, BaseMixin):
    __tablename__ = "pattern"  # Custom tên bảng snake_case

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pattern_text = db.Column(
        db.String(255), nullable=False, name="pattern_text"
    )  # Custom tên cột snake_case
    intent_id = db.Column(db.Integer, db.ForeignKey("intent.id"), nullable=False)
    # intent = db.relationship("Intent", backref="patterns", lazy=True)

    def __init__(self, pattern_text, intent_id):
        self.pattern_text = pattern_text
        self.intent_id = intent_id

    def __repr__(self):
        return f"Pattern({self.id}, {self.pattern_text}, {self.intent_id})"
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self, pattern: dict):
        update = db.session.query(Pattern).get(pattern['id'])
        for key, value in pattern.items():
            setattr(update, key, value)
        db.session.commit()
        db.session.flush()

    def json(self):
        return {
            "id": self.id,
            "pattern_text": self.pattern_text,
            "intent_id": self.intent_id,
        }
