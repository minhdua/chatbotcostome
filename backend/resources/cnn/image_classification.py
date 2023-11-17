import pdb

import numpy as np
from keras.preprocessing import image
from models.attribute_prediction_model import AttributePrediction
from models.category_prediction_model import CategoryPrediction
from PIL import Image
# Decode attribute predictions
def decode_attribute_predictions(predictions, threshold=0.5):

    # Truy vấn danh sách thuộc tính từ cơ sở dữ liệu
    attributes = AttributePrediction.get_all()

    # Iterate through the elements of the predictions array
    for prediction_values in predictions:
        decoded_attributes = [attribute for attribute, prediction_value in zip(attributes, prediction_values) if prediction_value >= threshold]

    return decoded_attributes

# Decode category predictions
def decode_category_predictions(predictions):
    # Load category objects
    categories = CategoryPrediction.get_all()

    # Implement decoding logic here based on your model's output format
    # If there's only one prediction, you can directly access it
    if predictions.shape[0] == 1:
        decoded_categories = [categories[np.argmax(predictions)]]
    else:
        # Handle the case where there are multiple predictions (batch size > 1)
        decoded_categories = [categories[idx] for idx in np.argmax(predictions, axis=1)]

    return decoded_categories

from keras.applications.resnet50 import preprocess_input


# Predict attributes and category for a single image
def predict_attributes_and_category(image_path, model):
     # Đọc ảnh và chuẩn hóa
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Dự đoán
    preds = model.predict(x)

    # Lấy kết quả
    cate_pred = preds[2] 
    attr_pred = preds[3]

    decoded_attrs = decode_attribute_predictions(cate_pred)
    decoded_cates = decode_category_predictions(attr_pred)

    # Trả về danh mục và các thuộc tính
    return decoded_cates, decoded_attrs