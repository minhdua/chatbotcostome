import os
import logging
from datetime import datetime
from pathlib import Path
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.preprocessing import MultiLabelBinarizer
import keras
from keras.layers import Layer
import imgaug as ia
import tensorflow as tf
from imgaug import augmenters as iaa
from keras import backend as K
from keras import layers
from keras.models import Model
from keras.applications import VGG16
from keras.applications.resnet50 import preprocess_input
from keras.optimizers import Adam
from keras.preprocessing.image import array_to_img, img_to_array
from keras.utils import Sequence, to_categorical
from keras.callbacks import CSVLogger, LambdaCallback, ModelCheckpoint, TensorBoard

from models.attribute_prediction_model import AttributePrediction
from models.category_prediction_model import CategoryPrediction
from models.clothing_image_features_model import ClothingImageFeatures
from models.fashionet_model import FashionNetModel


image_shape = (224, 224, 3)  # all images will be adjusted to this shape
no_model = 1
num_attr = 463  # each image has 463 attribute
num_category = 23  # all images belong to 23 category
num_landmark_visibility = 3  # each landmark has 3 visibility
steps = 0
model_dict = {
    1: 'fashionnet',
    2: 'resnet34'
}
MODEL_PATH = f'backend/resources/cnn/models/{model_dict[no_model]}/'
LOGGER_PATH = f'backend/resources/cnn/logs/{model_dict[no_model]}/'

train_df = None
val_df = None
test_df = None
category_weight = None
attribute_weight = None
model = None
histories = []
class CustomMultiLabelBinarizer(MultiLabelBinarizer):
    def __init__(self, classes=None):
        super().__init__(classes=classes)
        self._cached_dict = None
   
# from keras_contrib.applications import ResNet

# from lapjv import lapjv    # if use conda，need to install from lapjv's git repo
def expand_path(p, **kwargs):
    """Đọc đường dẫn đầy đủ
    
    Arguments
        p: chuỗi đường dẫn trong tệp CSV, ví dụ như `img/MEN/Denim/id_00000080/01_1_front.jpg`
        
    Return:
        Đường dẫn đầy đủ, ví dụ như `../data/input/Img/img/MEN/Denim/id_00000080/01_1_front.jpg`
    """
    header = Path('backend/static/')
    return str(header / p)

def read_raw_image(p, **kwargs):
    """Đọc hình ảnh từ đường dẫn
    
    Arguments
        p: chuỗi đường dẫn trong dữ liệu, ví dụ như `img/MEN/Denim/id_00000080/01_1_front.jpg`
    
    Return
        Đối tượng hình ảnh PIL
    """
    img = Image.open(expand_path(p))
    return img

def get_aug(rate=0.8):
    """Công cụ tăng cường dữ liệu cho tập dữ liệu.

    Tài liệu chính thức: https://github.com/aleju/imgaug

    Tham số
        rate: tỷ lệ sử dụng công cụ tăng cường dữ liệu. Nếu là 1, tất cả các hình ảnh sẽ sử dụng công cụ tăng cường dữ liệu, nếu là 0, không có hình ảnh nào sử dụng công cụ tăng cường dữ liệu.

    Trả về
        Công cụ tăng cường dữ liệu đã được cấu hình
    """
    sometimes = lambda aug: iaa.Sometimes(rate, aug)
    seq = iaa.Sequential([
        sometimes([
            iaa.Fliplr(0.5),  # Lật ngang với xác suất 0.5
            iaa.Flipud(0.5),  # Lật dọc với xác suất 0.5
            iaa.Crop(percent=(0, 0.15)),  # Cắt ngẫu nhiên một phần pixel và đảm bảo kích thước không thay đổi
            iaa.Sometimes(0.5, iaa.GaussianBlur(sigma=(0, 0.05))),  # Làm mờ Gaussian
            iaa.LinearContrast((0.75, 1.5)),  # Điều chỉnh độ tương phản tuyến tính
            iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),  # Nhiễu Gaussian
            iaa.Multiply((0.9, 1.1), per_channel=0.2),  # Biến đổi tô màu ngẫu nhiên
            iaa.Sometimes(0.6, iaa.Affine(
                scale={"x": (0.9, 1.1), "y": (0.8, 1.2)},
                translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
                rotate=(-15, 15),
                shear=(-8, 8)
            ))
        ]),
        iaa.Resize({'height': image_shape[0], 'width': image_shape[1]})
    ], random_order=True)
    return seq

class TrainSequence(Sequence):
    """Dãy huấn luyện kế thừa từ `Sequence`

    Tham số
        data: Một pd.DataFrame chứa train_df, val_df hoặc test_df
        batch_size: Kích thước batch để đưa vào mô hình
    """
    def __init__(self, data: pd.DataFrame, batch_size=32):
        """Khởi tạo đối tượng

        Thời gian thực hiện: 1 phút 22 giây
        """
        super().__init__()
        self.batch_size = batch_size
        
        self.data = data
        self.seq = get_aug(0.8)
        
        self.mlb = CustomMultiLabelBinarizer()
        self.mlb.classes_ = list(range(num_attr))  # Tổng số 463 thuộc tính
        self.on_epoch_end()
        
    def __getitem__(self, index):
        """Lấy mẫu từ dãy
        Thời gian thực hiện: 265 mili giây
        """
        start = self.batch_size * index
        end = self.batch_size * (index + 1) - 1
        batches = self.data.loc[start:end]
        seq = self.seq.to_deterministic()
        
        # Đọc dữ liệu gốc
        xs_a, attrs_data , cates, lands_v, lands_local = [], [], [], [], []
        for i in range(len(batches)):
            # Đọc hình ảnh
            a = batches.iloc[i]
            x_a = normal_image(np.asarray(read_raw_image(a['image_name']).convert('RGB')))
            xs_a.append(x_a)
            
            # Đọc thuộc tính, khi a['attribute_labels'] chỉ có một nhãn, nó sẽ được đọc là một số nguyên
            try:
                attr = [int(at) for at in str(a['attribute_labels']).split(' ') if at != '']
            except Exception as ex:
                pass
            attrs_data .append(attr)
            # Đọc danh mục (category)
            cates.append(a['category_label'])
            # Đọc điểm đánh dấu (landmark)
            lands_v.extend([a[f'landmark_visibility_{ii}'] for ii in range(1, 9)])
            lands_local.append(ia.KeypointsOnImage([
                ia.Keypoint(
                    x=a[f'landmark_location_x_{ii}'],
                    y=a[f'landmark_location_y_{ii}']
                ) for ii in range(1, 9)
            ], shape=x_a.shape))
            
        # Augment hình ảnh
        xs_a = np.array(seq.augment_images(xs_a))
        # Biểu diến one-hot cho danh mục (category)
        lands_v = to_categorical(lands_v, num_landmark_visibility)
        # Augment điểm đánh dấu   
        lands_local = seq.augment_keypoints(lands_local)
        res = []
        for local in lands_local:
            for keypoint in local.keypoints:
                res.append([keypoint.x, keypoint.y])
        lands_local = res
        try:
            lands_local = np.array(lands_local) / image_shape[:2]  # Scale về khoảng từ 0 đến 1
        except ValueError as e:
            # Kiểm tra tất cả dữ liệu đầu vào không thể chứa giá trị rỗng, nhưng vẫn có lỗi về kích thước không phù hợp,
            # ở đây kiểm tra dữ liệu nào có vấn đề
            raise ValueError(f"Lỗi: {e}, \n Hình ảnh: {batches['image_name']}'， \n Điểm đánh dấu: {lands_local}")
        lands = np.concatenate((lands_v, lands_local), axis=1)
        # Từ (None*8, 5) thành (None, 8*5)
        lands = lands.reshape((len(batches), -1))
        
        # Chuyển đổi danh mục (category) thành one-hot
        cates = to_categorical(cates, num_category)
        # Chuyển đổi dữ liệu thuộc tính (attrs_data)
        transformed_attrs_data = self.mlb.transform(attrs_data)

        return xs_a, [cates, lands, cates, transformed_attrs_data ]
    
    def on_epoch_end(self):
        """Thực hiện khi kết thúc epoch

        Thời gian thực hiện: 1 phút 3.57 giây
        """
        self.data = self.data.sample(frac=1.0).reset_index(drop=True)
    
    def __len__(self):
        return (len(self.data) + self.batch_size - 1) // self.batch_size
    
def normal_image(img):
    """Chuẩn hóa một hình ảnh bằng công cụ chuẩn hóa chính thống từ ImageNet.

    Tham số
        img: np.ndarray của pil.Image.Image

    Trả về
        Hình ảnh đã được chuẩn hóa
    """
    if isinstance(img, Image.Image):
        img = np.array(img, K.floatx())
    img = preprocess_input(img)
    return img

class ValSequence(TrainSequence):
    """Dãy kiểm định (validation) kế thừa từ `TrainSeqence`

    Tham số
        data: Một pd.DataFrame chứa train_df, val_df hoặc test_df
        batch_size: Kích thước batch để đưa vào mô hình
    """
    def __init__(self, data: pd.DataFrame, batch_size=32):
        """Khởi tạo đối tượng

        Thời gian thực hiện: 1 phút 22 giây
        """
        super().__init__(data=data, batch_size=batch_size)
        # Đảm bảo không sử dụng tăng cường dữ liệu bằng cách đặt tỷ lệ = 0
        self.seq = get_aug(0)

def category_classweight():
    """Tính toán trọng số lớp cho danh mục (category)

    Trả về
        Một mảng 1D numpy, với chỉ số tương ứng với danh mục (category)
    """
    class_dict = train_df['category_label'].value_counts().to_dict()
    num_max = max(class_dict.values())
    class_weight = []
    for i in range(num_category):
        label = str(i)
        if label not in class_dict:
            class_weight.append(0.)
        else:
            class_weight.append(730 / class_dict[label])
    class_weight = np.array(class_weight)
    return class_weight


def attribute_classweight():
    """Tính toán trọng số lớp cho thuộc tính (attribute)

    Trả về
        p_weight: Trọng số dương của train_df
        n_weight: Trọng số âm của train_df
    """
    p_weight = 0
    for i in range(len(train_df)):
        attrs_data = str(train_df.iloc[i]['attribute_labels'])
        p_weight += len(attrs_data.split(' '))
    p_weight = p_weight / (len(train_df) * num_attr)
    n_weight = 1 - p_weight
    return p_weight, n_weight

def category_loss(y_true, y_pred, gamma=0.):
    """Hàm mất mát của loại sử dụng Focal Loss.

    Tài liệu tham khảo của Focal Loss là "Focal Loss for Dense Object Detection."

    Tham số
        y_true: Mục tiêu học tập, hình dạng=(None, 23)
        y_pred: Giá trị dự đoán, hình dạng=(None, 23)
        gamma: Nếu là 0, Focal Loss tương đương với mất mát Cross-Entropy của loại.

    Trả về
        Mất mát, hình dạng=(None, 1)
    """
    loss = -y_true * K.log(y_pred + K.epsilon()) * category_weight
    loss = K.sum(loss, axis=-1)
    return loss

def attribute_loss(y_true, y_pred, gamma=0.):
    """Hàm mất mát của thuộc tính sử dụng Focal Loss.

    Tài liệu tham khảo của Focal Loss là "Focal Loss for Dense Object Detection."

    Tham số
        y_true: Mục tiêu học tập, hình dạng=(None, 463)
        y_pred: Giá trị dự đoán, hình dạng=(None, 463)
        gamma: Nếu là 0, Focal Loss tương đương với mất mát Cross-Entropy của loại.

    Trả về
        Mất mát, hình dạng=(None, 1)
    """
    y_true = K.cast(y_true, K.floatx())
    y_pred = K.cast(y_pred, K.floatx())

    y_ = y_true * y_pred + (1.0 - y_true) * (1.0 - y_pred) + K.epsilon()

    loss = -K.log(y_)

    weight = y_true * attribute_weight[0] + (1.0 - y_true) * attribute_weight[1]
    loss *= weight

    loss = K.sum(loss, axis=-1)
    return loss

def lands_loss(y_true, y_pred):
    """Mất mát của các điểm địa danh bao gồm hai phần, Cross-Entropy của sự hiển thị của các điểm đánh dấu
    và mất mát L2 của vị trí của các điểm đánh dấu.

    Tham số
        y_true: Mục tiêu học tập, hình dạng=(None, 40). Và mỗi điểm đánh dấu bao gồm trạng thái hiển thị
            của 3 yếu tố và vị trí (x/w, y/h) của 2 yếu tố. Và mỗi hình ảnh có 8 điểm đánh dấu.
        y_pred: Giá trị dự đoán, hình dạng=(None, 40).

    Trả về
        Mất mát, hình dạng=(None, 1)
    """
    y_true = K.reshape(y_true, (-1, 5))
    y_pred = K.reshape(y_pred, (-1, 5))

    lands_true = y_true[:, 3:]
    lands_pred = y_pred[:, 3:]
    lands_gate = y_true[:, 0, None]    # chỉ tính toán các điểm đánh dấu hiển thị
    lands = K.sum((K.sigmoid(lands_pred) - lands_true) ** 2 * lands_gate, axis=-1)

    lands_v_true = y_true[:, :3]
    lands_v_pred = y_pred[:, :3]
    visibility = -lands_v_true * K.log(K.softmax(lands_v_pred) + K.epsilon())
    visibility = K.sum(visibility, axis=-1)

    loss = lands + visibility
    loss = K.sum(K.reshape(loss, (-1, 8)), axis=-1)
    return loss

def triplet_loss(y_true, y_pred):
    """Mất mát triplet.

    Tài liệu tham khảo của mất mát triplet là "In Defense of the Triplet Loss for Person Re-Identification."

    Tham số
        y_true: Mục tiêu học tập, hình dạng=(None, 1). Trong thực tế, mất mát triplet không cần mục tiêu nào,
            nhưng khung làm việc Keras cần.

        y_pred: Giá trị dự đoán, hình dạng=(None, chiều của tensor đầu ra)

    Trả về
        Mất mát, hình dạng=(None, 1)
    """

    margin = 0.3
    loss = K.sum(y_pred, axis=-1, keepdims=True)
    # không sử dụng K.max, nó tính giá trị tối đa trong một tensor.
    loss = K.maximum(0., margin + loss + 0. * y_true)
    return loss

def top1(y_true, y_pred, k=1):
    """Độ chính xác top-1 danh mục

    Tham số
        y_true: Mục tiêu học tập, hình dạng=(None, 23)
        y_pred: Giá trị dự đoán, hình dạng=(None, 23)

    Trả về
        Độ chính xác top-1, hình dạng=(None, 1)
    """
    return K.cast(K.in_top_k(y_pred, K.argmax(y_true, axis=-1), k), K.floatx())

def top2(y_true, y_pred, k=2):
    """Độ chính xác top-2 danh mục

    Tham số
        y_true: Mục tiêu học tập, hình dạng=(None, 23)
        y_pred: Giá trị dự đoán, hình dạng=(None, 23)

    Trả về
        Độ chính xác top-2, hình dạng=(None, 1)
    """
    return K.cast(K.in_top_k(y_pred, K.argmax(y_true, axis=-1), k), K.floatx())

def top3(y_true, y_pred, k=3):
    """Độ chính xác top-3 danh mục

    Tham số
        y_true: Mục tiêu học tập, hình dạng=(None, 23)
        y_pred: Giá trị dự đoán, hình dạng=(None, 23)

    Trả về
        Độ chính xác top-3, hình dạng=(None, 1)
    """
    return K.cast(K.in_top_k(y_pred, K.argmax(y_true, axis=-1), k), K.floatx())

def top5(y_true, y_pred, k=5):
    """Độ chính xác top-5 danh mục

    Tham số
        y_true: Mục tiêu học tập, hình dạng=(None, 23)
        y_pred: Giá trị dự đoán, hình dạng=(None, 23)

    Trả về
        Độ chính xác top-5, hình dạng=(None, 1)
    """
    return K.cast(K.in_top_k(y_pred, K.argmax(y_true, axis=-1), k), K.floatx())

class RoiPooling(Layer):
    """Lớp RoiPooling (tích hợp vùng quan tâm) cho đầu vào 2D.

    Xem Spatial Pyramid Pooling trong Deep Convolutional Networks for Visual Recognition

    Tham số
        pool_size: int. Kích thước vùng quan tâm để sử dụng. pool_size = 7 sẽ tạo ra vùng 7x7.
        num_rois: số lượng vùng quan tâm sẽ được sử dụng
        window_size: kích thước cửa sổ trượt

    Đầu vào
        Một danh sách gồm một 4D tensor và một 2D tensor [X_img, X_roi] với hình dạng:
        X_img: (batch, channels, rows, cols) nếu data_format='channels_first' hoặc 4D tensor với hình dạng:
            (batch, rows, cols, channels) nếu data_format='channels_last'.
        X_roi: (batch, num_rois * 5) danh sách các vùng quan tâm, với sự sắp xếp (x_góc trên bên trái, y_góc trên bên trái) ở
            hai thành phần đầu tiên trong chiều cuối cùng.

    Đầu ra
        4D tensor với hình dạng:
            (batch, pool_size, pool_size, channels * num_rois) nếu data_format='channels_last'
            (batch, channels * num_rois, pool_size, pool_size) nếu data_format='channels_first'
    """
    def __init__(self, pool_size=2, num_rois=8, window_size=4, **kwargs):
        self.data_format = K.image_data_format()
        assert self.data_format in {'channels_last', 'channels_first'}, 'data_format phải nằm trong {channels_last, channels_first}'
        self.window_size = window_size
        self.pool_size = pool_size
        self.num_rois = num_rois
        super().__init__(**kwargs)

    def build(self, input_shape):
        if self.data_format == 'channels_first':
            self.nb_channels = input_shape[0][1]
        elif self.data_format == 'channels_last':
            self.nb_channels = input_shape[0][3]

    def compute_output_shape(self, input_shape):
        if self.data_format == 'channels_first':
            return None, self.num_rois * self.nb_channels, self.pool_size, self.pool_size
        else:
            return None, self.pool_size, self.pool_size, self.nb_channels * self.num_rois

    def call(self, x, mask=None): 
        assert (len(x) == 2)
        # Đầu vào là các đặc trưng và thông tin tọa độ
        img, rois = x[0], x[1]
        
        # Chuyển đổi ảnh
        if self.data_format == 'channels_first':
            img = K.permute_dimensions(img, (0, 2, 3, 1))
        else:
            img = K.permute_dimensions(img, (0, 1, 2, 3))

        # Chuyển đổi các hộp quan tâm
        shape = K.shape(img)
        rois = K.reshape(rois, (-1, 5))[:, 3:]
        x1 = rois[..., 0]
        y1 = rois[..., 1]

        if shape[2] is not None:
            x2 = rois[..., 0] + K.cast(self.window_size / shape[2], K.floatx())
        else:
            x2 = rois[..., 0]

        if shape[1] is not None:
            y2 = rois[..., 1] + K.cast(self.window_size / shape[1], K.floatx())
        else:
            y2 = rois[..., 1]

        x1 = K.expand_dims(x1, axis=-1)
        y1 = K.expand_dims(y1, axis=-1)
        x2 = K.expand_dims(x2, axis=-1)
        y2 = K.expand_dims(y2, axis=-1)

        boxes = K.concatenate([y1, x1, y2, x2], axis=-1)

        # Chuyển đổi ảnh
        img = K.concatenate([img] * self.num_rois, axis=1)
        try:
            img = K.reshape(img, (-1, 512)) # reshape chiều cuối
            img = K.reshape(img, (-1, 28, 28, 512)) # reshape các chiều còn lại
        except Exception as e:
            logging.error("Error in RoiPooling layer:", e)

        # Cắt và thay đổi kích thước ảnh
        # đầu vào: img(None*8, H, W, C), boxes(None*8, 4)
        # trả về: tensor(None, chiều_cao_đoạn, chiều_rộng_đoạn, C*số_boxes)
        box_ind = K.zeros_like(boxes, 'int32')
        box_ind = box_ind[..., 0]
        box_ind = K.reshape(box_ind, (-1, ))

        slices = tf.image.crop_and_resize(img, boxes, box_ind, (self.pool_size, self.pool_size))
        slices = K.reshape(slices, (-1, self.pool_size, self.pool_size, self.num_rois * shape[-1]))

        if self.data_format == 'channels_first':
            slices = K.permute_dimensions(slices, (0, 3, 1, 2))
        else:
            slices = K.permute_dimensions(slices, (0, 1, 2, 3))
        return slices
    
def build_model():
    """Xây dựng mô hình Fashion Net

    Tài liệu tham khảo về focal loss là DeepFashion: Powering Robust Clothes Recognition và
    Retrieval with Rich Annotations.

    Sử dụng batch normalization để tránh đầu ra của mạng nơ-ron bằng 0.

    Tham số
        lr: tỷ lệ học tập

    Trả về
        model_stage1: mô hình giai đoạn 1 cho việc huấn luyện
        model_stage2: mô hình giai đoạn 2 cho việc huấn luyện
        model_blue: mô hình cho việc dự đoán danh mục, tầm nhìn các điểm đặc trưng và vị trí các điểm đặc trưng
    """
    kwargs = {'kernel_initializer': 'he_normal', 'padding': 'same'}
    fkwargs = {'kernel_initializer': 'he_normal'}
    
    # Mô hình cơ sở
    inp_a = layers.Input(shape=image_shape, name='inp_a')
    inp_p = layers.Input(shape=image_shape, name='inp_p')
    inp_n = layers.Input(shape=image_shape, name='inp_n')
    
    model = VGG16(input_tensor=inp_a, weights='imagenet')
    # Nếu sử dụng model.trainable = False, block5 sẽ không được huấn luyện
    for layer in model.layers:
        if layer.name == 'block4_pool':
            break
        else:
            layer.trainable = False
    node = model.get_layer(name='block4_conv3').output
    # blue
    blue = layers.MaxPool2D((2, 2), strides=(2, 2), name='blue_pool1')(node)
    blue = layers.Conv2D(512, (3, 3), activation='relu', name='blue_conv1', **kwargs)(blue)
    blue = layers.Conv2D(512, (3, 3), activation='relu', name='blue_conv2', **kwargs)(blue)
    blue = layers.Conv2D(512, (3, 3), activation='relu', name='blue_conv3', **kwargs)(blue)
    blue = layers.MaxPool2D((2, 2), strides=(2, 2), name='blue_pool')(blue)   
    
    blue = layers.Flatten(name='blue_flatten')(blue)
    
    blue = layers.Dense(4096, name='blue_fc1', **fkwargs)(blue)
    blue = layers.BatchNormalization(name='blue_normal1')(blue)
    blue = layers.Activation('relu', name='blue_fc1_activation')(blue)
    blue = layers.Dense(4096, name='blue_fc2', **fkwargs)(blue)
    blue = layers.BatchNormalization(name='blue_normal2')(blue)
    blue = layers.Activation('relu', name='blue_fc2_activation')(blue)
    ## Mất mát danh mục và điểm đặc trưng
    blue_cates = layers.Dense(
        num_category,
        kernel_initializer='he_normal',
        activation='softmax',
        name='blue_cates'
    )(blue)
    blue_lands = layers.Dense(8 * (3 + 2), kernel_initializer='he_normal', name='blue_lands')(blue)
    model_blue = Model(inp_a, [blue_cates, blue_lands], name='model_blue')
    
    # red
    red = layers.MaxPool2D((2, 2), strides=(2, 2), name='red_pool1')(node)
    red = layers.Conv2D(512, (3, 3), activation='relu', name='red_conv1', **kwargs)(red)
    red = layers.Conv2D(512, (3, 3), activation='relu', name='red_conv2', **kwargs)(red)
    red = layers.Conv2D(512, (3, 3), activation='relu', name='red_conv3', **kwargs)(red)
    red = layers.MaxPooling2D((2, 2), strides=(2, 2), name='red_pool')(red)
    red = layers.Flatten(name='red_flatten')(red)
    red = layers.Dense(4096, name='red_fc1', **fkwargs)(red)
    
    # green
    green = RoiPooling(pool_size=2, num_rois=8, window_size=4, name='green_roi')([node, blue_lands])
    green = layers.Flatten(name='green_flatten')(green)
    green = layers.Dense(1024, name='green_fc1', **fkwargs)(green)
    
    # Kết hợp red và green
    red_green = layers.concatenate([red, green], name='concate')
    red_green = layers.BatchNormalization(name='concate_normal')(red_green)
    red_green = layers.Activation('relu', name='concate_activation')(red_green)
    ## Kết hợp mất mát danh mục
    red_green_cates = layers.Dense(
        num_category,
        kernel_initializer='he_normal',
        activation='softmax',
        name='concate_category'
    )(red_green)
    ## Mất mát thuộc tính
    red_green_attrs = layers.Dense(
        num_attr,
        kernel_initializer='he_normal',
        activation='sigmoid',
        name='attribute'
    )(red_green)
      
    model_source = Model(inp_a, [blue_cates, blue_lands, red_green_cates, red_green_attrs])
    
    # Điều chỉnh trọng số
    for layer in model.layers:
        name = layer.name
        if 'block5' in name:
            blue_name = f"blue_{name.split('_')[1]}"
            model_source.get_layer(blue_name).set_weights(layer.get_weights())
            red_name = f"red_{name.split('_')[1]}"
            model_source.get_layer(red_name).set_weights(layer.get_weights())

    return model_source, model_blue

def change_stage(model, lr=3e-4, stage=1):
    """Thay đổi giai đoạn huấn luyện của mô hình

    Tham số
        model: đối tượng mô hình
        lr: tỷ lệ học tập
        stage: nếu là 1, mô hình blue sẽ được huấn luyện, nếu là 2, mô hình blue sẽ không được huấn luyện
    """
    opt = Adam(lr)
    # Giai đoạn 1: huấn luyện nút blue
    if stage == 1:
        for layer in model.layers:
            if 'blue' in layer.name:
                layer.trainable = True 
        model.compile(
            opt,
            loss={
                'blue_cates': category_loss,
                'blue_lands': lands_loss,
                'concate_category': category_loss,
                'attribute': attribute_loss,
            },
            loss_weights={
                'blue_cates': 1.,
                'blue_lands': 1.,
                'concate_category': 0.1,
                'attribute': 0.1,
            },
            metrics={
                'blue_cates': [top1, top2, top3, top5]
            }
        )
    # Giai đoạn 2: huấn luyện nút red và green
    elif stage == 2:
        for layer in model.layers:
            if 'blue' in layer.name:
                layer.trainable = False
                
        model.compile(
            opt,
            loss={
                'blue_cates': category_loss,
                'blue_lands': lands_loss,
                'concate_category': category_loss,
                'attribute': attribute_loss
            },
            loss_weights={
                'blue_cates': 0.,
                'blue_lands': 0.,
                'concate_category': 1.,
                'attribute': 1.
            },
            metrics={
                'concate_category': [top1, top2, top3, top5]
            }
        )
    return model
class LRFinder(object):
    """Dùng để vẽ biểu đồ sự thay đổi của hàm mất mát của một mô hình Keras khi tỷ lệ học tập tăng theo cấp số mũ.
    """
    def __init__(self, model):
        self.model = model
        self.losses = []
        self.lrs = []
        self.best_loss = 1e9

    def on_batch_end(self, batch, logs):
        # Ghi log tỷ lệ học tập
        lr = K.get_value(self.model.optimizer.lr)
        self.lrs.append(lr)

        # Ghi log hàm mất mát
        loss = logs['loss']
        self.losses.append(loss)

        # Kiểm tra xem hàm mất mát có quá lớn hoặc NaN không
        if math.isnan(loss) or loss > self.best_loss * 4:
            self.model.stop_training = True
            return

        if loss < self.best_loss:
            self.best_loss = loss

        # Tăng tỷ lệ học tập cho lượt học kế tiếp
        lr *= self.lr_mult
        K.set_value(self.model.optimizer.lr, lr)

    def find(self, data_gen, start_lr, end_lr, epochs=1, class_weight=None):
        num_batches = epochs * len(data_gen)
        self.lr_mult = (float(end_lr) / float(start_lr)) ** (float(1) / float(num_batches))

        # Lưu trọng số vào một tệp
        self.model.save_weights('tmp.h5')

        # Ghi nhớ tỷ lệ học tập ban đầu
        original_lr = K.get_value(self.model.optimizer.lr)

        # Đặt tỷ lệ học tập ban đầu
        K.set_value(self.model.optimizer.lr, start_lr)

        callback = LambdaCallback(on_batch_end=lambda batch, logs: self.on_batch_end(batch, logs))

        self.model.fit_generator(data_gen, epochs=epochs, callbacks=[callback], class_weight=class_weight)

        # Khôi phục trọng số về trạng thái trước khi huấn luyện mô hình
        self.model.load_weights('tmp.h5')

        # Khôi phục tỷ lệ học tập ban đầu
        K.set_value(self.model.optimizer.lr, original_lr)

    def plot_loss(self, n_skip_beginning=10, n_skip_end=5):
        """
        Vẽ biểu đồ hàm mất mát.
        Tham số:
            n_skip_beginning - số lượng batch bỏ qua bên trái.
            n_skip_end - số lượng batch bỏ qua bên phải.
        """
        plt.ylabel("mất mát")
        plt.xlabel("tỷ lệ học tập (tỷ lệ log)")
        plt.plot(self.lrs[n_skip_beginning:-n_skip_end], self.losses[n_skip_beginning:-n_skip_end])
        plt.xscale('log')

    def plot_loss_change(self, sma=1, n_skip_beginning=10, n_skip_end=5, y_lim=(-0.01, 0.01)):
        """
        Vẽ biểu đồ tốc độ thay đổi của hàm mất mát.
        Tham số:
            sma - số lượng batch cho trung bình động đơn giản để làm mờ đường cong.
            n_skip_beginning - số lượng batch bỏ qua bên trái.
            n_skip_end - số lượng batch bỏ qua bên phải.
            y_lim - giới hạn trục y.
        """
        assert sma >= 1
        derivatives = [0] * sma
        for i in range(sma, len(self.lrs)):
            derivative = (self.losses[i] - self.losses[i - sma]) / sma
            derivatives.append(derivative)

        plt.ylabel("tốc độ thay đổi mất mát")
        plt.xlabel("tỷ lệ học tập (tỷ lệ log)")
        plt.plot(self.lrs[n_skip_beginning:-n_skip_end], derivatives[n_skip_beginning:-n_skip_end])
        plt.xscale('log')
        plt.ylim(y_lim)
    
    def plot_loss_smoothing(self, smoothing=0.6, n_skip_beginning=10, n_skip_end=5):
        """Vẽ đường cong mất mát được làm mờ giống như tensorboard
        """
        losses, lrs = self.losses[n_skip_beginning:-n_skip_end], self.lrs[n_skip_beginning:-n_skip_end]
        last = losses[0]
        smoothes = []
        for point in losses:
            smooth = last * smoothing + (1-smoothing) * point
            smoothes.append(smooth)
            last = point
        
        plt.ylabel("tốc độ thay đổi mất mát được làm mờ")
        plt.xlabel("tỷ lệ học tập (tỷ lệ log)")
        plt.plot(lrs, smoothes)
        plt.xscale('log')
        
def set_lr(model, lr):
    """Cấu hình tỷ lệ học tập của mô hình"""
    K.set_value(model.optimizer.lr, float(lr))
    
    
def get_lr(model):
    """Lấy tỷ lệ học tập của mô hình"""
    return K.get_value(model.optimizer.lr)


def save_model(model,filename):
    """Lưu mô hình của bước hiện tại vào đường dẫn MODEL_PATH"""
    model.save(f"{MODEL_PATH}{filename}")
    
    
def load_model(model, temp_step):
    """Nạp mô hình từ mô hình đã lưu
    
    Tham số
        model: mô hình đã được xây dựng
        temp_step: bước nào của mô hình bạn muốn nạp
    
    Kết quả
        mô hình đã nạp
    """
    global steps
    steps = temp_step
    
    model_file = f'{MODEL_PATH}epoch{steps}.h5'
    tmp = keras.models.load_model(model_file, compile=False)
    model.set_weights(tmp.get_weights())
    return model
    

def load_modelfile(model, modelfile):
    """Nạp mô hình từ đường dẫn mô hình
    
    Tham số
        model: mô hình đã được xây dựng
        modelfile: đường dẫn tệp mô hình, ví dụ: '../data/output/models/fashionnet/epoch.04-0.22-0.333.h5' hoặc
            'epoch.04-0.22-0.333.h5'
    
    Kết quả
        mô hình đã nạp
    """
    import pdb
    global steps
    steps = int(modelfile.split('-')[0].split('.')[-1])
    
    model_file = f'{MODEL_PATH}{modelfile}'
    model.load_weights(model_file, by_name=True)
    return model
    
def compute_test_accuracy(model, test_df, batch_size=64):

    test_gen = ValSequence(test_df, batch_size=batch_size)  
    predictions = model.predict(test_gen, verbose=1)
    
    # Tách tất cả các đầu ra 
    cates_pred = predictions[0]  
    lands_pred = predictions[1]
    triplet_pred = predictions[2]
    attrs_pred = predictions[3]

    # Tính độ chính xác cho mỗi đầu ra
    cates_true = test_df['category_label'].values
    blue_cates_acc = np.mean(np.equal(np.argmax(cates_pred, axis=1), cates_true))
    # Lấy các cột visibility
    land_vis = [f'landmark_visibility_{i}' for i in range(1, 9)]  

    # Chuyển đổi visibility sang one-hot 
    lands_v = test_df[land_vis].values
    lands_v = to_categorical(lands_v, num_landmark_visibility)
    lands_v = lands_v.reshape(-1, 8 * 3)
    # Lấy các cột location
    land_x = [f'landmark_location_x_{i}' for i in range(1, 9)]
    land_y = [f'landmark_location_y_{i}' for i in range(1, 9)]
   
    # Lấy giá trị của các cột location
    lands_x = test_df[land_x].values
    lands_y = test_df[land_y].values

    lands_xy = np.stack((lands_x, lands_y), axis=-1)
    lands_xy = lands_xy.reshape(-1, 8 * 2)
    # Gộp visibility và location 
    lands_true = np.concatenate([lands_v, lands_xy], axis=1)
    # lands_true = lands_true.reshape(-1, 8 * (3 + 2))
    blue_lands_acc = np.mean(np.equal(np.round(lands_pred), lands_true))

    red_green_cates_acc = np.mean(np.equal(np.argmax(triplet_pred, axis=1), cates_true))

    mlb = CustomMultiLabelBinarizer()
    mlb.classes_ = list(range(num_attr))
    attrs_true = mlb.transform(test_df['attribute_labels'].values)  
    red_green_attrs_acc = np.mean([
        np.equal(np.round(attrs_pred[i]), attrs_true[i]).sum() / num_attr
        for i in range(len(test_df)) 
    ])

    test_accuracy = (blue_cates_acc + blue_lands_acc + red_green_cates_acc + red_green_attrs_acc) / 4
    
    # Trả về tất cả độ chính xác
    return [float(f'{blue_cates_acc:.4f}'), float(f'{blue_lands_acc:.4f}'), float(f'{red_green_cates_acc:.4f}'), float(f'{red_green_attrs_acc:.4f}'), float(f'{test_accuracy:.4f}')]

def custom_callback(model, test_df, batch_size, lr, stage, epoch, logs, save_interval, model_file_name):
    """Callback tùy chỉnh để lưu model vào cơ sở dữ liệu và in ra độ chính xác."""
    # Thực hiện các công việc cần thiết tại mỗi epoch
    # Ví dụ: lưu model vào cơ sở dữ liệu và in ra độ chính xác trên tập test
    
    # Lưu model vào cơ sở dữ liệu
    if epoch % save_interval == 0:  # Lưu model sau mỗi 
        model_file_name = model_file_name.replace('epoch', '').replace('val_loss', '').replace('val_blue_cates_loss', '')
        # remove model path
        model_file_name = model_file_name.replace(MODEL_PATH, '')
        model_file_name = model_file_name.replace('.h5', '.keras')
        model_file_name = model_file_name.format(epoch, logs['val_loss'], logs['val_blue_cates_loss'])

        blue_cates_acc, blue_lands_acc, red_green_cates_acc, red_green_attrs_acc, test_accuracy = compute_test_accuracy(model, test_df, batch_size)  # Viết hàm này để tính độ chính xác
        # In ra độ chính xác
        logging.info("Epoch %d - Category Accuracy: %.4f - Attribute Accuracy: %.4f - Test Accuracy: %.4f", steps, blue_cates_acc, red_green_attrs_acc, test_accuracy)
        # Tiến hành lưu thông tin vào cơ sở dữ liệu
        fashion_model = FashionNetModel(
            model_file=model_file_name,
            batch_size=batch_size,
            lr=lr,
            stage=stage,
            epoch=epoch,
            attribute_loss = logs.get('attribute_loss', 0.0),
            blue_cates_loss = logs.get('blue_cates_loss', 0.0),
            blue_cates_top1 = logs.get('blue_cates_top1', 0.0),
            blue_cates_top2 = logs.get('blue_cates_top2', 0.0),
            blue_cates_top3 = logs.get('blue_cates_top3', 0.0),
            blue_cates_top5 = logs.get('blue_cates_top5', 0.0),
            blue_lands_loss = logs.get('blue_lands_loss', 0.0),
            concate_category_loss = logs.get('concate_category_loss', 0.0),
            loss = logs.get('loss', 0.0),
            val_attribute_loss = logs.get('val_attribute_loss', 0.0),
            val_blue_cates_loss = logs.get('val_blue_cates_loss', 0.0),
            val_blue_cates_top1 = logs.get('val_blue_cates_top1', 0.0),
            val_blue_cates_top2 = logs.get('val_blue_cates_top2', 0.0),
            val_blue_cates_top3 = logs.get('val_blue_cates_top3', 0.0),
            val_blue_cates_top5 = logs.get('val_blue_cates_top5', 0.0),
            val_blue_lands_loss = logs.get('val_blue_lands_loss', 0.0),
            val_concate_category_loss = logs.get('val_concate_category_loss', 0.0),
            val_loss = logs.get('val_loss', 0.0),
            blue_cates_acc = blue_cates_acc,
            red_green_attrs_acc = red_green_attrs_acc,
            blue_lands_acc = blue_lands_acc,
            red_green_cates_acc = red_green_cates_acc,
            test_accuracy = test_accuracy
        )
        try:
            fashion_model.save_to_db()
            save_model(model, model_file_name)
        except Exception as e:
            logging.error("Error in saving model to database: %s", e)
        logging.info("Saved model to database")

    
# Định nghĩa lại hàm callbacks() để thêm callback tùy chỉnh
def callbacks():
    """Lấy các callback đào tạo Keras đã được cấu hình"""
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Tạo tên file dựa trên thời gian và các giá trị epoch và mất mát
    model_file_name = f'ckpt_model.{current_time}.{{epoch:02d}}-{{val_loss:.4f}}-{{val_blue_cates_loss:.4f}}.h5'
    ckpt_file = MODEL_PATH + model_file_name
    checkpoint = ModelCheckpoint(ckpt_file, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
    
    csv_log_file = f'{LOGGER_PATH}{model_dict[no_model]}.csv'
    csv_log = CSVLogger(csv_log_file)
    
    tensorboard = TensorBoard(f'{LOGGER_PATH}')
    
    return [checkpoint, csv_log, tensorboard]

def make_steps(step, batch_size=64, lr=3e-4, stage=1, save_interval=1):
    """Huấn luyện trong một số epoch nhất định
    
    Tham số
        step: số epoch mô hình sẽ được huấn luyện 
    """
    global steps, histories

    callbacks_list = callbacks() 
    checkpoint = callbacks_list[0]
    callbacks_list.append(LambdaCallback(
        on_epoch_end=lambda epoch, logs: custom_callback(
            model, test_df, batch_size, lr, stage, epoch, logs, save_interval=save_interval, model_file_name=checkpoint.filepath
        ))
    )
    # Huấn luyện mô hình trong 'step' epoch
    history = model.fit(
        TrainSequence(train_df, batch_size=batch_size),
        validation_data=ValSequence(val_df, batch_size=64),
        callbacks=callbacks_list,
        initial_epoch=steps, epochs=steps + step, max_queue_size=12, workers=8, verbose=1).history
    steps += step

    # Thu thập dữ liệu lịch sử
    history['epochs'] = steps
    history['lr'] = get_lr(model)
    logging.info("Epochs: %d - Learning rate: %f", history['epochs'], history['lr'])
    histories.append(history)
    
def find_lr(model, start_lr=3e-5, end_lr=1):
    """Vẽ đồ thị mất mát-tỷ lệ học tập để tìm một mô hình phù hợp"""
    lr_finder = LRFinder(model)
    lr_finder.find(
        TrainSequence(train_df, batch_size=8),
        start_lr=start_lr, end_lr=end_lr
    )
    lr_finder.plot_loss()
    return lr_finder

def cnn_training(model_file = None, epochs = 10, batch_size = 64, lr = 3e-4, stage = 1, save_interval = 1):
    global no_model, num_attr, num_category
    global train_df, val_df, test_df
    global category_weight, attribute_weight
    global model, steps, histories
    
    features = ClothingImageFeatures.get_all()
    train_data = list(filter(lambda x: x.evaluation_status == 'train', features))
    val_data = list(filter(lambda x: x.evaluation_status == 'query', features))
    test_data = list(filter(lambda x: x.evaluation_status == 'gallery', features))

    train_df = pd.DataFrame([data.json() for data in train_data])
    val_df = pd.DataFrame([data.json() for data in val_data])
    test_df = pd.DataFrame([data.json() for data in test_data])

    categories = CategoryPrediction.get_all()
    category_labels = [c.name for c in categories]
    num_category = len(category_labels)  # all images belong to 23 category

    attributes = AttributePrediction.get_all()
    attribute_lables = [a.name for a in attributes]
    num_attr = len(attribute_lables)  # each image has 463 attribute 

    category_weight = category_classweight()
    attribute_weight = attribute_classweight()

    histories = []
    steps = 0

    model_source, model_blue = build_model()
    if model_file is not None:
        model = load_modelfile(model_source, model_file)
    else:
        model_lastest = FashionNetModel.get_model_latest()
        if model_lastest is not None:
            model = load_modelfile(model_source, model_lastest.model_file)
        else:
            model = model_source
    model = change_stage(model, lr=lr, stage=stage)
    make_steps(step=epochs, batch_size=batch_size, lr=lr, stage=stage, save_interval=save_interval)