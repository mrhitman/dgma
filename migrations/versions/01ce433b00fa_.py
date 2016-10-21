"""Students migration

Revision ID: 01ce433b00fa
Revises: 7641a3820b40
Create Date: 2016-05-23 08:37:27.956588

"""

# revision identifiers, used by Alembic.
revision = '01ce433b00fa'
down_revision = '7641a3820b40'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('student_discipline_mark',
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
