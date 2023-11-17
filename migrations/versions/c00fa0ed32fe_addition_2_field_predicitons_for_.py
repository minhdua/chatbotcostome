"""addition 2 field predicitons for products

Revision ID: c00fa0ed32fe
Revises: 77ceca2c8d8c
Create Date: 2023-09-14 23:10:55.777218

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c00fa0ed32fe'
down_revision = '77ceca2c8d8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_attributes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('attribute_predict_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['attribute_predict_id'], ['attribute_prediction.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('category_predict_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_predict_id'], ['category_prediction.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('attribute_prediction', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    with op.batch_alter_table('category_prediction', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category_prediction', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    with op.batch_alter_table('attribute_prediction', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    op.drop_table('product_categories')
    op.drop_table('product_attributes')
    # ### end Alembic commands ###