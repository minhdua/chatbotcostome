
import logging
import os

from config import DevelopmentConfig, ProductionConfig
from db import db
from flask import Flask
from flask_admin import Admin
from flask_migrate import Migrate
from flask_restful import Api


def create_app():
    app = Flask(__name__)
    app_env = os.getenv('FLASK_ENV', 'Development')

    if app_env == 'Development':
        app.config.from_object(DevelopmentConfig)
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    elif app_env == 'Production':
        app.config.from_object(ProductionConfig)

    db.init_app(app)
    migrate = Migrate(app, db)
    return app, db

app, db = create_app()
api = Api(app)
admin = Admin()
admin.init_app(app)
