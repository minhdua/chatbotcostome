from db import db
from models.base_mixin import BaseMixin


class AiConfig(db.Model, BaseMixin):
    __tablename__ = 'ai_configs'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))  # Mô tả cấu hình
    config_name = db.Column(db.String(255))  # Tên cấu hình
    string_value = db.Column(db.String(255))  # Giá trị string
    int_value = db.Column(db.Integer)  # Giá trị integer
    float_value = db.Column(db.Float)  # Giá trị float
    bool_value = db.Column(db.Boolean)  # Giá trị boolean
    # Bổ sung thêm các trường cấu hình khác nếu cần

    def __init__(self, config_name, description, string_value, int_value, float_value, bool_value):
        self.config_name = config_name
        self.description = description
        self.string_value = string_value
        self.int_value = int_value
        self.float_value = float_value
        self.bool_value = bool_value
        # Khởi tạo các trường cấu hình khác nếu có

    def json(self):
        return {
            'id': self.id,
            'config_name': self.config_name,
            'description': self.description, 
            'string_value': self.string_value,
            'int_value': self.int_value,
            'float_value': self.float_value,
            'bool_value': self.bool_value,
        }
    
    def find_by_name(config_name):
        return AiConfig.query.filter_by(config_name=config_name).first()

    def __repr__(self):
        return f"<AiConfig(id={self.id}, config_name='{self.config_name}')>"
