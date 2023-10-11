from db import db
from models.base_mixin import BaseMixin


class ProductCategories(db.Model, BaseMixin):
    __tablename__ = "product_categories"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Các trường dữ liệu khác cho mô hình ProductCategories
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    category_predict_id = db.Column(db.Integer, db.ForeignKey("category_prediction.id"), nullable=False)
    # product = db.relationship("Product", backref="product_categories")
    # category_prediction = db.relationship("CategoryPrediction", backref="product_categories")
    def __init__(self, product_id, category_predict_id):
        self.product_id = product_id
        self.category_predict_id = category_predict_id

    def __repr__(self):
        return f"ProductCategories({self.id}, {self.product_id}, {self.category_predict_id})"
    
    def json(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "category_predict_id": self.category_predict_id,
        }

    def delete_by_product_id(product_id):
        ProductCategories.query.filter_by(product_id=product_id).delete()
        db.session.commit()
        return True
    
    def delete_by_category_predict_id(category_predict_id):
        ProductCategories.query.filter_by(category_predict_id=category_predict_id).delete()
        db.session.commit()
        return True