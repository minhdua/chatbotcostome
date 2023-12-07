import json
import os
import re

import nltk
import numpy as np
import requests
import torch
import torch.nn as nn
from app_factory import admin, api, app
from resources.dictionary import DictionaryListResource, DictionaryResource
# from chat import get_response
from config import swagger_config, swagger_template
from app_factory import db
from flasgger import Swagger
from flask import jsonify, make_response, redirect, render_template, request, send_from_directory
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS
from models.category_model import Category
from models.common.normalize_text import (
    check_uppercase_in_array,
    compare_array_source_array_dest,
    compare_strings,
    filter_duplicate_in_array,
    normalize_text,
)
from models.common.response import CommonResponse
from models.dictionary_model import Dictionary
from models.enum import (
    MessageType,
    ResponseCategoryBody,
    ResponseMessage,
    ResponseSizes,
    ResponseURL,
)
from models.history_model import History
from models.nlp.intent_model import Intent
from models.nlp.pattern_model import Pattern
from models.nlp.response_model import Response
from models.order_model import Order, OrderAdminView
from models.order_product_model import OrderProduct, OrderProductAdminView
from models.product_model import Product
from models.tag_model import Tag
from module import NeuralNet
from nltk_utils import bag_of_words, download_nltk_data, stem, tokenize
from pyvi import ViUtils
from resources.ai_config import AiConfigResource, BestCNNModelUpdateResource
from resources.category import CategoryListResource
from resources.cnn.attribute_prediction import AttributePredictionCreateListResource
from resources.cnn.category_prediction import CategoryPredictionCreateListResource
from resources.cnn.clothing_image_features import (
    CNNPredictResource,
    ClothingImageFeaturesCreateListResource,
    ClothingImageFeaturesNewIdResource,
    ClothingImageFeaturesResource,
    CNNTrainingResource,
    PreProcessingResource,
    UpdateAccuracyResource,
    UploadImageResource,
)
from resources.cnn.search_image import extract_features
from resources.history import HistoryBySessionResource, HistoryListResource
from resources.master_data import (
    ClothingPartsListResource,
    ColorResourceList,
    EvaluationStatusListResource,
    GenderListResource,
    LandMarkStatusListResource,
    OrderStatusResourceList,
    PerspectiveListResource,
    SizeResourceList,
)
from resources.order import OrderGetUpdateDeletedResource, OrderListCreateResource
from resources.product import (
    ProductCNNResource,
    ProductListCreateResource,
    ProductResource,
)
from sqlalchemy import text
from torch.utils.data import DataLoader, Dataset
from utils import allowed_file

with app.app_context():
    download_nltk_data()


CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}})

def upload_image(request):
    file = request.files['file_image']
    session_user = request.form.get('session_user')
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER']+"/uploads", filename)
        file.save(file_path)
        
        attributes, category = extract_features(file_path)
        attribute_ids = ','.join([str(attribute.id) for attribute in attributes])
        category_ids = ','.join([str(cate.id) for cate in category])
        
        product_url = ResponseURL.URL_IMAGE.value.format(attributes=attribute_ids, categories=category_ids)
        
        response_chatbot = ""
        if len(attributes) > 0 or len(category) > 0:
            response_chatbot += ResponseURL.TAG_A.value.format(url=product_url, text_user=ResponseMessage.MESSAGE_RESPONSE.value)
        else:
            response_chatbot = ResponseMessage.MESSAGE_NOTFOUND.value
        
        user_say_image_url = f"{request.host_url}static/uploads/{filename}"
        
        history = History(
            session_user=session_user,
            user_say=user_say_image_url,
            chat_response=response_chatbot,
            concepts=json.dumps([]),
            message_type=MessageType.IMAGE.value
        )
        history.save()
        
        return jsonify({
            "answer": response_chatbot
        })
    else:
    	return jsonify({
      		"message": "Các loại hình ảnh được phép là -> png, jpg, jpeg, gif",
        	"url": request.url,
            "attributes": attributes,
            "categories": category,
		})


@app.route('/')
def redirect_to_swagger():
    return redirect('/swagger')

@app.post('/predict')
def predict():
    """
    Predict
    ---
    tags:
      - predict
    """
    text = request.form.get('message')
    if (len(text) > 0):
        response = get_response(text)
        return jsonify({
            "answer": response,
            "filename_upload": "",
			"result_files": []
   		})
    
    if 'file_image' in request.files:
        return upload_image(request)

# Master api
api.add_resource(SizeResourceList, "/sizes")
api.add_resource(ColorResourceList, "/colors")
api.add_resource(OrderStatusResourceList, "/order-statuses")
api.add_resource(PerspectiveListResource, "/perspectives")
api.add_resource(GenderListResource, "/genders")
api.add_resource(LandMarkStatusListResource, "/landmark-statuses")
api.add_resource(ClothingPartsListResource, "/clothing-parts")
api.add_resource(EvaluationStatusListResource, "/evaluation-statuses")
api.add_resource(CategoryListResource, "/categories")
api.add_resource(ProductResource, "/products/<int:product_id>")
api.add_resource(ProductListCreateResource, "/products")

api.add_resource(OrderGetUpdateDeletedResource, "/orders/<int:order_id>")
api.add_resource(OrderListCreateResource, "/orders")

api.add_resource(HistoryListResource, "/histories")
api.add_resource(HistoryBySessionResource, "/history_by_session/<string:session_user>")

# CNN api
api.add_resource(ProductCNNResource, "/products_cnn")
api.add_resource(AttributePredictionCreateListResource, "/attribute_predictions")
api.add_resource(CategoryPredictionCreateListResource, "/category_predictions")
api.add_resource(ClothingImageFeaturesResource, "/clothing_image_features/<int:clothing_id>")
api.add_resource(ClothingImageFeaturesCreateListResource, "/clothing_image_features")
api.add_resource(ClothingImageFeaturesNewIdResource, "/clothing_image_features/new_item_id")
api.add_resource(CNNTrainingResource, "/training")
api.add_resource(AiConfigResource, "/ai_configs")
api.add_resource(BestCNNModelUpdateResource, "/best_cnn_model")
api.add_resource(UpdateAccuracyResource, "/update_accuracy")
api.add_resource(PreProcessingResource, "/pre_processing")
api.add_resource(CNNPredictResource, "/image_predict")
api.add_resource(UploadImageResource, "/upload_image")
# NLP
api.add_resource(DictionaryResource, "/dictionaries/<int:dictionary_id>")
api.add_resource(DictionaryListResource, "/dictionaries")

swagger = Swagger(app, config=swagger_config, template=swagger_template)
admin.add_view(ModelView(Intent, db.session))
admin.add_view(ModelView(Pattern, db.session))
admin.add_view(ModelView(Response, db.session))
admin.add_view(ModelView(Dictionary, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(OrderAdminView(Order, db.session))
admin.add_view(OrderProductAdminView(OrderProduct, db.session))
admin.add_view(ModelView(History, db.session))
admin.add_view(ModelView(Tag, db.session))


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.get('/health')
def health_check():
    response = make_response(jsonify({"status": "Healthy"}), 200)
    return response


#################################################################
# API add_dictionary                                            #
#################################################################
@app.post('/add_dictionary')
def add_dictionary():
    data = request.json
    dictionary = Dictionary(word=data["word"], synonyms=json.dumps(data["synonyms"]))
    dictionary.save()
    return {"message": "Dictionary created successfully."}
#################################################################


#################################################################
# API get_dictionaries                                          #
#################################################################
@app.get('/get_dictionaries')
def get_dictionaries():
    dictionaries = [dictionary.json() for dictionary in Dictionary.query.all()]
    return jsonify({
        'status':'Success',
        'message':'Get Dictionaries list success',
        'data': dictionaries
    }), 200
#################################################################
    

#################################################################
# API get_find_by_word                                          #
#################################################################
@app.route("/find_by_word", methods=["POST"])
def find_by_word():
    data = request.json
    categories = []
    dictionaries = Dictionary.query.all()
    
    for dictionary in dictionaries:
        synonyms_array = json.loads(dictionary.synonyms)
        if data['question'] in synonyms_array:
            categories.append(dictionary.word)
        
    return jsonify({
        'status':'Success',
        'message':'Get Categories success',
        'data': categories
    }), 200
    
def find_word(question):
    categories = []
    dictionaries = Dictionary.query.all()
    
    for dictionary in dictionaries:
        synonyms_array = [normalize_text(synonyms) for synonyms in dictionary.synonyms]
        if normalize_text(question) in synonyms_array:
            categories.append(dictionary.word)
    return categories

def filter_bodys(text_analysis, bodys):
    for text_val in text_analysis:
        for body in bodys:
            if normalize_text(text_val) == normalize_text(body['text']):
                return body['key']
#################################################################


#################################################################
# API train_chatbot                                             #
#################################################################
@app.route("/train_chatbot", methods=["GET"])
def train_chatbot():
    results = []
    all_words = []
    tags = []
    xy = []
    
    intents = Intent.query.all()
    # Lặp qua từng câu trong các mẫu ý định của chúng tôi
    for intent in intents:
        tag = intent.tag
        # Thêm vào danh sách thẻ
        tags.append(tag)
        for pattern in intent.patterns:
            print(pattern.pattern_text)
            # Mã hóa từng từ trong câu
            w = tokenize(pattern.pattern_text)
            # Thêm vào danh sách từ của chúng tôi
            all_words.extend(w)
            # Thêm vào cặp xy
            xy.append((w, tag))
        
    # Bắt nguồn và hạ thấp từng từ
    ignore_words = ['?', '.', '!']
    all_words = [stem(w) for w in all_words if w not in ignore_words]
    
    # Loại bỏ trùng lặp và sắp xếp
    all_words = sorted(set(all_words))
    tags = sorted(set(tags))
    
    print(len(xy), "patterns")
    print(len(tags), "tags:", tags)
    print(len(all_words), "unique stemmed words:", all_words)

    # Thêm vào kết quả hiển thị trả về
    results.append({"patterns": f'{len(xy)}'})
    results.append({"tags": f'({len(tags)}) {tags}'})
    results.append({"unique stemmed words": f'({len(all_words)}) {all_words}'})
    
    # Tạo dữ liệu huấn luyện
    X_train = []
    y_train = []
    for (pattern_sentence, tag) in xy:
        # X: Túi từ cho mỗi pattern_sentence
        bag = bag_of_words(pattern_sentence, all_words)
        X_train.append(bag)
        # y: PyTorch CrossEntropyLoss chỉ cần nhãn lớp, không cần một lần nóng
        label = tags.index(tag)
        y_train.append(label)
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    
    # Hyper-parameters (siêu tham số)
    num_epochs = 1000
    batch_size = 8
    learning_rate = 0.001
    input_size = len(X_train[0])
    hidden_size = 8
    output_size = len(tags)
    print(input_size, output_size)
    
    # Thêm vào kết quả hiển thị trả về
    results.append({"input_size": input_size})
    results.append({"output_size": output_size})
    
    class ChatDataset(Dataset):
        def __init__(self):
            self.n_samples = len(X_train)
            self.x_data = X_train
            self.y_data = y_train

        # Hỗ trợ lập chỉ mục sao cho bộ dữ liệu [i] có thể được sử dụng để lấy mẫu thứ i
        def __getitem__(self, index):
            return self.x_data[index], self.y_data[index]

        # Chúng ta có thể gọi len(dataset) để trả về kích thước
        def __len__(self):
            return self.n_samples
        
    dataset = ChatDataset()
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    
    # Mất mát và tối ưu hóa
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    # Train the model (Đào tạo mô hình)
    epoch_array = []
    for epoch in range(num_epochs):
        for (words, labels) in train_loader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)
            
            # Chuyển tiếp qua
            outputs = model(words)
            # Nếu y là một điểm nóng, chúng ta phải áp dụng
            # Nhãn = torch.max(nhãn, 1)[1]
            loss = criterion(outputs, labels)
            
            # Lùi lại và tối ưu hóa
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
        if (epoch+1) % 100 == 0:
            print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
            epoch_array.append(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
    
    # Thêm vào kết quả hiển thị trả về
    results.append({"Epoch": epoch_array})
    
    print(f'final loss: {loss.item():.4f}')
    results.append({"Final loss": f'{loss.item():.4f}'})
    
    data = {
        "model_state": model.state_dict(),
        "input_size": input_size,
        "hidden_size": hidden_size,
        "output_size": output_size,
        "all_words": all_words,
        "tags": tags
    }

    FILE = "backend/data.pth"
    torch.save(data, FILE)
    print(f'Training complete. file saved to {FILE}')
    
    # Thêm vào kết quả hiển thị trả về
    results.append({"Result": f'Training complete. File saved to {FILE}'})
    
    return jsonify({
        'status':'Success',
        'message':'Train Chatbot success',
        'data': results
    }), 200
#################################################################


#################################################################
# API chatbot                                                   #
#################################################################
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    
    # Lấy dữ liệu từ chatbot đã huấn luyện
    if (len(data['question']) > 0):
        response_chatbot = get_response(data['question'])
        
        # Nhận danh mục loại đúng với từ khóa tìm kiếm của người dùng đã thêm trong từ điển
        category_names = process_category(data['question'])
        
        question = corpus_process(data['question'])
        response = corpus_process(response_chatbot)
        
        if (compare_strings(response_chatbot, ResponseMessage.MESSAGE_SORRY.value) == True or 
            compare_array_source_array_dest(question, response) == True):
            
            # Lọc theo áo hoặc quần hoặc váy hoặc đầm
            categories_by_body = get_categories_full_by_body(data['question'])
            if len(categories_by_body) > 0 and len(category_names) > 0:
                category_names += categories_by_body + get_intent_history(data['session_user'])
                # Trả về list thuộc theo áo hoặc quần hoặc váy hoặc đầm
                response_chatbot = ResponseMessage.BODY_TYPE.value.format(body_type=process_products_with_category(filter_duplicate_in_array(category_names), data['question'], '', ''))
                # Lưu lịch sử chatbot
                history = History(
                    session_user=data['session_user'],
                    user_say=data['question'],
                    chat_response=response_chatbot,
                    concepts=json.dumps(category_names),
                    message_type=MessageType.TEXT.value
                )
                history.save()
                return jsonify({
                    "answer": response_chatbot
                })
            
        
            # Lấy ý niệm trước đó
            if len(category_names) == 0:
                category_names += get_intent_history(data['session_user'])
                # Lấy sizes từ người dùng nhập
                sizes = filter_duplicate_in_array(get_size_user_say(data['question']))
                # Lấy colors từ người dùng nhập
                colors = filter_duplicate_in_array(get_color_user_say(data['question']))
                # Kiểm tra sản phẩm có size, color thuộc catagory không
                categories_filtered = check_product_has_sizes_colors_with_categories(filter_duplicate_in_array(category_names), sizes, colors)
                if len(categories_filtered) > 0:
                    #response_chatbot = ResponseMessage.BODY_TYPE.value.format(body_type=process_products_with_category(categories_filtered, data['question'], '', ''))
                    response_chatbot += process_products_with_category(categories_filtered, data['question'], '', '')
                    # Lưu lịch sử chatbot
                    history = History(
                        session_user=data['session_user'],
                        user_say=data['question'],
                        chat_response=response_chatbot,
                        concepts=json.dumps(category_names),
                        message_type=MessageType.TEXT.value
                    )
                    history.save()
                    return jsonify({
                        "answer": response_chatbot
                    })
                else:
                    # response_chatbot = ResponseMessage.BODY_TYPE.value.format(body_type=process_products_with_category(filter_duplicate_in_array(category_names), data['question']))
                    # Lưu lịch sử chatbot
                    history = History(
                        session_user=data['session_user'],
                        user_say=data['question'],
                        chat_response=response_chatbot,
                        concepts=json.dumps(category_names),
                        message_type=MessageType.TEXT.value
                    )
                    history.save()
                    return jsonify({
                        "answer": response_chatbot
                    })
            
            
            if len(category_names) > 0:
                response_chatbot += process_products_with_category(filter_duplicate_in_array(category_names), data['question'], '', '')


    # Lưu lịch sử chatbot
    history = History(
        session_user=data['session_user'],
        user_say=data['question'],
        chat_response=response_chatbot,
        concepts=json.dumps(category_names),
        message_type=MessageType.TEXT.value
    )
    history.save()
    return jsonify({
        "answer": response_chatbot
    })


# Lấy ý niệm trước đó
def get_intent_history(session_user):
    histories = History.query.filter_by(session_user=session_user).all()
    category_names = []
    for history in [history.concepts for history in histories]:
        words = json.loads(history)
        if len(words) > 0:
            category_names += words
    return category_names

# Lọc theo áo, quần, váy hoặc đầm
def get_categories_full_by_body(user_say):
    tokens = nltk.word_tokenize(user_say)
    find_body = filter_bodys(tokens, ResponseCategoryBody.BODY.value)
    categories = Category.query.filter_by(category_type=find_body).all()
    category_names = [str(category.category_name) for category in categories]
    return category_names

# Lấy text size từ người dùng chat 
def get_size_user_say(user_say):
    tokens = nltk.word_tokenize(user_say)
    size_enum = ResponseSizes.SIZES.value
    sizes = []
    for token in tokens:
        for i in range(len(size_enum)):
            if re.search(token.upper(), size_enum[i]):
                sizes.append(token)
    return sizes

# Lấy text color từ người dùng chat 
def get_color_user_say(user_say):
    word_bigram_trigram = corpus_process(user_say)
    colors = []
    for word_val in word_bigram_trigram:
        words = find_word(word_val)
        if len(words) > 0 and check_uppercase_in_array(words).any() == True:
            colors += words
    return colors

# Lấy size từ người dùng chat 
def check_product_has_sizes_colors_with_categories(category_name_array, sizes, colors):
    categories = Category.query.filter(Category.category_name.in_(category_name_array)).all()
    category_id_str = ','.join([str(category.id) for category in categories])
    url_product = ResponseURL.URL_PRODUCT.value.format(categories=category_id_str)
    response = requests.get(url_product).json()
    category_ids = []
    
    # Kiểm tra sản phẩm có size, color thuộc catagory
    for product in response['data']:
        size_pro = [size.lower() for size in product['sizes']]
        size_user = [size.lower() for size in sizes]
        color_pro = [color.lower() for color in product['colors']]
        color_user = [color.lower() for color in colors]
        is_size = compare_array_source_array_dest(size_user, size_pro)
        is_color = compare_array_source_array_dest(color_user, color_pro)
        if (is_size == True or is_color == True):
            category_ids.append(product['category_id'])
            
    category_name_filtered = []
    if len(category_ids) > 0:
        for category in categories:
            if category.id in category_ids:
                category_name_filtered.append(category.category_name)
    
    return category_name_filtered

# Xử lý dữ liệu phân tích
def corpus_process(user_say):
    contents = []
    
    # Mã hóa văn bản.
    tokens = nltk.word_tokenize(user_say)

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

# Xử lý danh mục phân tích
def process_category(data_text):
    response_words = []
    data_word_array = corpus_process(data_text)
    for data_word in data_word_array:
        words = find_word(data_word)
        for word in words:
            if response_words.count(word) == 0 and not word.isupper():
                response_words.append(word)
    
    return response_words

# Xử lý danh mục phân tích với sản phẩm danh sách kết quả
def process_products_with_category(category_name_array, question, size, color):
    response_chatbot = " "
    
    # Lấy sizes từ người dùng nhập
    sizes = filter_duplicate_in_array(get_size_user_say(question))
    if len(sizes) == 1:
        size = sizes[0]
        
    # Lấy colors từ người dùng nhập
    colors = filter_duplicate_in_array(get_color_user_say(question))
    if len(colors) == 1:
        color = colors[0]
    
    categories = Category.query.filter(Category.category_name.in_(category_name_array)).all()
    category_id_str = ','.join([str(category.id) for category in categories])
    product_url = ResponseURL.URL.value.format(categories=category_id_str, size=size, color=color)
    if len(categories) > 0:
        response_chatbot += ResponseURL.TAG_A.value.format(url=product_url, text_user=question)
    
    return response_chatbot
#################################################################


#################################################################
# API upload_file                                               #
#################################################################
@app.route("/upload_file", methods=["POST"])
def upload_file():
    if 'file_image' in request.files:
        return upload_image(request)
#################################################################


#################################################################
# API add_history                                               #
#################################################################
@app.post('/add_history')
def add_history():
    data = request.json
    
    # Quy trình nhận danh mục
    category_names = process_category(data['user_say'])
    
    # Lấy dữ liệu từ chatbot
    if (len(data['user_say']) > 0):
        response_chatbot = get_response(data['user_say'])
    
    # Quy trình lấy danh sách sản phẩm theo danh mục
    if (compare_strings(response_chatbot, ResponseMessage.MESSAGE_SORRY.value) == False):
        response_chatbot += process_products_with_category(category_names, data['user_say'], '', '')
    
    history = History(
        session_user=data['session_user'],
        user_say=data['user_say'],
        chat_response=response_chatbot,
        concepts=json.dumps(category_names),
        message_type=MessageType.TEXT.value
    )
    
    history.save()
    return {"message": "History created successfully."}
#################################################################


#################################################################
# API get_histories                                             #
#################################################################
@app.get('/get_histories')
def get_histories():
    histories = [history.json() for history in History.query.all()]
    return jsonify({
        'status':'Success',
        'message':'Get Histories list success',
        'data': histories
    }), 200
#################################################################


#################################################################
# API get_history_by_session                                    #
#################################################################
@app.post('/get_history_by_session')
def get_history_by_session():
    data = request.json
    histories = [history.json() for history in History.find_by_session(data["session_user"])]
    return jsonify({
        'status':'Success',
        'message':'Get Histories list success',
        'data': histories
    }), 200
#################################################################


#################################################################
# API Add Intent Pattern Response                               #
#################################################################
@app.post('/create_or_edit_intent')
def add_intent():
    data = request.json
    intent = Intent(tag=data['tag'], description=data['description'])
    message = "Intent created successfully."
    
    if data['id'] != 0:
        intent.update({
            'id':data['id'],
            'tag':data['tag'],
            'description':data['description']
        })
        message = "Intent updated successfully."
    else:
        intent.save()
        
    if int(data['id']) == 0:
        data['id'] = intent.id
    
    # filter delete patterns
    pattern_ids_db = [pattern.id for pattern in Pattern.query.filter_by(intent_id=int(data['id'])).all()]
    pattern_ids = [int(pattern_val['id']) for pattern_val in data['patterns'] if int(pattern_val['id']) > 0]
    pattern_diff_ids = [x for x in pattern_ids_db if x not in set(pattern_ids)]
    for pattern_id in pattern_diff_ids:
        pattern_del = Pattern.query.filter_by(id=pattern_id).first()
        pattern_del.delete()
    
    # patterns
    for pattern_val in data['patterns']:
        pattern = Pattern(pattern_text=pattern_val['pattern_text'], intent_id=int(data['id']))
        if pattern_val['id'] != 0:
            pattern.update({
                'id':pattern_val['id'],
                'pattern_text':pattern_val['pattern_text'],
                'intent_id':pattern_val['intent_id']
            })
        else:
            pattern.save()
            
    # filter delete responses
    response_ids_db = [response.id for response in Response.query.filter_by(intent_id=int(data['id'])).all()]
    response_ids = [int(response['id']) for response in data['responses'] if int(response['id']) > 0]
    response_diff_ids = [x for x in response_ids_db if x not in set(response_ids)]
    for response_id in response_diff_ids:
        response_del = Response.query.filter_by(id=response_id).first()
        response_del.delete()
        
    # responses
    for response_val in data['responses']:
        response = Response(response_text=response_val['response_text'], intent_id=int(data['id']))
        if response_val['id'] != 0:
            response.update({
                'id':response_val['id'],
                'response_text':response_val['response_text'],
                'intent_id':response_val['intent_id']
            })
        else:
            response.save()
    
    return {"message": message}
#################################################################


#################################################################
# API Get Detail Intent Pattern Response                        #
#################################################################
@app.get('/get_detail_intent/<int:intent_id>')
def get_detail_intent(intent_id):
    intent = Intent.query.filter_by(id=intent_id).first()
    if intent is None:
        return jsonify({
            'status':'NotFound',
            'message':'Not found Intent'
        }), 404
        
    return jsonify({
        'status':'Success',
        'message':'Get Intent detail success',
        'data': intent.json()
    }), 200
#################################################################


#################################################################
# API Get List Intent Pattern Response                          #
#################################################################
@app.get('/get_intents')
def get_intents():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 15, type=int)
    sort_by = request.args.get('sort_by', 'id')
    sort_order = request.args.get('sort_order', 'asc')
    
    if sort_order == 'asc':
        sort_func = getattr(Intent, sort_by)
    else:
        sort_func = getattr(Intent, sort_by).desc()
        
    data = Intent.query.order_by(sort_func).paginate(page=page, per_page=per_page)
    results = [intent.json() for intent in data]
        
    return jsonify({
        'status':'Success',
        'message':'Get Intent list success',
        'data': results,
        'total_pages': data.pages,
        'total_records': data.total,
        'current_page': data.page,
        'prev_page': data.prev_num,
        'next_page': data.next_num
    }), 200
#################################################################


#################################################################
# API Delete Intent Pattern Response                            #
#################################################################
@app.delete('/delete_intent/<int:intent_id>')
def delete_intent(intent_id):
    intent = Intent.query.get(intent_id)
    
    if intent is None:
        return jsonify({
            'status':'NotFound',
            'message':'Not found Intent'
        }), 404
    
    for pattern in intent.patterns:
        pattern.delete()
    
    for response in intent.responses:
        response.delete()
        
    intent.delete()
    
    return jsonify({
        'status':'Success',
        'message':'Delete Intent success'
    }), 200
#################################################################


#################################################################
# API Add Intent Pattern Response                               #
#################################################################
@app.put('/update_status_order')
def update_status_order():
    data = request.json
    order = Order.query.filter_by(id=data['order_id']).first()
    order.update(order.id, data['status'])
    return jsonify({
        'message': f"Update Status [{data['status']}] Order success",
    }), 200
#################################################################


#################################################################
# API fill text                                                 #
#################################################################
@app.get('/fill_add_text')
def fill_add_text():
    data = request.json
    results = []
    for word in data['words']:
        text_remove_accents = ViUtils.remove_accents(word)
        results.append(word.lower())
        results.append(word.capitalize())
        results.append(f'{text_remove_accents.lower()}')
        results.append(f'{text_remove_accents.capitalize()}')
        
    data_results = []
    for text in results:
        data_results.append(text.replace("b'", "").replace("'", ""))
        
    return jsonify({
        'data': data_results
    }), 200
#################################################################


@app.errorhandler(Exception)
def handle_exception(error):
    error_message = str(error)  # Extract the error message as a string
    return CommonResponse.internal_server_error("An error occurred while processing the request.", error_message)

if __name__ == '__main__':
    app.run(debug=True)