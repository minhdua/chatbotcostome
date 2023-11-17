import os

from app_factory import app
from app_factory import db
from models.base_mixin import BaseMixin
from models.enum import Gender, Perspective


class ClothingImageFeatures(db.Model, BaseMixin):
    __tablename__ = "clothing_image_features"

    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(255), nullable=False)
    item_id = db.Column(db.String, nullable=False)
    evaluation_status = db.Column(db.String(255), nullable=False)
    
    # Columns for landmark visibility (landmark_visibility_1 to landmark_visibility_8)
    landmark_visibility_1 = db.Column(db.Integer, default=0)
    landmark_visibility_2 = db.Column(db.Integer, default=0)
    landmark_visibility_3 = db.Column(db.Integer, default=0)
    landmark_visibility_4 = db.Column(db.Integer, default=0)
    landmark_visibility_5 = db.Column(db.Integer, default=0)
    landmark_visibility_6 = db.Column(db.Integer, default=0)
    landmark_visibility_7 = db.Column(db.Integer, default=0)
    landmark_visibility_8 = db.Column(db.Integer, default=0)
    
    # Columns for landmark locations (landmark_location_x_1 to landmark_location_x_8)
    landmark_location_x_1 = db.Column(db.Float, default=0.0)
    landmark_location_x_2 = db.Column(db.Float, default=0.0)
    landmark_location_x_3 = db.Column(db.Float, default=0.0)
    landmark_location_x_4 = db.Column(db.Float, default=0.0)
    landmark_location_x_5 = db.Column(db.Float, default=0.0)
    landmark_location_x_6 = db.Column(db.Float, default=0.0)
    landmark_location_x_7 = db.Column(db.Float, default=0.0)
    landmark_location_x_8 = db.Column(db.Float, default=0.0)
    
    # Columns for landmark locations (landmark_location_y_1 to landmark_location_y_8)
    landmark_location_y_1 = db.Column(db.Float, default=0.0)
    landmark_location_y_2 = db.Column(db.Float, default=0.0)
    landmark_location_y_3 = db.Column(db.Float, default=0.0)
    landmark_location_y_4 = db.Column(db.Float, default=0.0)
    landmark_location_y_5 = db.Column(db.Float, default=0.0)
    landmark_location_y_6 = db.Column(db.Float, default=0.0)
    landmark_location_y_7 = db.Column(db.Float, default=0.0)
    landmark_location_y_8 = db.Column(db.Float, default=0.0)

    box_top_left_x = db.Column(db.Float, default=0.0)
    box_top_left_y = db.Column(db.Float, default=0.0)
    box_bottom_right_x = db.Column(db.Float, default=0.0)
    box_bottom_right_y = db.Column(db.Float, default=0.0)
    
    attribute_labels = db.Column(db.String(255), nullable=False)
    category_label = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Integer, default=0)

    def __init__(self, image_name, item_id, evaluation_status,
                 landmark_visibility_1, landmark_visibility_2, landmark_visibility_3, landmark_visibility_4,
                 landmark_visibility_5, landmark_visibility_6, landmark_visibility_7, landmark_visibility_8,
                 landmark_location_x_1, landmark_location_x_2, landmark_location_x_3, landmark_location_x_4,
                 landmark_location_x_5, landmark_location_x_6, landmark_location_x_7, landmark_location_x_8,
                 landmark_location_y_1, landmark_location_y_2, landmark_location_y_3, landmark_location_y_4,
                 landmark_location_y_5, landmark_location_y_6, landmark_location_y_7, landmark_location_y_8,
                    box_top_left_x, box_top_left_y, box_bottom_right_x, box_bottom_right_y,
                 attribute_labels, category_label, gender=0):
        self.image_name = image_name
        self.item_id = item_id
        self.evaluation_status = evaluation_status
        self.landmark_visibility_1 = landmark_visibility_1
        self.landmark_visibility_2 = landmark_visibility_2
        self.landmark_visibility_3 = landmark_visibility_3
        self.landmark_visibility_4 = landmark_visibility_4
        self.landmark_visibility_5 = landmark_visibility_5
        self.landmark_visibility_6 = landmark_visibility_6
        self.landmark_visibility_7 = landmark_visibility_7
        self.landmark_visibility_8 = landmark_visibility_8
        self.landmark_location_x_1 = landmark_location_x_1
        self.landmark_location_x_2 = landmark_location_x_2
        self.landmark_location_x_3 = landmark_location_x_3
        self.landmark_location_x_4 = landmark_location_x_4
        self.landmark_location_x_5 = landmark_location_x_5
        self.landmark_location_x_6 = landmark_location_x_6
        self.landmark_location_x_7 = landmark_location_x_7
        self.landmark_location_x_8 = landmark_location_x_8
        self.landmark_location_y_1 = landmark_location_y_1
        self.landmark_location_y_2 = landmark_location_y_2
        self.landmark_location_y_3 = landmark_location_y_3
        self.landmark_location_y_4 = landmark_location_y_4
        self.landmark_location_y_5 = landmark_location_y_5
        self.landmark_location_y_6 = landmark_location_y_6
        self.landmark_location_y_7 = landmark_location_y_7
        self.landmark_location_y_8 = landmark_location_y_8
        self.box_top_left_x = box_top_left_x
        self.box_top_left_y = box_top_left_y
        self.box_bottom_right_x = box_bottom_right_x
        self.box_bottom_right_y = box_bottom_right_y
        self.attribute_labels = attribute_labels
        self.category_label = category_label
        self.gender = gender

    def __repr__(self):
        return f"ClothingImageFeatures(id={self.id}, image_name={self.image_name}, item_id={self.item_id}, evaluation_status={self.evaluation_status}, ...)"

    def json(self):
        return {
            "id": self.id,
            "image_name": self.image_name,
            "item_id": self.item_id,
            "evaluation_status": self.evaluation_status,
            "landmark_visibility_1": self.landmark_visibility_1 or 0.,
            "landmark_visibility_2": self.landmark_visibility_2 or 0.,
            "landmark_visibility_3": self.landmark_visibility_3 or 0.,
            "landmark_visibility_4": self.landmark_visibility_4 or 0.,
            "landmark_visibility_5": self.landmark_visibility_5 or 0.,
            "landmark_visibility_6": self.landmark_visibility_6 or 0.,
            "landmark_visibility_7": self.landmark_visibility_7 or 0.,
            "landmark_visibility_8": self.landmark_visibility_8 or 0.,
            "landmark_location_x_1": self.landmark_location_x_1 or 0.,
            "landmark_location_x_2": self.landmark_location_x_2 or 0.,
            "landmark_location_x_3": self.landmark_location_x_3 or 0.,
            "landmark_location_x_4": self.landmark_location_x_4 or 0,
            "landmark_location_x_5": self.landmark_location_x_5 or 0,
            "landmark_location_x_6": self.landmark_location_x_6 or 0.,
            "landmark_location_x_7": self.landmark_location_x_7 or 0.,
            "landmark_location_x_8": self.landmark_location_x_8 or 0,
            "landmark_location_y_1": self.landmark_location_y_1 or 0.,
            "landmark_location_y_2": self.landmark_location_y_2 or 0.,
            "landmark_location_y_3": self.landmark_location_y_3 or 0.,
            "landmark_location_y_4": self.landmark_location_y_4 or 0.,
            "landmark_location_y_5": self.landmark_location_y_5 or 0.,
            "landmark_location_y_6": self.landmark_location_y_6 or 0.,
            "landmark_location_y_7": self.landmark_location_y_7 or 0.,
            "landmark_location_y_8": self.landmark_location_y_8 or 0.,
            "box_top_left_x": self.box_top_left_x or 0.,
            "box_top_left_y": self.box_top_left_y or 0.,
            "box_bottom_right_x": self.box_bottom_right_x or 0.,
            "box_bottom_right_y": self.box_bottom_right_y or 0.,
            "attribute_labels": self.attribute_labels,
            "category_label": self.category_label,
            "gender": self.gender or 0
        }
    
    def get_new_id():
        # format id_00000030

        # group by item_id after get item_id max remove prefix id_ convert to int and add 1
        max_id = ClothingImageFeatures.query.with_entities(ClothingImageFeatures.item_id).order_by(ClothingImageFeatures.item_id.desc()).first()
        if max_id is None:
            return "id_00000001"
        else:
            max_id = max_id.item_id
            max_id = int(max_id[3:])
            new_id = max_id + 1
            new_id = str(new_id).zfill(8)
            new_id = "id_" + new_id
            return new_id

    def get_feature_group_by_item_id():
        # Truy vấn dữ liệu từ cơ sở dữ liệu
        result = (
            ClothingImageFeatures.query
            .with_entities(
                ClothingImageFeatures.item_id,
                ClothingImageFeatures.attribute_labels,
                ClothingImageFeatures.category_label,
                ClothingImageFeatures.gender,
                ClothingImageFeatures.image_name,
                ClothingImageFeatures.evaluation_status,
                ClothingImageFeatures.landmark_visibility_1,
                ClothingImageFeatures.landmark_visibility_2,
                ClothingImageFeatures.landmark_visibility_3,
                ClothingImageFeatures.landmark_visibility_4,
                ClothingImageFeatures.landmark_visibility_5,
                ClothingImageFeatures.landmark_visibility_6,
                ClothingImageFeatures.landmark_visibility_7,
                ClothingImageFeatures.landmark_visibility_8,
                ClothingImageFeatures.landmark_location_x_1,
                ClothingImageFeatures.landmark_location_x_2,
                ClothingImageFeatures.landmark_location_x_3,
                ClothingImageFeatures.landmark_location_x_4,
                ClothingImageFeatures.landmark_location_x_5,
                ClothingImageFeatures.landmark_location_x_6,
                ClothingImageFeatures.landmark_location_x_7,
                ClothingImageFeatures.landmark_location_x_8,
                ClothingImageFeatures.landmark_location_y_1,
                ClothingImageFeatures.landmark_location_y_2,
                ClothingImageFeatures.landmark_location_y_3,
                ClothingImageFeatures.landmark_location_y_4,
                ClothingImageFeatures.landmark_location_y_5,
                ClothingImageFeatures.landmark_location_y_6,
                ClothingImageFeatures.landmark_location_y_7,
                ClothingImageFeatures.landmark_location_y_8,
                ClothingImageFeatures.box_top_left_x,
                ClothingImageFeatures.box_top_left_y,
                ClothingImageFeatures.box_bottom_right_x,
                ClothingImageFeatures.box_bottom_right_y,
            )
            # .filter_by(...)  
            .all()
        )

        # Biến đổi kết quả thành định dạng mong muốn
        formatted_result = []

        for row in result:
            item_id, attribute_labels, category_label, gender, image_name, evaluation_status, \
            landmark_visibility_1, landmark_visibility_2, landmark_visibility_3, landmark_visibility_4, \
            landmark_visibility_5, landmark_visibility_6, landmark_visibility_7, landmark_visibility_8, \
            landmark_location_x_1, landmark_location_x_2, landmark_location_x_3, landmark_location_x_4, \
            landmark_location_x_5, landmark_location_x_6, landmark_location_x_7, landmark_location_x_8, \
            landmark_location_y_1, landmark_location_y_2, landmark_location_y_3, landmark_location_y_4, \
            landmark_location_y_5, landmark_location_y_6, landmark_location_y_7, landmark_location_y_8 \
            , box_top_left_x, box_top_left_y, box_bottom_right_x, box_bottom_right_y = row

            image_host = app.config['IMAGE_DEFAULT_URL']
            gender = Gender.from_value(gender)
            # split / get -1 remove extension file, after split _ get first for clothing remain for perspective
            file_name = image_name.split("/")[-1]
            # remove extension 
            clothing_perspective = file_name.split(".")[0]
            # split _ get first for clothing
            clothing = clothing_perspective.split("_")[0]
            # split _ get last for perspective
            perspective = '_'.join(clothing_perspective.split("_")[1:])
            perspective = Perspective.from_value(perspective)
            # Xử lý và biến đổi dữ liệu thành định dạng mong muốn
            # ...

            formatted_result.append({
                'item_id': item_id,
                'attribute_labels': attribute_labels,
                'category_label': category_label,
                'gender': gender.json(),
                'clothings': [
                    {
                        'name': clothing,
                        'items': [
                            {
                                'image_url': os.path.join(image_host, image_name),
                                'perspective': perspective.json(),
                                'box': {
                                    'top_left': {'x': box_top_left_x, 'y': box_top_left_y},
                                    'bottom_right': {'x': box_bottom_right_x, 'y': box_bottom_right_y}
                                },
                                'land_marks': [
                                    {
                                        'status': status,
                                        'clothing_parts': clothing_parts,
                                        'x': x,
                                        'y': y
                                    }
                                    for status, clothing_parts, x, y in 
                                    [(landmark_visibility_1, 1 , landmark_location_x_1, landmark_location_y_1),
                                    (landmark_visibility_2, 2 , landmark_location_x_2, landmark_location_y_2),
                                    (landmark_visibility_3, 3 , landmark_location_x_3, landmark_location_y_3),
                                    (landmark_visibility_4, 4 , landmark_location_x_4, landmark_location_y_4),
                                    (landmark_visibility_5, 5 , landmark_location_x_5, landmark_location_y_5),
                                    (landmark_visibility_6, 6 , landmark_location_x_6, landmark_location_y_6),
                                    (landmark_visibility_7, 7 , landmark_location_x_7, landmark_location_y_7),
                                    (landmark_visibility_8, 8 , landmark_location_x_8, landmark_location_y_8)]
                                ]
                            }
                        ]
                    }
                ]
            })

        return formatted_result

