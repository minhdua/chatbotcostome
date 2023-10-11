"""update table name and field name for table

Revision ID: 1fb74b569aa0
Revises: ee530764064e
Create Date: 2023-09-16 15:06:22.957427

"""
import pdb

import pandas as pd
import sqlalchemy as sa
from alembic import op
from models.clothing_image_features_model import ClothingImageFeatures

# revision identifiers, used by Alembic.
revision = '1fb74b569aa1'
down_revision = '1fb74b569aa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    file_path = 'F:\\chatbotsupportcostume-main\\migrations\\versions\\train.csv'
    # đọc train.csv
    df = pd.read_csv(
                    file_path,
                    sep=r',',
                    header=0,
                    engine='python'
                )
    for index, row in df.iterrows():
        data = ClothingImageFeatures(
            image_name=row['image_name'],
            item_id=row['item_id'],
            evaluation_status=row['evaluation_status'],
            landmark_visibility_1=row['landmark_visibility_1'],
            landmark_location_x_1=row['landmark_location_x_1'],
            landmark_location_y_1=row['landmark_location_y_1'],
            landmark_visibility_2=row['landmark_visibility_2'],
            landmark_location_x_2=row['landmark_location_x_2'],
            landmark_location_y_2=row['landmark_location_y_2'],
            landmark_visibility_3=row['landmark_visibility_3'],
            landmark_location_x_3=row['landmark_location_x_3'],
            landmark_location_y_3=row['landmark_location_y_3'],
            landmark_visibility_4=row['landmark_visibility_4'],
            landmark_location_x_4=row['landmark_location_x_4'],
            landmark_location_y_4=row['landmark_location_y_4'],
            landmark_visibility_5=row['landmark_visibility_5'],
            landmark_location_x_5=row['landmark_location_x_5'],
            landmark_location_y_5=row['landmark_location_y_5'],
            landmark_visibility_6=row['landmark_visibility_6'],
            landmark_location_x_6=row['landmark_location_x_6'],
            landmark_location_y_6=row['landmark_location_y_6'],
            landmark_visibility_7=row['landmark_visibility_7'],
            landmark_location_x_7=row['landmark_location_x_7'],
            landmark_location_y_7=row['landmark_location_y_7'],
            landmark_visibility_8=row['landmark_visibility_8'],
            landmark_location_x_8=row['landmark_location_x_8'],
            landmark_location_y_8=row['landmark_location_y_8'],
            attribute_labels=row['attribute_labels'],
            category_label=row['category_label'],
            gender=row['gender']
        )
        data.save_to_db()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clothing_image_features')
    # ### end Alembic commands ###
