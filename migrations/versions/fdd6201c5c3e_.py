"""Add tables students

Revision ID: fdd6201c5c3e
Revises: 7641a3820b40
Create Date: 2016-05-23 12:14:05.812119

"""

# revision identifiers, used by Alembic.
revision = 'fdd6201c5c3e'
down_revision = '7641a3820b40'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('photo', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('cathedra_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cathedra_id'], ['cathedra.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('student')
    op.drop_table('group')
