
import pdb

from models.ai_config_model import AiConfig
from models.fashionet_model import FashionNetModel
from resources.cnn.fashion_net import build_model, change_stage, load_modelfile
from resources.cnn.image_classification import predict_attributes_and_category
from utils import CNN_MODEL_NAME


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