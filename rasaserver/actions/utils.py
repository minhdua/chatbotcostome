import re
import nltk
import numpy as np
import unicodedata
from collections import OrderedDict

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


def check_uppercase_in_array(array_text):
  return np.array([string.isupper() for string in array_text])


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