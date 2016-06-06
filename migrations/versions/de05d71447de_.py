"""Init database

Revision ID: de05d71447de
Revises: None
Create Date: 2016-05-19 15:27:28.720687

"""

# revision identifiers, used by Alembic.
revision = 'de05d71447de'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facility',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('short_name', sa.String(length=15), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('load_page_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('load_page_work_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=True),
    sa.Column('info', sa.String(length=30), nullable=True),
    sa.Column('mark', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['load_page_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('second_name', sa.String(length=50), nullable=True),
    sa.Column('middle_name', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('cathedra',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('short_name', sa.String(length=15), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('facility_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['facility_id'], ['facility.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('load_page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('work_type_id', sa.Integer(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('mark', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('load_page_root_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['work_type_id'], ['load_page_work_types.id'], ),
    sa.ForeignKeyConstraint(['load_page_root_id'], ['load_page_root.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('cathedra_id', sa.Integer(), nullable=True),
    sa.Column('post', sa.String(length=50), nullable=True),
    sa.Column('academic_degree', sa.String(length=50), nullable=True),
    sa.Column('rank', sa.String(length=50), nullable=True),
    sa.Column('photo', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['cathedra_id'], ['cathedra.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('professor')
    op.drop_table('load_page')
    op.drop_table('cathedra')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('load_page_work_types')
    op.drop_table('facility')
    ### end Alembic commands ###
