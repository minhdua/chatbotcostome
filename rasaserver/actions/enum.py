from enum import Enum

class URL(Enum):
    API_ADD_HISTORY = 'http://127.0.0.1:5000/add_history'

class SizeEnum(Enum):
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"
    XXXL = "XXXL"
    
    
class EntityNameEnum(Enum):
    CATEGORY_TYPE = 'category_type'
    COLOR = 'color'
    SIZE = 'size'
    CATEGORY = 'category'
    PRICE = 'price'
    PRICE_FROM = 'price_from'
    PRICE_TO = 'price_to'


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


class ResponseURL(Enum):
    BASE_URL = 'http://localhost:4200/shop?page=1&per_page=200'
    URL_PRODUCT = 'http://127.0.0.1:5000/products?category={categories}'
    URL_CHECK_HAS_PRODUCT = 'http://127.0.0.1:5000/products'
    URL = 'http://localhost:4200/shop?page=1&per_page=200'
    TAG_A = ' <a href="{url}" target="_blank" id="link_show_product">{text_user}</a>.'
    URL_IMAGE = 'http://localhost:4200/shop?page=1&per_page=200&attributes_predict={attributes}&categories_predict={categories}'


class ResponseSizes(Enum):
    SIZES = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
    

class ResponseMessage(Enum):
    NOTIFICATION = "Sản phẩm bạn tìm là"
    CLICK = "Nhấn vào xem sản phẩm"
    

class ResponseMessage(Enum):
    NOTIFICATION = "Shop có sản phẩm bạn tìm là"
    NOT_PRODUCTS_START = "Hiện tại Shop không có sản phẩm bạn đang tìm là"
    NOT_PRODUCTS_END = "Vui lòng tìm kiếm thông tin sản phẩm khác ạ! Shop cảm ơn bạn"
    CLICK = "Nhấn vào xem sản phẩm"
    PRICE_FROM = "có giá"
    

class ResponseCategoryBody(Enum):
    BODY = [
        { "key": "UPPER_BODY", "text": 'áo' },
        { "key": "LOWER_BODY", "text": 'quần' },
        { "key": "FULL_BODY", "text": 'váy' },
        { "key": "FULL_BODY", "text": 'đầm' }
    ]


class ResponseColors(Enum):
    COLORS = [
        'WHITE', 'BLUE' ,'GREEN' , 'YELLOW', 'ORANGE', 'PINK', 'GREY', 'RED', 'BLACK', 'BROWN', 'PURPLE'
    ]


class ColorsText(Enum):
    COLORS = [
        {'key': 'WHITE', 'text': 'màu trắng'},
        {'key': 'BLUE', 'text': 'màu xanh'},
        {'key': 'GREEN', 'text': 'màu xanh lá'}, 
        {'key': 'PURPLE', 'text': 'màu xanh da trời'},
        {'key': 'YELLOW', 'text': 'màu vàng'}, 
        {'key': 'ORANGE', 'text': 'màu cam'}, 
        {'key': 'PINK', 'text': 'màu hồng'},
        {'key': 'GREY', 'text': 'màu xám'},
        {'key': 'RED', 'text': 'màu đỏ'}, 
        {'key': 'BLACK', 'text': 'màu đen'}, 
        {'key': 'BROWN', 'text': 'màu nâu'}
    ]