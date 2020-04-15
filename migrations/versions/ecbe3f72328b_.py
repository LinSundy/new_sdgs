"""empty message

Revision ID: ecbe3f72328b
Revises: e52d2c514566
Create Date: 2020-04-15 12:17:10.421783

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ecbe3f72328b'
down_revision = 'e52d2c514566'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    op.alter_column('sys_user', 'password',
               existing_type=mysql.VARCHAR(length=256),
               server_default=None,
               existing_nullable=False)
    op.alter_column('sys_user', 'username',
               existing_type=mysql.VARCHAR(length=128),
               server_default=None,
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sys_user', 'username',
               existing_type=mysql.VARCHAR(length=128),
               server_default=sa.text("''"),
               existing_nullable=False)
    op.alter_column('sys_user', 'password',
               existing_type=mysql.VARCHAR(length=256),
               server_default=sa.text("''"),
               existing_nullable=False)
    op.create_table('test',
    sa.Column('id', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=32), nullable=True),
    sa.Column('level', mysql.INTEGER(display_width=10), autoincrement=False, nullable=True),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###