# # 1. In attribute type, "1" represents texture-related attributes, "2" represents fabric-related attributes, "3" represents shape-related attributes, "4" represents part-related attributes, "5" represents style-related attributes;
# from db import db
# from models.base_mixin import BaseMixin

# # from models.product import Product


# class Attribute(db.Model, BaseMixin):
#     __tablename__ = "attribute"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     attribute_name = db.Column(db.String(255), nullable=False, name="attribute_name")
#     attribute_type = db.Column(db.Integer, nullable=False, name="attribute_type")
#     # products = db.relationship("Product", secondary="product_attribute", back_populates="attributes")

#     def __init__(self, attribute_name, attribute_type):
#         self.attribute_name = attribute_name
#         self.attribute_type = attribute_type

#     def __repr__(self):
#         return f"Attribute({self.id}, {self.attribute_name}, {self.attribute_type})"

#     def json(self):
#         return {"id": self.id, "attribute_name": self.attribute_name, "attribute_type": self.attribute_type}

#     @classmethod
#     def find_by_name(cls, attribute_name):
#         return cls.query.filter_by(attribute_name=attribute_name).first()

#     @classmethod
#     def find_by_type(cls, attribute_type):
#         return cls.query.filter_by(attribute_type=attribute_type).first()
