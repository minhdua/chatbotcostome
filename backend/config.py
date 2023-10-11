import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')  # Cần cung cấp giá trị SECRET_KEY từ biến môi trường
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER','backend/static/') #'backend/static/uploads/'
    IMAGE_DEFAULT_URL = os.getenv('IMAGE_DEFAULT_URL','http://127.0.0.1:5000/static/')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI_DEV')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI_PROD')

swagger_config = {
    "headers": [],
    "specs": [{"endpoint": 'swagger', "route": '/swagger.json'}],
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "CostomeShop's API",
        "description": "API for CostomeShop",
        "contact": {
            "responsibleDeveloper": "Pham Thi Diem",
            "email": "phamthidiem@gmail.com",
        },
        "version": "1.1.0",
    },
    "schemes": ["http", "https"],
    "operationId": "GetData",
}
