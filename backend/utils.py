import json


class FileUtil:
    def load_data_json(file_path):
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data
        
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

DEFAULT_PRODUCT_IMAGE_URL = "products/no_image.png"
CNN_MODEL_NAME = 'cnn_model_name'
ATTRIBUTE_THRESHOLD = 'attribute_threshold'
IMAGE_SEARCH_MODE = 'image_search_mode'
NUMBER_OF_PRODUCT_RETURN = 'number_of_images'
MODEL_FOLDER_PATH = "backend/resources/cnn/models/vectors/"
VECTOR_FILE = "vectors.pkl"
PATH_FILE = "paths.pkl"

def if_not_none(value, default):
        if value is None:
            return default
        return value
    

# Load data file json
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