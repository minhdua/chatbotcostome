from app_factory import db
from models.base_mixin import BaseMixin


class FashionNetModel(db.Model, BaseMixin):
    __tablename__ = 'fashion_net_models'

    id = db.Column(db.Integer, primary_key=True)
    model_file = db.Column(db.String(255))  # Tên tệp lưu trữ mô hình
    batch_size = db.Column(db.Integer)  # Kích thước batch
    lr = db.Column(db.Float)  # Tỷ lệ học tập (learning rate)
    stage = db.Column(db.Integer)  # Giai đoạn huấn luyện
    epoch = db.Column(db.Integer)  # Số epoch
    attribute_loss = db.Column(db.Float)  # Mất mát thuộc tính
    blue_cates_loss = db.Column(db.Float)  # Mất mát danh mục blue
    blue_cates_top1 = db.Column(db.Float)  # Top-1 accuracy danh mục blue
    blue_cates_top2 = db.Column(db.Float)  # Top-2 accuracy danh mục blue
    blue_cates_top3 = db.Column(db.Float)  # Top-3 accuracy danh mục blue
    blue_cates_top5 = db.Column(db.Float)  # Top-5 accuracy danh mục blue
    blue_lands_loss = db.Column(db.Float)  # Mất mát lands blue
    concate_category_loss = db.Column(db.Float)  # Mất mát danh mục kết hợp
    loss = db.Column(db.Float)  # Mất mát tổng cộng
    val_attribute_loss = db.Column(db.Float)  # Mất mát thuộc tính trên tập validation
    val_blue_cates_loss = db.Column(db.Float)  # Mất mát danh mục blue trên tập validation
    val_blue_cates_top1 = db.Column(db.Float)  # Top-1 accuracy danh mục blue trên tập validation
    val_blue_cates_top2 = db.Column(db.Float)  # Top-2 accuracy danh mục blue trên tập validation
    val_blue_cates_top3 = db.Column(db.Float)  # Top-3 accuracy danh mục blue trên tập validation
    val_blue_cates_top5 = db.Column(db.Float)  # Top-5 accuracy danh mục blue trên tập validation
    val_blue_lands_loss = db.Column(db.Float)  # Mất mát lands blue trên tập validation
    val_concate_category_loss = db.Column(db.Float)  # Mất mát danh mục kết hợp trên tập validation
    val_loss = db.Column(db.Float)  # Mất mát tổng cộng trên tập validation
    blue_cates_acc = db.Column(db.Float)  # Độ chính xác danh mục
    blue_lands_acc = db.Column(db.Float) # Độ chính xác lands
    red_green_cates_acc = db.Column(db.Float) # Độ chính xác triplet
    red_green_attrs_acc = db.Column(db.Float)  # Độ chính xác thuộc tính
    test_accuracy = db.Column(db.Float)  # Độ chính xác trên tập test
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, model_file, batch_size, lr, stage, epoch, attribute_loss, blue_cates_loss,
                 blue_cates_top1, blue_cates_top2, blue_cates_top3, blue_cates_top5, blue_lands_loss,
                 concate_category_loss, loss, val_attribute_loss, val_blue_cates_loss, val_blue_cates_top1,
                 val_blue_cates_top2, val_blue_cates_top3, val_blue_cates_top5, val_blue_lands_loss,
                 val_concate_category_loss, val_loss, blue_cates_acc, blue_lands_acc, red_green_cates_acc, red_green_attrs_acc, test_accuracy):
        self.model_file = model_file
        self.batch_size = batch_size
        self.lr = lr
        self.stage = stage
        self.epoch = epoch
        self.attribute_loss = attribute_loss
        self.blue_cates_loss = blue_cates_loss
        self.blue_cates_top1 = blue_cates_top1
        self.blue_cates_top2 = blue_cates_top2
        self.blue_cates_top3 = blue_cates_top3
        self.blue_cates_top5 = blue_cates_top5
        self.blue_lands_loss = blue_lands_loss
        self.concate_category_loss = concate_category_loss
        self.loss = loss
        self.val_attribute_loss = val_attribute_loss
        self.val_blue_cates_loss = val_blue_cates_loss
        self.val_blue_cates_top1 = val_blue_cates_top1
        self.val_blue_cates_top2 = val_blue_cates_top2
        self.val_blue_cates_top3 = val_blue_cates_top3
        self.val_blue_cates_top5 = val_blue_cates_top5
        self.val_blue_lands_loss = val_blue_lands_loss
        self.val_concate_category_loss = val_concate_category_loss
        self.val_loss = val_loss
        self.blue_cates_acc = blue_cates_acc
        self.blue_lands_acc = blue_lands_acc
        self.red_green_cates_acc = red_green_cates_acc
        self.red_green_attrs_acc = red_green_attrs_acc
        self.test_accuracy = test_accuracy

    def json(self):
        return {
            'id': self.id,
            'model_file': self.model_file,
            'batch_size': self.batch_size,
            'lr': self.lr,
            'stage': self.stage,
            'epoch': self.epoch,
            'attribute_loss': self.attribute_loss,
            'blue_cates_loss': self.blue_cates_loss,
            'blue_cates_top1': self.blue_cates_top1,
            'blue_cates_top2': self.blue_cates_top2,
            'blue_cates_top3': self.blue_cates_top3,
            'blue_cates_top5': self.blue_cates_top5,
            'blue_lands_loss': self.blue_lands_loss,
            'concate_category_loss': self.concate_category_loss,
            'loss': self.loss,
            'val_attribute_loss': self.val_attribute_loss,
            'val_blue_cates_loss': self.val_blue_cates_loss,
            'val_blue_cates_top1': self.val_blue_cates_top1,
            'val_blue_cates_top2': self.val_blue_cates_top2,
            'val_blue_cates_top3': self.val_blue_cates_top3,
            'val_blue_cates_top5': self.val_blue_cates_top5,
            'val_blue_lands_loss': self.val_blue_lands_loss,
            'val_concate_category_loss': self.val_concate_category_loss,
            'val_loss': self.val_loss,
            'blue_cates_acc': self.blue_cates_acc,
            'blue_lands_acc': self.blue_lands_acc,
            'red_green_cates_acc': self.red_green_cates_acc,
            'red_green_attrs_acc': self.red_green_attrs_acc,
            'test_accuracy': self.test_accuracy,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __repr__(self):
        return f"<FashionNetModel(id={self.id}, model_file='{self.model_file}')>"

    def get_model_latest():
        return FashionNetModel.query.order_by(FashionNetModel.id).first()
    
    def get_model_by_model_file(model_file):
        return FashionNetModel.query.filter_by(model_file=model_file).first()

    def find_by_model_file(model_file):
        return FashionNetModel.query.filter_by(model_file=model_file).first()