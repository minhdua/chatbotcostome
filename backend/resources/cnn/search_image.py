
import pdb
from PIL import Image
from models.ai_config_model import AiConfig
from models.fashionet_model import FashionNetModel
from resources.cnn.fashion_net import build_model, change_stage, load_modelfile
from resources.cnn.image_classification import predict_attributes_and_category
from utils import CNN_MODEL_NAME

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

