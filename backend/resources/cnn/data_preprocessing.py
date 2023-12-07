from multiprocessing import Pool
import re
import numpy as np
import pandas as pd
from models.attribute_prediction_model import AttributePrediction
from models.category_prediction_model import CategoryPrediction

from models.clothing_image_features_model import ClothingImageFeatures

def edit_attrimg(index, attr_items):
    """transform the No.index item's attribute_labels of attr_items.
    Transform the label 1 or -1 into the index of attribute labels
    
    Arguments
        index: the index of attr_items
    
    Return
        None
    """
    labels = attr_items['attribute_labels'].loc[index]
    try:
        ll = labels
        labels = re.split(r' +', labels)
    except TypeError as e:
        raise TypeError(f'{e}, {ll}')
#     labels = [str(item[0]) for item in enumerate(labels) if item[1] == '1']
    labels = np.array(labels)
    labels = np.argwhere(labels == '1').flatten().astype(np.str_)
    
    labels = ' '.join(labels)
    return labels

def data_preprocessing():
    LANDMARKS_INSHOP = 'backend/resources/cnn/input/Anno/list_landmarks_inshop.txt'
    EVAL_PARTITION = 'backend/resources/cnn/input/Eval/list_eval_partition.txt'
    ATTR_ITEMS = 'backend/resources/cnn/input/Anno/list_attr_items.txt'
    ATTR_LISTS = 'backend/resources/cnn/input/Anno/list_attr_cloth.txt'
    TRAIN_DF = 'backend/resources/cnn/input/train.csv'
    VAL_DF = 'backend/resources/cnn/input/val.csv'
    TEST_DF = 'backend/resources/cnn/input/test.csv'

    CATEGORY = ['MEN_Denim',
                'MEN_Jackets_Vests',
                'MEN_Pants',
                'MEN_Shirts_Polos',
                'MEN_Shorts',
                'MEN_Suiting',
                'MEN_Sweaters',
                'MEN_Sweatshirts_Hoodies',
                'MEN_Tees_Tanks',
                'WOMEN_Blouses_Shirts',
                'WOMEN_Cardigans',
                'WOMEN_Denim',
                'WOMEN_Dresses',
                'WOMEN_Graphic_Tees',
                'WOMEN_Jackets_Coats',
                'WOMEN_Leggings',
                'WOMEN_Pants',
                'WOMEN_Rompers_Jumpsuits',
                'WOMEN_Shorts',
                'WOMEN_Skirts',
                'WOMEN_Sweaters',
                'WOMEN_Sweatshirts_Hoodies',
                'WOMEN_Tees_Tanks'
            ]

    num_attr = 0
    with open(ATTR_LISTS, 'r') as file:
        # read first line
        num_attr = int(file.readline())
        file.readline() # skip second line

        for i in range(num_attr):
            id = i + 1
            attr_name = file.readline()
            atrr_predit = AttributePrediction.find_by_id(id)
            if atrr_predit:
                atrr_predit.name = attr_name
                atrr_predit.save_to_db()
            else:
                new_attr = AttributePrediction(id = id,name=attr_name)
                new_attr.save_to_db()
               
    for index, category in enumerate(CATEGORY):
        category_name = category.split('_')[1]
        category_gender = category.split('_')[0]
        category = CategoryPrediction.find_by_id(index + 1)
        if category:
            category.name = category_name
            category.gender = category_gender
            category.save_to_db()
        else:
            new_category = CategoryPrediction(id=index + 1, name=category_name, gender=category_gender)
            new_category.save_to_db()

    landmarks_inshop = pd.read_csv(
        LANDMARKS_INSHOP,
        sep=r' +',
        header=1,
        engine='python'
    )

    eval_partition = pd.read_csv(
        EVAL_PARTITION,
        sep=r' +',
        header=1,
        engine='python'
    )

    attr_items = pd.read_csv(
        ATTR_ITEMS,
        sep=r' ',
        header=None,
        skiprows=[0,1],
        names=['item_id', ] + list(range(num_attr)),
        engine='python'
    )

    # merge all attribute into one string
    attr_items['attribute_labels'] = ''
    for i in range(num_attr):
        attr_items['attribute_labels'] += (' ' + attr_items[i].map(str))
    attr_items['attribute_labels'] = attr_items['attribute_labels'].map(lambda x: x[1:])
    attr_items = attr_items.drop(columns=range(num_attr))

    eval_dict = dict([(m, c)for _, m, i, c in eval_partition.to_records()])

    # Tạo danh sách các đối số cho mỗi cuộc gọi của hàm
    args_list = [(index, attr_items) for index in range(len(attr_items))]
    pool = Pool()
    labels = pool.starmap(edit_attrimg, args_list)
    attr_items['attribute_labels'] = labels
    pool.close()
    pool.join()

    df = eval_partition\
        .merge(landmarks_inshop, on='image_name')\
        .merge(attr_items, on='item_id')\
        .drop(columns=['clothes_type', 'variation_type'])\
        .fillna(0)
    
    df['category_label'] = ''

    for index, row in df.iterrows():
        gender = row['image_name'].split('/')[-4]
        category_name = row['image_name'].split('/')[-3]

        category_index = CATEGORY.index(gender + '_' + category_name)
        df.at[index, 'category_label'] = category_index

    created_count = 0
    updated_count = 0
    for index, row in df.iterrows():
        new_image_name = row['image_name'].replace("img", "training")
        clothing_image_features = ClothingImageFeatures.find_by_image_name(new_image_name)
        if clothing_image_features:
            updated_count += 1
            clothing_image_features.item_id = row['item_id']
            clothing_image_features.evaluation_status = row['evaluation_status']
            clothing_image_features.landmark_visibility_1 = row['landmark_visibility_1']
            clothing_image_features.landmark_visibility_2 = row['landmark_visibility_2']
            clothing_image_features.landmark_visibility_3 = row['landmark_visibility_3']
            clothing_image_features.landmark_visibility_4 = row['landmark_visibility_4']
            clothing_image_features.landmark_visibility_5 = row['landmark_visibility_5']
            clothing_image_features.landmark_visibility_6 = row['landmark_visibility_6']
            clothing_image_features.landmark_visibility_7 = row['landmark_visibility_7']
            clothing_image_features.landmark_visibility_8 = row['landmark_visibility_8']
            clothing_image_features.landmark_location_x_1 = row['landmark_location_x_1']
            clothing_image_features.landmark_location_x_2 = row['landmark_location_x_2']
            clothing_image_features.landmark_location_x_3 = row['landmark_location_x_3']
            clothing_image_features.landmark_location_x_4 = row['landmark_location_x_4']
            clothing_image_features.landmark_location_x_5 = row['landmark_location_x_5']
            clothing_image_features.landmark_location_x_6 = row['landmark_location_x_6']
            clothing_image_features.landmark_location_x_7 = row['landmark_location_x_7']
            clothing_image_features.landmark_location_x_8 = row['landmark_location_x_8']
            clothing_image_features.landmark_location_y_1 = row['landmark_location_y_1']
            clothing_image_features.landmark_location_y_2 = row['landmark_location_y_2']
            clothing_image_features.landmark_location_y_3 = row['landmark_location_y_3']
            clothing_image_features.landmark_location_y_4 = row['landmark_location_y_4']
            clothing_image_features.landmark_location_y_5 = row['landmark_location_y_5']
            clothing_image_features.landmark_location_y_6 = row['landmark_location_y_6']
            clothing_image_features.landmark_location_y_7 = row['landmark_location_y_7']
            clothing_image_features.landmark_location_y_8 = row['landmark_location_y_8']
            clothing_image_features.attribute_labels = row['attribute_labels']
            clothing_image_features.category_label = row['category_label']
            clothing_image_features.gender = 1 if new_image_name.split('/')[-4] == "MEN" else 0
            clothing_image_features.save_to_db()
        else:
            created_count += 1
            clothing_image_features = ClothingImageFeatures(
                image_name=new_image_name,
                item_id=row['item_id'],
                evaluation_status=row['evaluation_status'],
                landmark_visibility_1=row['landmark_visibility_1'],
                landmark_visibility_2=row['landmark_visibility_2'],
                landmark_visibility_3=row['landmark_visibility_3'],
                landmark_visibility_4=row['landmark_visibility_4'],
                landmark_visibility_5=row['landmark_visibility_5'],
                landmark_visibility_6=row['landmark_visibility_6'],
                landmark_visibility_7=row['landmark_visibility_7'],
                landmark_visibility_8=row['landmark_visibility_8'],
                landmark_location_x_1=row['landmark_location_x_1'],
                landmark_location_x_2=row['landmark_location_x_2'],
                landmark_location_x_3=row['landmark_location_x_3'],
                landmark_location_x_4=row['landmark_location_x_4'],
                landmark_location_x_5=row['landmark_location_x_5'],
                landmark_location_x_6=row['landmark_location_x_6'],
                landmark_location_x_7=row['landmark_location_x_7'],
                landmark_location_x_8=row['landmark_location_x_8'],
                landmark_location_y_1=row['landmark_location_y_1'],
                landmark_location_y_2=row['landmark_location_y_2'],
                landmark_location_y_3=row['landmark_location_y_3'],
                landmark_location_y_4=row['landmark_location_y_4'],
                landmark_location_y_5=row['landmark_location_y_5'],
                landmark_location_y_6=row['landmark_location_y_6'],
                landmark_location_y_7=row['landmark_location_y_7'],
                landmark_location_y_8=row['landmark_location_y_8'],
                box_top_left_x=0,
                box_top_left_y=0,
                box_bottom_right_x=0,
                box_bottom_right_y=0,
                attribute_labels=row['attribute_labels'],
                category_label=row['category_label']
            )
           
            clothing_image_features.save_to_db()

    return {
        "created_count": created_count,
        "updated_count": updated_count
    }
            
def find_by_id(object_list, id):
    matches = [obj for obj in object_list if obj.id == id]
    return matches[0] if matches else None

def get_preprocessing_info():
    cif = ClothingImageFeatures.get_all()
    attribute_labels = AttributePrediction.get_all()
    category_labels = CategoryPrediction.get_all()
    total_count = len(cif)
    train_count = len([c for c in cif if c.evaluation_status == 'train'])
    val_count = len([c for c in cif if c.evaluation_status == 'query'])
    test_count = len([c for c in cif if c.evaluation_status == 'gallery'])
    attributes = {}
    for c in cif:
        for a in c.attribute_labels.split(' '):
            if a == '':
                continue
            attribute_label = find_by_id(attribute_labels, int(a))
            if attribute_label not in attributes:
                attributes[attribute_label] = 0
            attributes[attribute_label] += 1

    labels = {}
    for c in cif:
        category_label = find_by_id(category_labels, int(c.category_label))
        if category_label not in labels:
            labels[category_label] = 0
        labels[category_label] += 1

    gender = {
        "MEN": 0,
        "WOMEN": 0
    }

    for c in cif:
        if c.gender == 1:
            gender['MEN'] += 1
        else:
            gender['WOMEN'] += 1

    return {
        "total_count": total_count,
        "train_count": train_count,
        "val_count": val_count,
        "test_count": test_count,
        "attributes": attributes,
        "labels": labels,
        "gender": gender
    }