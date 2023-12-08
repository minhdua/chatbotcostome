from app_factory import db
from models.dictionary_model import Dictionary
from models.base_mixin import BaseMixin
from models.product_attribute_model import ProductAttributes


class AttributePrediction(db.Model, BaseMixin):
	__tablename__ = "attribute_prediction"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(255), nullable=False)
	products = db.relationship("Product", secondary=ProductAttributes.__tablename__, lazy=True, backref=db.backref("attribute_predictions", lazy=True))
	# Các trường dữ liệu khác cho mô hình AttributePrediction

	def __init__(self, name, products=[]):
		self.name = name
		self.products = products

	def __repr__(self):
		return f"AttributePrediction({self.id}, {self.name})"
	
	def json(self):
		# product_json = [p.json() for p in self.products]
		name_other = Dictionary.find_by_word(self.name)
		return {
			"id": self.id,
			"name": self.name,
			"name_other": name_other.synonyms,
			# "products": product_json,
		}
	
	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first()
	
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

		for product in self.products:
			product_attribute = ProductAttributes(product_id=product.id, attribute_predict_id=self.id)
			product_attribute.save_to_db()

		return self
	
	def update_on_db(self, name):
		self.name = name
		db.session.commit()
		
		for product in self.products:
			product_attribute = ProductAttributes.query.filter_by(product_id=product.id, attribute_predict_id=self.id).first()
			product_attribute.update_on_db(product_id=product.id, attribute_predict_id=self.id)

