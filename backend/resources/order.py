import pdb
from datetime import datetime

from flask import request
from flask_restful import Resource, reqparse
from models.common.response import CommonResponse
from models.order import Order, OrderFilter, OrderFilterByStatus
from models.order_product import OrderProduct
from models.product import Product
from resources.validators import (
    validate_email,
    validate_order_status,
    validate_phone,
    validate_products,
)


class OrderGetUpdateDeletedResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("email", type=validate_email)  # Thay đổi tên field
	parser.add_argument("phone", type=validate_phone)  # Thay đổi tên field
	parser.add_argument("address", type=str)  # Thay đổi tên field
	parser.add_argument("fullname", type=str)  # Thêm field mới
	parser.add_argument("status", type=validate_order_status)
	parser.add_argument('products', type=list, location='json')
	def get(self, order_id):
		"""
		Get order by id
		---
		tags:
			- Order
		parameters:
			- in: path
			  name: order_id
			  type: integer
			  required: true
			  description: The order id
		responses:
			200:
				description: The order data
				schema:
					$ref: '#/definitions/Order'
			404:
				description: The order was not found
		"""
		order = Order.find_by_id(order_id)
		if order:
			return CommonResponse.ok("Order found", order.json())
		return CommonResponse.not_found("Order not found")
    
	def put(self, order_id):
		"""
		Update order by id
		---
		tags:
			- Order
		parameters:
			- in: path
			  name: order_id
			  type: integer
			  required: true
			  description: The order id
			- in: body
			  name: body
			  schema:
				$ref: '#/definitions/Order'
			  example:
				application/json:
					email: "customer@example.com"
					phone: "0123456789"
					address: "123 Nguyen Van Linh"
					fullname: "Nguyen Van A"
					status: "pending"
					products:
						- product_id: 1
						  order_size: "S"
						  order_color: "Black"
						  quantity: 1
						- product_id: 2
						  order_size: "M"
						  order_color: "White"
						  quantity: 2
		responses:
			200:
				description: The order data
				schema:
					$ref: '#/definitions/Order'
			400:
				description: The order was not updated due to invalid data
			404:
				description: The order was not found
		definitions:
			Order:
				type: object
				properties:
					email:
						type: string
					phone:
						type: string	
					address:
						type: string
					fullname:
						type: string
					status:
						type: string
					products:
						type: array
						items:
							type: object
							properties:
								product_id:
									type: integer
								order_size:
									type: 
										$ref: '#/definitions/Size'
								order_color:
									type: 
										$ref: '#/definitions/Color'
								quantity:
									type: integer
				Sizes:
					type: string
					enum:
						- S
						- M
						- L
						- XL
				Colors:
					type: string
					enum:
						- Black
						- White
						- Red
						- Blue
						- Yellow
						- Green

		"""
		order = Order.find_by_id(order_id)
		if order:
			data = self.parser.parse_args()
			products_data = data.pop("products")
			
			# Tính toán lại tổng giá trị đơn hàng dựa trên sản phẩm mới
			total_price = 0
			products = []
			if products_data:
				for product_data in products_data:
					product = Product.find_by_id(product_data["product_id"])
					product_order = validate_products(product_data)
					# check size and color has in product
					if product_order["order_size"] not in [s.size.value for s in product.sizes]:
						raise ValueError("Invalid order_size")
					if product_order["order_color"] not in [c.color.value for c in product.colors]:
						raise ValueError("Invalid order_color")
					total_price += product_data["quantity"] * product.price
					products.append(product_order)
				order.update_to_db(**data,total_price=total_price,products=products)
			else:
				order.update_to_db(**data)
			# Cập nhật thông tin đơn hàng và lưu lại
			return CommonResponse.ok("Order updated successfully", data=order.json())
		return CommonResponse.not_found("Order not found")
    
	# def delete(self, order_id):
	# 	"""
	# 	Delete order by id
	# 	---
	# 	tags:
	# 		- Order
	# 	parameters:
	# 		- in: path
	# 		  name: order_id
	# 		  type: integer
	# 		  required: true
	# 		  description: The order id
	# 	responses:
	# 		200:
	# 			description: The order data
	# 			schema:
	# 				$ref: '#/definitions/Order'
	# 		404:
	# 			description: The order was not found
	# 	"""
	# 	order = Order.query.get(order_id)
	# 	if order:
	# 		order.delete()
	# 		return CommonResponse.ok("Order deleted successfully", data=order.json())
	# 	return CommonResponse.not_found("Order not found")
    
class OrderListCreateResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("email", type=validate_email, required=True, help="This field cannot be blank.")  # Thay đổi tên field
	parser.add_argument("phone", type=validate_phone, required=True, help="This field cannot be blank.")  # Thay đổi tên field
	parser.add_argument("address", type=str, required=True, help="This field cannot be blank.")  # Thay đổi tên field
	parser.add_argument("fullname", type=str, required=True, help="This field cannot be blank.")  # Thêm field mới
	parser.add_argument("status", type=validate_order_status, required=True, help="This field cannot be blank.")
	# parser.add_argument("products", type=validate_products, required=True, help="This field cannot be blank.")
	parser.add_argument('products', type=list, location='json', default=[])
	def get(self):
		"""
		Get all orders
		---
		tags:
			- Order
		parameters:
			- in: query
			  name: page
			  type: integer
			  required: false
			  description: The page number
			- in: query
			  name: per_page
			  type: integer
			  required: false
			  description: The number of items per page
			- in: query
			  name: status
			  type: string
			  required: false
			  description: The order status
			  enum:
				- Pending
				- Confirmed
				- Shipping
				- Delivered
				- Cancelled
		responses:
			200:
				description: The order data
				schema:
					$ref: '#/definitions/Order'
		"""
		status_filter = request.args.get("status")

		orders = Order.query.all()

		status_stragegy = OrderFilterByStatus(status_filter)
		order_filter = OrderFilter(orders, status_stragegy)
		orders = order_filter.filter()

		total = len(orders)
		start_index = request.args.get("page", 1, type=int)
		per_page = request.args.get("per_page", 10, type=int)
		orders_pagination = [order.json() for order in orders[(start_index - 1) * per_page:start_index * per_page]]
		return CommonResponse.ok("Orders found", orders_pagination, total, start_index, per_page)

	def post(self):
		"""
		Create new order
		---
		tags:
			- Order
		parameters:
			- in: body
			  name: body
			  schema:
				$ref: '#/definitions/Order'
			  examples:
				application/json:
					email: "custome@example.com"
					phone: "0123456789"
					address: "123 Nguyen Van Linh"
					fullname: "Nguyen Van A"
					status: "pending"
					products:
						- product_id: 1
						  order_size: "S"
						  order_color: "Black"
						  quantity: 1
						- product_id: 2
						  order_size: "M"
						  order_color: "White"
						  quantity: 2
		responses:
			200:
				description: The order data
				schema:
					$ref: '#/definitions/Order'
			400:
				description: The order was not created due to invalid data

		definitions:
			Order:
				type: object
				properties:
					email:
						type: string
					phone:
						type: string	
					address:
						type: string
					fullname:
						type: string
					status:
						type: string
					products:
						type: array
						items:
							type: object
							properties:
								product_id:
									type: integer
								order_size:
									type: string
								order_color:
									type: string
								quantity:
									type: integer
		"""
		data = self.parser.parse_args()
		products_data = data.pop("products")
		total_price = 0
		products = []
		for product_data in products_data:
			product = Product.find_by_id(product_data["product_id"])
			product_order = validate_products(product_data)
			if product_order["order_size"].value not in [s.size.value for s in product.sizes]:
						return CommonResponse.bad_request("Invalid order_size")
			if product_order["order_color"].value not in [c.color.value for c in product.colors]:
				return CommonResponse.bad_request("Invalid order_color")
			# check quantity
			if product_order["quantity"] > product.quantity:
				return CommonResponse.bad_request("Invalid quantity")
			total_price += product_data["quantity"] * product.price
			products.append(product_order)

		order = Order(**data,order_date=datetime.now(),total_price=total_price,products=products)
		order.save_to_db()
		# Cập nhật quantity của sản phẩm
		for product_data in products_data:
			product = Product.find_by_id(product_data["product_id"])
			product.update_to_db(quantity=product.quantity - product_data["quantity"])
		return CommonResponse.created("Order created successfully", data=order.json())