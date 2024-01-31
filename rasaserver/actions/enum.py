from enum import Enum


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


class ResponseURL(Enum):
    BASE_URL = 'http://localhost:4200/shop?page=1&per_page=200'
    URL_PRODUCT = 'http://127.0.0.1:5000/products?category={categories}'
    URL = 'http://localhost:4200/shop?page=1&per_page=200&category={categories}&size={size}&color={color}'
    TAG_A = ' <a href="{url}" target="_blank" id="link_show_product">{text_user}</a>.'
    URL_IMAGE = 'http://localhost:4200/shop?page=1&per_page=200&attributes_predict={attributes}&categories_predict={categories}'


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