"""add disciplines

Revision ID: 17325760d604
Revises: 58fbf981e5b0
Create Date: 2016-06-06 14:19:09.332770

"""

# revision identifiers, used by Alembic.
revision = '17325760d604'
down_revision = '58fbf981e5b0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('discipline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('cathedra_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cathedra_id'], ['cathedra.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_mark',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('discipline_id', sa.Integer(), nullable=True),
    sa.Column('mark', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.ForeignKeyConstraint(['discipline_id'], ['discipline.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('discipline')
    op.drop_table('student_mark')