
import pdb
import pickle
from PIL import Image
from models.product_model import Product, ProductFilter, ProductFilterByCategoryPredictionAndAttributePrediction
from resources.cnn.store_vectors import get_extract_model
from models.ai_config_model import AiConfig
from models.fashionet_model import FashionNetModel
from resources.cnn.fashion_net import build_model, change_stage, load_modelfile
from resources.cnn.image_classification import predict_attributes_and_category
from utils import CNN_MODEL_NAME, MODEL_FOLDER_PATH, PATH_FILE, VECTOR_FILE

# import thu vien
import os

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import  Model

from PIL import Image
import numpy as np


def extract_features(image_path):
    model_file_path = AiConfig.find_by_name(CNN_MODEL_NAME).string_value
    fashion_model = FashionNetModel.find_by_model_file(model_file_path)
    # Load the model from the specified file
    model_file = fashion_model.model_file
    lr = fashion_model.lr
    stage = fashion_model.stage
    batch_size = fashion_model.batch_size
    model_source, model_blue = build_model()
    model = load_modelfile(model_source, model_file)
    model = change_stage(model, lr, stage)
    # Perform inference on the image using the loaded model
    predictions = predict_attributes_and_category(image_path, model)
    return predictions


def search_product_by_image(image_path, k=16):

    # Khoi tao model
    model = get_extract_model()

    # Trich dac trung anh search
    search_vector = extract_vector(model, image_path)

    # Load 4700 vector tu vectors.pkl ra bien
    vector_file = os.path.join(MODEL_FOLDER_PATH,VECTOR_FILE)
    path_file = os.path.join(MODEL_FOLDER_PATH,PATH_FILE)
    vectors = pickle.load(open(vector_file,"rb"))
    paths = pickle.load(open(path_file,"rb"))

    # Tinh khoang cach tu search_vector den tat ca cac vector
    distance = np.linalg.norm(vectors - search_vector, axis=1)

    # Sap xep va lay ra K vector co khoang cach ngan nhat
    ids = np.argsort(distance)[:k]

    # Tao oputput
    nearest_image = [(paths[id], distance[id]) for id in ids]

    # sort image desc
    sorted_image = sorted(nearest_image, key=lambda x: x[1])

    products = []
    for image_path, distance in sorted_image:
        product = Product.find_by_image_url(image_path)
        products.append(product)
    return products

def search_product_by_category_and_attribute(image_path, k=16):
    category, attributes = extract_features(image_path)
    product_strategy = ProductFilterByCategoryPredictionAndAttributePrediction(category, attributes)
    product_filter = ProductFilter(ProductFilterByCategoryPredictionAndAttributePrediction)
    products = product_filter.filter()
    return products

# Ham tien xu ly, chuyen doi hinh anh thanh tensor
def image_preprocess(img):
    img = img.resize((224,224))
    img = img.convert("RGB")
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

def extract_vector(model, image_path):
    print("Xu ly : ", image_path)
    img = Image.open(image_path)
    img_tensor = image_preprocess(img)

    # Trich dac trung
    vector = model.predict(img_tensor)[0]
    # Chuan hoa vector = chia chia L2 norm (tu google search)
    vector = vector / np.linalg.norm(vector)
    return vector

