import re
import unicodedata
import numpy as np

def normalize_text(text):
  # Loại bỏ dấu tiếng Việt
  text = unicodedata.normalize("NFD", text)
  text = "".join([c for c in text if not unicodedata.combining(c)])

  # Loại bỏ khoảng trắng thừa và chuyển đổi thành chữ thường
  text = re.sub(r"\s+", " ", text).strip().lower()

  return text

def check_uppercase_in_array(array_text):
  return np.array([string.isupper() for string in array_text])

def filter_duplicate_in_array(array):
  unique_values = []
  for value in array:
    if value not in unique_values:
      unique_values.append(value)
  return unique_values

def compare_array_source_array_dest(array_source, array_dest):
  for value in array_source:
    if value in array_dest:
      return True
  return False

def compare_strings(text, string):
  pattern = re.compile(string)
  match = re.search(pattern, text)
  if match:
      return True
  else:
      return False