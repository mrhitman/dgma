"""empty message

Revision ID: f7847e981e2d
Revises: 17325760d604
Create Date: 2016-06-06 20:07:34.695557
0
"""

# revision identifiers, used by Alembic.
revision = 'f7847e981e2d'
down_revision = '17325760d604'

from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer


def upgrade():
    conn = op.get_bind()
    load_page_type = table('load_page_type', 
        column('name', String)
    )
    op.bulk_insert(load_page_type, 
        [
            {'name': 'Учебно-методическая работа'},
            {'name': 'Организационно-методическая работа'},
            {'name': 'Научная работа'},
            {'name': 'Воспитательная работа'},
            {'name': 'Другие виды работ'},
        ]
    )


def downgrade():
    pass
