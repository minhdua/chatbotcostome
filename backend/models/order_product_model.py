from app_factory import db
from flask_admin.contrib.sqla import ModelView
from models.base_mixin import BaseMixin
from models.enum import ColorEnum, SizeEnum


class OrderProductAdminView(ModelView):
	form_columns = ['order_id', 'product_id', 'order_size', 'order_color', 'quantity']


class OrderProduct(db.Model, BaseMixin):
	__tablename__ = 'order_product'

	id = db.Column(db.Integer, primary_key=True)
	order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
	product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
	order_size = db.Column(db.Enum(SizeEnum))  # Trường size kiểu Enum
	order_color = db.Column(db.Enum(ColorEnum))  # Trường color kiểu Enum
	quantity = db.Column(db.Integer, nullable=False, default=1)
	product = db.relationship('Product', backref='order_product')
	order = db.relationship('Order', backref='order_product')

	def __init__(self, order_id, product_id, order_size, order_color, quantity=1):
		self.order_id = order_id
		self.product_id = product_id
		self.order_size = order_size
		self.order_color = order_color
		self.quantity = quantity

	def __repr__(self):
		return f"OrderProduct({self.id}, {self.order_id}, {self.product_id}, {self.order_size}, {self.order_color}, {self.quantity})"

	def json(self):
		return {
			"id": self.id,
			"order_id": self.order_id,
			"product_id": self.product_id,
			"order_size": self.order_size.value,  # Lấy giá trị của Enum
			"order_color": self.order_color.value,  # Lấy giá trị của Enum
			"quantity": self.quantity,
		}
	
	def delete_by_product_id(product_id):
		OrderProduct.query.filter_by(product_id=product_id).delete()
		db.session.commit()

	def delete_by_order_id(order_id):
		OrderProduct.query.filter_by(order_id=order_id).delete()
		db.session.commit()