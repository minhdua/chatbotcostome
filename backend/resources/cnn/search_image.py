
import pdb

from resources.cnn.fashion_net import build_model, load_modelfile
from resources.cnn.image_classification import predict_attributes_and_category


def extract_features(image_path):
    model_file_path = 'ckpt_model.15-23.5125-0.9086.h5'
    # Load the model from the specified file
    model, _ = build_model()
    model = load_modelfile(model, model_file_path)
    # Perform inference on the image using the loaded model
    predictions = predict_attributes_and_category(image_path, model)
    return predictions