"""disciplines

Revision ID: 8e5882db4d85
Revises: 26507d5ea2db
Create Date: 2016-10-21 16:51:08.954319

"""

# revision identifiers, used by Alembic.
revision = '8e5882db4d85'
down_revision = '26507d5ea2db'

from alembic import op
import sqlalchemy as sa


def upgrade():
    conn = op.get_bind()
    conn.execute('''INSERT INTO "main"."discipline" VALUES (1, 'Высшая математика', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (2, 'Дискретная математика', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (3, 'Физика', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (4, 'Украинский язык', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (5, 'Английский язык', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (6, 'Численные методы', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (7, 'Теория алгоритмов', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (8, 'Компьютерные сети', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (9, 'Сопротивление материалов', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (10, 'Физкультура', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (11, 'Черчение', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (12, 'Философия', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (13, 'История', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (14, 'Психолигия', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (15, 'Экономика', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (16, 'Менеджмент', 1, 50);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (17, 'Учет и аудит', 1, 50);''')


def downgrade():
    pass
