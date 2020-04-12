"""empty message

Revision ID: b7da98bd0c32
Revises: 8a21538aec5c
Create Date: 2020-04-12 18:41:14.320524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7da98bd0c32'
down_revision = '8a21538aec5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('industry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('info', sa.Text(length=256), nullable=True),
    sa.Column('register_capital', sa.String(length=20), nullable=True),
    sa.Column('industry_type', sa.Integer(), nullable=True),
    sa.Column('contact_person', sa.String(length=128), nullable=True),
    sa.Column('contacts', sa.String(length=128), nullable=True),
    sa.Column('recent_situation', sa.Text(length=256), nullable=True),
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['industry_type'], ['industry.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(length=256), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    op.drop_table('company')
    op.drop_table('industry')
    # ### end Alembic commands ###
