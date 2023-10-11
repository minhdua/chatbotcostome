from db import db
from models.base_mixin import BaseMixin


class Brand(db.Model, BaseMixin):
    __tablename__ = "brand"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String(255), nullable=False, name="brand_name")
    # products = db.relationship("Product", backref="brand", lazy=True)

    def __init__(self, brand_name):
        self.brand_name = brand_name

    def __repr__(self):
        return f"Brand({self.id}, {self.brand_name})"

    def json(self):
        return {"id": self.id, "brand_name": self.brand_name}

    def find_by_name(self, brand_name):
        return self.query.filter_by(brand_name=brand_name).first()