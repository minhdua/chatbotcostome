from enum import Enum


def serialize_enum(enum_value):
    return enum_value.value
        # Add other attributes you want to include in the serialization
    
def serialize_enum_list(enum_list):
    result = [serialize_enum(e) for e in enum_list]
    return sorted(result)

class SizeEnum(Enum):
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"
    XXXL = "XXXL"


class ColorEnum(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    YELLOW = "Yellow"
    BLACK = "Black"
    WHITE = "White"
    GREY = "Grey"
    PINK = "Pink"
    PURPLE = "Purple"
    BROWN = "Brown"
    ORANGE = "Orange"
    OTHERS = "Others"

class OrderStatusEnum(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    SHIPPING = "Shipping"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

class CategoryTypeEnum(Enum):
    UPPER_BODY = "Upper Body"
    LOWER_BODY = "Lower Body"
    FULL_BODY = "Full Body"
    ACCESSORIES = "Accessories"
    FOOTWEAR = "Footwear"
    OTHERS = "Others"

class GenderEnum(Enum):
    MEN = 1
    WOMEN = 0
class MessageType(Enum):
    TEXT = "text"
    IMAGE = "image"
    
class ResponseURL(Enum):
    URL_PRODUCT = 'http://127.0.0.1:5000/products?category={categories}'
    URL = 'http://localhost:4200/shop?page=1&per_page=200&category='
    TAG_A = ' <a href="{url}" target="_blank" id="link_show_product">{text_user}</a>.'
    URL_IMAGE = 'http://localhost:4200/shop?page=1&per_page=200&attributes_predict={attributes}&categories_predict={categories}'
    
class EnumValueLabel:
    def __init__(self, value, label):
        self.value = value
        self.label = label

    def json(self):
        return {'value': self.value, 'label': self.label}
    

class Perspective(Enum):
    FRONT = EnumValueLabel('1_front', "Góc nhìn phía trước")
    SIDE = EnumValueLabel('2_side', "Góc nhìn bên")
    BACK = EnumValueLabel('3_back', "Góc nhìn phía sau")
    FULL = EnumValueLabel('4_full', "Góc nhìn toàn thân")
    PARTIAL = EnumValueLabel('5_partial', "Góc nhìn một phần")
    FAT = EnumValueLabel('6_fat', "Góc nhìn béo")
    ADDITIONAL = EnumValueLabel('7_additional', "Góc nhìn bổ sung")

    def from_value(value):
        for item in Perspective:
            if item.value == value:
                return item
        return None
    

class Gender(Enum):
    WOMEN = EnumValueLabel(-1, "Nữ")
    MEN = EnumValueLabel(1, "Nam")
    UNISEX = EnumValueLabel(0, "Unisex")

    def from_value(value):
        for item in Gender:
            if item.value == value:
                return item
        return None
    
class LandMarkStatus(Enum):
    DISPLAYED = EnumValueLabel(0, "Điểm đánh dấu hiển thị")
    HIDDEN = EnumValueLabel(1, "Điểm đánh dấu ẩn/khuất")
    CUT = EnumValueLabel(2, "Điểm đánh dấu cắt/bị cắt")

    def from_value(value):
        for item in LandMarkStatus:
            if item.value == value:
                return item
        return None

class ClothingParts(Enum):
    LEFT_COLLAR = EnumValueLabel(1, "Cổ áo trái")
    RIGHT_COLLAR = EnumValueLabel(2, "Cổ áo phải")
    LEFT_SLEEVE = EnumValueLabel(3, "Tay áo trái")
    RIGHT_SLEEVE = EnumValueLabel(4, "Tay áo phải")
    LEFT_WAIST = EnumValueLabel(5, "Đường eo trái")
    RIGHT_WAIST = EnumValueLabel(6, "Đường eo phải")
    LEFT_HEM = EnumValueLabel(7, "Gấu áo trái")
    RIGHT_HEM = EnumValueLabel(8, "Gấu áo phải")

    def from_value(value):
        for item in ClothingParts:
            if item.value == value:
                return item
        return None

class EvaluationStatus(Enum):
    TRAIN = EnumValueLabel(0, "Dữ liệu huấn luyện")
    TEST = EnumValueLabel(1, "Dữ liệu kiểm tra")
    VALIDATION = EnumValueLabel(2, "Dữ liệu đánh giá")

    def from_value(value):
        for item in EvaluationStatus:
            if item.value == value:
                return item
        return None

class ResponseMessage(Enum):
    MESSAGE01 = 'Tôi xin lỗi, tôi không hiểu ý bạn. Bạn có thể diễn đạt lại câu hỏi của mình không?'
    MESSAGE02 = 'Tôi xin lỗi, tôi không thể tìm thấy bất kỳ thông tin nào về điều đó.'
    MESSAGE_SORRY = 'Tôi xin lỗi'
    BODY_TYPE = 'Đây là các sản phẩm bạn muốn tìm {body_type}'
    MESSAGE_RESPONSE = 'Nhấn vào đây để xem'
    MESSAGE_NOTFOUND = 'Sản phẩm này hiện tại chưa kinh doanh. Vui lòng chọn sản phẩm khác!'
    MESSAGE_PRO_NOTFOUND = 'Hiện tại Shop không tìm thấy sản phẩm với thông tin trên. Vui lòng tìm sản phẩm với thông tin khác!'

class ResponseSizes(Enum):
    SIZES = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
    
class ResponseCategoryBody(Enum):
    BODY = [
        { "key": "UPPER_BODY", "text": 'ao' },
        { "key": "LOWER_BODY", "text": 'quan' },
        { "key": "FULL_BODY", "text": 'vay' },
        { "key": "FULL_BODY", "text": 'đam' },
    ]

class ResponseColors(Enum):
    COLORS = [
        'WHITE', 'BLUE' ,'GREEN' , 'YELLOW', 'ORANGE', 'PINK', 'GREY', 'RED', 'BLACK', 'BROWN', 'PURPLE'
    ]