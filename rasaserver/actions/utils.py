import re
import unicodedata
from collections import OrderedDict

def get_slots(slots):
    entity_values = []
    for slot in slots:
        if slot['event'] == 'slot':
            entity_values.append(slot)
    return entity_values


def filter_duplicate_in_array(array):
  unique_values = []
  for value in array:
    if value not in unique_values:
      unique_values.append(value)
  return unique_values


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


def get_entity_value(entities, text):
    entity_values = []
    for entitie in entities:
        start = entitie['start']
        end = entitie['end']
        if entitie['entity'] == 'price':
            entity_values.append({"entity":entitie['role'], "value":text[start:end]})
        else:
            entity_values.append({"entity":entitie['entity'], "value":text[start:end]})
    return entity_values