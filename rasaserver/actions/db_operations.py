import re
import requests
import nltk
from .enum import ResponseSizes, ResponseURL
from .db_config import cursor
from .utils import check_uppercase_in_array, compare_array_source_array_dest, normalize_text

def get_categories(categories):
    query = f"SELECT * FROM category WHERE category_name IN ({', '.join(map(str, categories))})"
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def find_word(words):
    data = []
    query = f"SELECT * FROM dictionaries"
    cursor.execute(query)
    dictionaries = cursor.fetchall()

    for dictionary in dictionaries:
        synonyms_array = [normalize_text(synonyms) for synonyms in dictionary[2]]
        if normalize_text(words) in synonyms_array:
            data.append(dictionary[1])
    return data


def get_color_user_say(word):
    colors = []
    words = find_word(word)
    if len(words) > 0 and check_uppercase_in_array(words).any() == True:
        colors += words
    return colors


def get_size_user_say(user_say):
    tokens = nltk.word_tokenize(user_say)
    size_enum = ResponseSizes.SIZES.value
    sizes = []
    for token in tokens:
        for i in range(len(size_enum)):
            if re.search(token.upper(), size_enum[i]):
                sizes.append(token)
    return sizes


def get_categories_full_by_body(category_type_clothing):
    body = [
        { "key": "UPPER_BODY", "text": 'áo' },
        { "key": "LOWER_BODY", "text": 'quần' },
        { "key": "FULL_BODY", "text": 'váy' },
        { "key": "FULL_BODY", "text": 'đầm' }
    ]
    find_body = filter_bodys(category_type_clothing, body)
    if find_body == None:
        return []
    
    query = f"SELECT * FROM category WHERE category_type = '{find_body}'"
    cursor.execute(query)
    categories = cursor.fetchall()
    
    category_names = [str(category[1]) for category in categories]
    return category_names
        
def query_dictionary_by_word(words):
    categories = []
    
    categories_body = get_categories_full_by_body(words)
    if len(categories_body) > 0:
        categories += categories_body
    
    query = f"SELECT * FROM dictionaries"
    cursor.execute(query)
    dictionaries = cursor.fetchall()
    
    for dictionary in dictionaries:
        synonyms_array = [normalize_text(synonyms) for synonyms in dictionary[2]]
        if normalize_text(words) in synonyms_array:
            categories.append(dictionary[1])
    return categories
        

def filter_bodys(text_val, bodys):
    for body in bodys:
        if normalize_text(text_val) == normalize_text(body['text']):
            return body['key']
        

# Lấy size từ người dùng chat 
def check_product_has_sizes_colors_with_categories(categories, sizes, colors):
    category_id_str = ','.join([str(category.id) for category in categories])
    url_product = ResponseURL.URL_PRODUCT.value.format(categories=category_id_str)
    response = requests.get(url_product).json()
    category_ids = []
    
    # Kiểm tra sản phẩm có size, color thuộc catagory
    for product in response['data']:
        size_pro = [size.lower() for size in product['sizes']]
        size_user = [size.lower() for size in sizes]
        color_pro = [color.lower() for color in product['colors']]
        color_user = [color.lower() for color in colors]
        is_size = compare_array_source_array_dest(size_user, size_pro)
        is_color = compare_array_source_array_dest(color_user, color_pro)
        if (is_size == True or is_color == True):
            category_ids.append(product['category_id'])
            
    category_name_filtered = []
    if len(category_ids) > 0:
        for category in categories:
            if category.id in category_ids:
                category_name_filtered.append(category.category_name)
    
    return category_name_filtered