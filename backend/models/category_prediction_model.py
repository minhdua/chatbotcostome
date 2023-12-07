from app_factory import db
from models.enum import CategoryTypeEnum, GenderEnum
from models.base_mixin import BaseMixin
from models.product_category_model import ProductCategories


class CategoryPrediction(db.Model, BaseMixin):
	__tablename__ = "category_prediction"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(255), nullable=False)
	type = db.Column(db.Enum(CategoryTypeEnum), nullable=True, name="categorytypeenum")
	gender = db.Column(db.Enum('MEN', 'WOMEN', name='genderenum', create_type=True), nullable=False, server_default='MEN')
	products = db.relationship("Product", secondary=ProductCategories.__tablename__, lazy=True, backref=db.backref("category_predictions", lazy=True))
	# Các trường dữ liệu khác cho mô hình CategoryPrediction

	def __init__(self, name, products=[]):
		self.name = name
		self.products = products

	def __repr__(self):
		return f"CategoryPrediction({self.id}, {self.name})"

	def json(self):
		# product_json = [p.json() for p in self.products]
		return {
			"id": self.id,
			"name": self.name,
			# "products": product_json,
		}
	
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

		for product in self.products:
			image_category = ProductCategories(product_id=product.id, category_predict_id=self.id)
			image_category.save_to_db()

		return self
	
	def update_on_db(self, name):
		self.name = name
		db.session.commit()
		
		for product in self.products:
			image_category = ProductCategories.query.filter_by(product_id=product.id, category_predict_id=self.id).first()
			image_category.update_on_db(product_id=product.id, category_predict_id=self.id)