import re
import requests
import nltk
from .enum import ResponseCategoryBody, ResponseSizes, ResponseURL
from .db_config import cursor
from .utils import check_uppercase_in_array, compare_array_source_array_dest, get_number_in_string, normalize_text

def get_categories(categories):
    formatted_categories = ', '.join(f"'{category}'" for category in categories)
    if formatted_categories == "":
        return []
    query = f"SELECT * FROM category WHERE category_name IN ({formatted_categories})"
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def get_dictionaries():
    query = f"SELECT * FROM dictionaries"
    cursor.execute(query)
    dictionaries = cursor.fetchall()
    return dictionaries


def find_word(words):
    data = []
    dictionaries = get_dictionaries()

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
    find_body = filter_bodys(category_type_clothing, ResponseCategoryBody.BODY.value)
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
    
    for dictionary in get_dictionaries():
        synonyms_array = [normalize_text(synonyms) for synonyms in dictionary[2]]
        if normalize_text(words) in synonyms_array:
            categories.append(dictionary[1])
    return categories
        

def filter_bodys(text_val, bodys):
    for body in bodys:
        if normalize_text(text_val) == normalize_text(body['text']):
            return body['key']
        
def get_category_ids(categories):
    category_ids_str = ','.join([str(category[0]) for category in get_categories(categories)])
    return category_ids_str
        
def get_products_with_categories(categories):
    category_id_str = ','.join([str(category[0]) for category in get_categories(categories)])
    url_product = ResponseURL.URL_PRODUCT.value.format(categories=category_id_str)
    response = requests.get(url_product).json()
    
    if len(response['data']) > 0:
        return response['data']
    return []
        

def check_product_sizes_with_categories(categories, sizes):
    category_ids = []
    category_pro_filter_sizes = []
    
    for product in get_products_with_categories(categories):
        size_pro = [size.lower() for size in product['sizes']]
        size_user = [size.lower() for size in sizes]
        is_size = compare_array_source_array_dest(size_user, size_pro)
        if (is_size == True):
            category_ids.append(product['category_id'])
    
    if len(category_ids) > 0:
        for category in get_categories(categories):
            if category[0] in category_ids:
                category_pro_filter_sizes.append(category[1])
    
    return category_pro_filter_sizes


def check_product_colors_with_categories(categories, colors):
    category_ids = []
    category_pro_filter_colors = []
    
    for product in get_products_with_categories(categories):
        color_pro = [color.lower() for color in product['colors']]
        color_user = [color.lower() for color in colors]
        is_color = compare_array_source_array_dest(color_user, color_pro)
        if (is_color == True):
            category_ids.append(product['category_id'])
    
    if len(category_ids) > 0:
        for category in get_categories(categories):
            if category[0] in category_ids:
                category_pro_filter_colors.append(category[1])
    
    return category_pro_filter_colors


def check_product_prices_with_categories(categories, price_from, price_to):
    category_ids = []
    category_pro_filter_prices = []
    
    price_from = get_number_in_string(price_from)
    price_to = get_number_in_string(price_to)
    
    for product in get_products_with_categories(categories):
        if (price_from != None and int(price_from) <= int(product['price'])):
            category_ids.append(product['category_id'])
        
        elif(price_from != None and price_to != None):
            if (int(price_from) <= int(product['price']) <= int(price_to)):
                category_ids.append(product['category_id'])
    
    if len(category_ids) > 0:
        for category in get_categories(categories):
            if category[0] in category_ids:
                category_pro_filter_prices.append(category[1])
    
    return category_pro_filter_prices