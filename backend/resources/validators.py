import pdb
import re

from models.category_model import Category
from models.enum import ColorEnum, OrderStatusEnum, SizeEnum


def validate_email(value):
    # Thực hiện kiểm tra email ở đây, ví dụ: sử dụng regex
    if not re.match(r'^[\w\.-]+@[\w\.-]+$', value):
        raise ValueError("Invalid email format")
    return value

def validate_phone(value):
    # Thực hiện kiểm tra số điện thoại ở đây, ví dụ: độ dài phải là 10
    if len(value) != 10:
        raise ValueError("Invalid phone number format")
    return value

def validate_address(value):
    # Thực hiện kiểm tra địa chỉ ở đây, ví dụ: không được để trống
    if not value.strip():
        raise ValueError("Address cannot be blank")

def validate_order_status(value):
    status = value.capitalize()  # Chuyển đổi chữ cái đầu thành chữ hoa, không phân biệt hoa thường
    if status not in [s.value for s in OrderStatusEnum]:
        raise ValueError("Invalid status")
    return OrderStatusEnum(status)
    
def validate_size(value):
    size = value.upper()  # Chuyển đổi thành chữ hoa để không phân biệt hoa thường
    if size not in [s.value for s in SizeEnum]:
        raise ValueError("Invalid size")
    return SizeEnum(size)

def validate_color(value):
    color = value.capitalize()  # Chuyển đổi chữ cái đầu thành chữ hoa, không phân biệt hoa thường
    if color not in [c.value for c in ColorEnum]:
        raise ValueError("Invalid color")
    return ColorEnum(color)
    
# Định nghĩa hàm kiểm tra dữ liệu đầu vào cho trường "products"
def validate_products(value):

	if not isinstance(value, dict):
		raise ValueError("Each product must be an object")

	required_fields = ["product_id", "order_size", "order_color", "quantity"]
	for field in required_fields:
		if field not in value:
			raise ValueError(f"Product is missing required field: {field}")

        # Kiểm tra kiểu dữ liệu của các trường
	if not isinstance(value["product_id"], int):
		raise ValueError("product_id must be an integer")
	if not isinstance(value["quantity"], int):
		raise ValueError("quantity must be an integer")
	return {
		"product_id": value["product_id"],
		"order_size": validate_size(value["order_size"]),
		"order_color": validate_color(value["order_color"]),
		"quantity": value["quantity"]
	}

def validate_category(value):
    # kiểu int và tồn tại
    if not isinstance(value, int):
        raise ValueError("Category must be an integer")
    
    category = Category.find_by_id(value)
    if not category:
        raise ValueError("Category not found")
    return category.id
    
def validate_product_name(value):
    # kiểu str và không rỗng nhưng có thể none
    if not isinstance(value, str):
        raise ValueError("Product name must be a string")
    if not value.strip():
        raise ValueError("Product name cannot be blank")
    return value