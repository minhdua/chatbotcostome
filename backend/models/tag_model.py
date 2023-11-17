from app_factory import db
from models.base_mixin import BaseMixin
from models.product_tag_model import ProductTag


class Tag(db.Model, BaseMixin):
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(255), nullable=False, name="tag_name")
    products = db.relationship(
        "Product",
        secondary=ProductTag.__tablename__,
        lazy="subquery",
        backref=db.backref("associated_tags", lazy=True),  
       
    )

    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __repr__(self):
        return f"Tag({self.id}, {self.tag_name})"

    def json(self):
        return {"id": self.id, "tag_name": self.tag_name}
    
    @classmethod
    def find_by_name(cls, tag_name):
        return cls.query.filter_by(tag_name=tag_name).first()
