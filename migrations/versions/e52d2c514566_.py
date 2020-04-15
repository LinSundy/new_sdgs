"""empty message

Revision ID: e52d2c514566
Revises: e9174ceef5e8
Create Date: 2020-04-15 08:27:23.617520

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e52d2c514566'
down_revision = 'e9174ceef5e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('company', 'url',
               existing_type=mysql.VARCHAR(length=256),
               type_=sa.String(length=1000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('company', 'url',
               existing_type=sa.String(length=1000),
               type_=mysql.VARCHAR(length=256),
               existing_nullable=True)
    # ### end Alembic commands ###