import pdb

import numpy as np
from models.attribute_prediction import AttributePrediction
from models.category_prediction import CategoryPrediction
from PIL import Image


# Define a preprocessing function
def preprocess_image(image):
    # Normalize the image pixels to the range [0, 1]
    image = image.astype(np.float32) / 255.0
    return image

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


# Predict attributes and category for a single image
def predict_attributes_and_category(image_path, model):
    # Load and preprocess the image
    img = Image.open(image_path)
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = preprocess_image(img_array)
    input_image = np.expand_dims(img_array, axis=0)

    # Use the model to predict attributes and categories for the image
    predictions = model.predict(input_image)

    # Convert the predictions to NumPy arrays
    attributes_pred = np.array(predictions[3])
    categories_pred = np.array(predictions[2])

    # Decode the predictions
    decoded_attributes = decode_attribute_predictions(attributes_pred)
    decoded_category = decode_category_predictions(categories_pred)
    return decoded_attributes, decoded_category