from enum import Enum


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
    URL = 'http://localhost:4200/shop?page=1&per_page=200&category={categories}&size={size}&color={color}'
    TAG_A = ' <a href="{url}" target="_blank" id="link_show_product">{text_user}</a>.'
    URL_IMAGE = 'http://localhost:4200/shop?page=1&per_page=200&attributes_predict={attributes}&categories_predict={categories}'


class ResponseSizes(Enum):
    SIZES = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
    

class ResponseMessage(Enum):
    NOTIFICATION = "Sản phẩm bạn tìm là"
    CLICK = "Nhấn vào xem sản phẩm"
    

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