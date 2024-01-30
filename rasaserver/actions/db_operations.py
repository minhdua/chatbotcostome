from .db_config import cursor
from .utils import normalize_text

def get_categories(categories):
    query = f"SELECT * FROM category WHERE category_name IN ({', '.join(map(str, categories))})"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

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