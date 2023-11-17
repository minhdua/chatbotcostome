from app_factory import db
from models.base_mixin import BaseMixin


class ProductTag(db.Model, BaseMixin):
	__tablename__ = 'product_tag'
	
	id = db.Column(db.Integer, primary_key=True)
	product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
	tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
	
	def __init__(self, product_id, tag_id):
		self.product_id = product_id
		self.tag_id = tag_id
	
	def __repr__(self):
		return f"ProductTag({self.id}, {self.product_id}, {self.tag_id})"
	
	def json(self):
		return {
			"id": self.id,
			"product_id": self.product_id,
			"tag_id": self.tag_id,
		}
	
	@classmethod
	def delete_by_product_id(cls, product_id):
		db.session.query(cls).filter(cls.product_id == product_id).delete()
		db.session.commit()