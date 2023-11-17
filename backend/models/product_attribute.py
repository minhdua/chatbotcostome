from db import db
from models.base_mixin import BaseMixin


class ProductAttributes(db.Model, BaseMixin):
    __tablename__ = "product_attributes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Các trường dữ liệu khác cho mô hình ProductAttributes
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    attribute_predict_id = db.Column(db.Integer, db.ForeignKey("attribute_prediction.id"), nullable=False)
    # product = db.relationship("Product", backref="product_attributes")
    # attribute_prediction = db.relationship("AttributePrediction", backref="product_attributes")

    def __init__(self, product_id, attribute_predict_id):
        self.product_id = product_id
        self.attribute_predict_id = attribute_predict_id

    def __repr__(self):
        return f"ProductAttributes({self.id}, {self.product_id}, {self.attribute_predict_id})"
    
    def json(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "attribute_predict_id": self.attribute_predict_id,
        }
    
    def delete_by_product_id( product_id):
        ProductAttributes.query.filter_by(product_id=product_id).delete()
        db.session.commit()
        return True
    
    def delete_by_attribute_predict_id(attribute_predict_id):
        ProductAttributes.query.filter_by(attribute_predict_id=attribute_predict_id).delete()
        db.session.commit()
        return True