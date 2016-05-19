"""Add facilities

Revision ID: acbb697476a1
Revises: de05d71447de
Create Date: 2016-05-19 15:28:46.571584

"""

# revision identifiers, used by Alembic.
revision = 'acbb697476a1'
down_revision = 'de05d71447de'

from alembic import op


def upgrade():
    conn = op.get_bind()
    conn.execute('''INSERT INTO "main"."facility" VALUES (1, 'Факультет автоматизации машиностроения и информационных технологий', 'ФАМИТ', 'facility/famit.jpg');''')
    conn.execute('''INSERT INTO "main"."facility" VALUES (2, 'Факультет машиностроения', 'ФМ', 'facility/finansi.jpg');''')
    conn.execute('''INSERT INTO "main"."facility" VALUES (3, 'Факультет интегрированных технологий и оборудования', 'ФИТО', 'facility/fito.jpg');''')
    conn.execute('''INSERT INTO "main"."facility" VALUES (4, 'Факультет экономики и менеджмента', 'ФЭМ', 'facility/fm.jpg');''')


def downgrade():
    pass
