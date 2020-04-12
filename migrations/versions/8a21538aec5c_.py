"""empty message

Revision ID: 8a21538aec5c
Revises: 3f1c6e647755
Create Date: 2020-04-10 14:45:33.843056

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8a21538aec5c'
down_revision = '3f1c6e647755'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'roles', 'sys_user', ['user_id'], ['id'])
    op.drop_column('sys_user', 'role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sys_user', sa.Column('role', mysql.VARCHAR(length=64), nullable=True))
    op.drop_constraint(None, 'roles', type_='foreignkey')
    op.drop_column('roles', 'user_id')
    # ### end Alembic commands ###