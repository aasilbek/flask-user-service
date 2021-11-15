"""add language to posts

Revision ID: 78741bfdf629
Revises: 558f73a2f5e4
Create Date: 2021-09-11 12:21:43.171950

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '78741bfdf629'
down_revision = '558f73a2f5e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
