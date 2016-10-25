"""Add facilities

Revision ID: acbb697476a1
Revises: de05d71447de
Create Date: 2016-05-19 15:28:46.571584

"""

# revision identifiers, used by Alembic.
revision = 'acbb697476a1'
down_revision = 'de05d71447de'

from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer


def upgrade():
    conn = op.get_bind()
    facilities = table('facility', 
        column('id', Integer),
        column('name', String),
        column('short_name', String),
        column('image', String),
    )
    op.bulk_insert(facilities, 
        [
            {'id': 1,'name': 'Факультет автоматизации машиностроения и информационных технологий', 'short_name': 'ФАМИТ', 'image': 'facility/famit.jpg'},
            {'id': 2,'name': 'Факультет машиностроения', 'short_name': 'ФМ', 'image': 'facility/finansi.jpg'},
            {'id': 3,'name': 'Факультет интегрированных технологий и оборудования', 'short_name': 'ФИТО', 'image': 'facility/fito.jpg'},
            {'id': 4,'name': 'Факультет экономики и менеджмента', 'short_name': 'ФЭМ', 'image': 'facility/fm.jpg'},
        ]
    )    


def downgrade():
    pass
