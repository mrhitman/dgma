"""add load_page root

Revision ID: 58fbf981e5b0
Revises: fdd6201c5c3e
Create Date: 2016-06-01 11:59:35.368604

"""

# revision identifiers, used by Alembic.
revision = '58fbf981e5b0'
down_revision = 'fdd6201c5c3e'
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('load_page_root',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('start_period', sa.DateTime(), nullable=True),
    sa.Column('end_period', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('load_page_root')
