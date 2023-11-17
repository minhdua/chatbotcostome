from db import db
from models.base_mixin import BaseMixin


class Dictionary(db.Model, BaseMixin):
    __tablename__ = "dictionaries"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word = db.Column(db.String(255), nullable=False, name="word")
    synonyms = db.Column(db.Text, nullable=False, name="synonyms")

    def __init__(self, word, synonyms):
        self.word = word
        self.synonyms = synonyms

    def __repr__(self):
        return f"Dictionaries({self.id}, {self.word}, {self.synonyms})"

    def json(self): 
        return {"id": self.id, "word": self.word, "synonyms": self.synonyms}
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_word(cls, word):
        return cls.query.filter_by(word=word).first()