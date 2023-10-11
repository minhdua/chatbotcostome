from db import db
from models.base_mixin import BaseMixin
from models.enum import CategoryTypeEnum

# from models.product_model import Product


class Category(db.Model, BaseMixin):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(255), nullable=False, name="category_name")
    category_type = db.Column(db.Enum(CategoryTypeEnum), nullable=False, name="category_type")
    # products = db.relationship("Product", backref="category", lazy=True)

    def __init__(self, category_name, category_type):
        self.category_name = category_name
        self.category_type = category_type

    def __repr__(self):
        return f"Category({self.id}, {self.category_name}, {self.category_type})"

    def json(self): 
        return {"id": self.id, "category_name": self.category_name, "category_type": self.category_type.value}

    @classmethod
    def find_by_name(cls, category_name):
        return cls.query.filter_by(category_name=category_name).first()

    @classmethod
    def find_by_type(cls, category_type):
        return cls.query.filter_by(category_type=category_type).first()