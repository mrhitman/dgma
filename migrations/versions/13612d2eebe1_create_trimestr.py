""" create trimester

Revision ID: 13612d2eebe1
Revises: 8e5882db4d85
Create Date: 2016-10-25 18:08:56.026679

"""

# revision identifiers, used by Alembic.
revision = '13612d2eebe1'
down_revision = '8e5882db4d85'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('trimester',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('num', sa.Integer(), nullable=True),
        sa.Column('start_date', sa.Date(), nullable=True),
        sa.Column('end_date', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('trimester')
