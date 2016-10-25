""" add mark/schedule

Revision ID: 26507d5ea2db
Revises: f7847e981e2d
Create Date: 2016-10-21 16:50:35.691197

"""

# revision identifiers, used by Alembic.
revision = '26507d5ea2db'
down_revision = 'f7847e981e2d'

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('student_subject_mark',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('student_id', sa.Integer(), nullable=True),
        sa.Column('subject_id', sa.Integer(), nullable=True),
        sa.Column('mark', sa.Integer(), nullable=True),
        sa.Column('date', sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
        sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_schedule',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=True),
        sa.Column('subject_id', sa.Integer(), nullable=True),
        sa.Column('day_number', sa.Integer(), nullable=True),
        sa.Column('lesson_number', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('student_subject_mark')
    op.drop_table('student_schedule')
