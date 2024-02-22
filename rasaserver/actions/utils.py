import json
import re
import nltk
import numpy as np
import unicodedata
from collections import OrderedDict
import requests
from .enum import URL, ColorsText
from .enum import ResponseURL

def get_slots(slots):
    entity_values = []
    for slot in slots:
        if slot['event'] == 'slot':
            entity_values.append(slot)
    return entity_values


def corpus_process(user_say):
    contents = []
    
    # Mã hóa văn bản.
    tokens = nltk.word_tokenize(user_say)
    contents += tokens

    # Tạo n-gram từ văn bản được mã hóa.
    bigrams = nltk.bigrams(tokens)
    trigrams = nltk.trigrams(tokens)

    # Đếm tần số của mỗi n-gram.
    bigram_freq = nltk.FreqDist(bigrams)
    trigram_freq = nltk.FreqDist(trigrams)

    # Xử lý nhận văn bản với bigram
    for bigram in bigram_freq.most_common():
        text_bigram = " ".join(bigram[0])
        contents.append(text_bigram)
    
    # Xử lý lấy văn bản bằng bát quái
    for trigram in trigram_freq.most_common():
        text_trigram = " ".join(trigram[0])
        contents.append(text_trigram)
    
    return contents


def filter_duplicate_in_array(array):
  unique_values = []
  for value in array:
    if value not in unique_values:
      unique_values.append(value)
  return unique_values


def get_number_in_string(str_text):
    if str_text:
        numbers = re.findall(r'\d+', str_text)
        return numbers[0]
    return str_text


def convert_text_to_url(category_ids, sizes_format, colors_format, price_min,  price_max):
    product_url = f"{ResponseURL.URL.value}"
    if category_ids != "":
        product_url += f"&category={category_ids}"
        
    if sizes_format != "":
        product_url += f"&size={sizes_format}"
        
    if colors_format != "":
        product_url += f"&color={colors_format}"
    
    if int(price_min) > 0:
        product_url += f"&price_min={price_min}"
    
    if int(price_max) > 0:
        product_url += f"&price_max={price_max}"
    return product_url


def check_products_call_api(category_ids, sizes_format, colors_format, price_min,  price_max):
    product_url = f"{ResponseURL.URL_CHECK_HAS_PRODUCT.value}"
    if category_ids != "":
        product_url += f"?category={category_ids}"
        
    if sizes_format != "":
        product_url += f"&size={sizes_format}"
        
    if colors_format != "":
        product_url += f"&color={colors_format}"
    
    if int(price_min) > 0:
        product_url += f"&price_min={price_min}"
    
    if int(price_max) > 0:
        product_url += f"&price_max={price_max}"
        
    response = requests.get(product_url).json()
    
    if len(response['data']) > 0:
        return True
    return False


def check_uppercase_in_array(array_text):
  return np.array([string.isupper() for string in array_text])


def map_color_text(colors):
    color_texts = []
    for color in colors:
        value = find_value(ColorsText.COLORS.value, color)
        color_texts.append(value)
    return color_texts


def find_value(list_of_dicts, value):
    for dictionary in list_of_dicts:
        if (dictionary['key']).strip().lower() == value.strip().lower():
            return dictionary['text']
    return ""


def add_history_api(payload):
    requests.post(f"{URL.API_ADD_HISTORY.value}", json=payload)


def compare_array_source_array_dest(array_source, array_dest):
  for value in array_source:
    if value in array_dest:
      return True
  return False


def merge_and_remove_duplicates_ordered(arr1, arr2):
    merged_array = arr1 + arr2
    unique_elements = list(OrderedDict.fromkeys(merged_array))
    return unique_elements


def normalize_text(text):
  # Loại bỏ dấu tiếng Việt
  text = unicodedata.normalize("NFD", text)
  text = "".join([c for c in text if not unicodedata.combining(c)])

  # Loại bỏ khoảng trắng thừa và chuyển đổi thành chữ thường
  text = re.sub(r"\s+", " ", text).strip().lower()

  return text


def get_confidence_max(entities):
    entities_filter = []
    for entitie in entities:
        if entitie['entity'] == 'category' and entitie['confidence_entity'] >= 0.9:
            entities_filter.append(entitie)
        
        if entitie['entity'] == 'color' and entitie['confidence_entity'] >= 0.9:
            entities_filter.append(entitie)
            
        if entitie['entity'] == 'size' and entitie['confidence_entity'] >= 0.9:
            entities_filter.append(entitie)
            
        if entitie['entity'] == 'category_type' and entitie['confidence_entity'] >= 0.9:
            entities_filter.append(entitie)
            
        if entitie['entity'] == 'price' and entitie['confidence_entity'] >= 0.9:
            entities_filter.append(entitie)
    return entities_filter


def get_entity_value(entities, value_text):
    entity_values = []
    for entitie in entities:
        start = entitie['start']
        end = entitie['end']
        entity_values.append({"entity":entitie['entity'], "value":value_text[start:end]})
    return entity_values


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(f"Error: File not found: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON data: {e}")
        return None


def find_element_nlus(data_list, value):
    for item in data_list['data']:
        if item['user_say'].strip().lower() == value.strip().lower():
            return item
    return None
