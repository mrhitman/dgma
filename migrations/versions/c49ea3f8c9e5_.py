"""Subjects added

Revision ID: c49ea3f8c9e5
Revises: 01ce433b00fa
Create Date: 2016-10-21 15:30:36.332298

"""

# revision identifiers, used by Alembic.
revision = 'c49ea3f8c9e5'
down_revision = '01ce433b00fa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    conn = op.get_bind()
    conn.execute('''INSERT INTO "main"."discipline" VALUES (1, 'Высшая математика', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (2, 'Дискретная математика', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (3, 'Физика', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (4, 'Украинский язык', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (5, 'Английский язык', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (6, 'Численные методы', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (7, 'Теория алгоритмов', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (8, 'Компьютерные сети', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (9, 'Сопротивление материалов', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (10, 'Физкультура', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (11, 'Черчение', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (12, 'Философия', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (13, 'История', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (14, 'Психолигия', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (15, 'Экономика', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (16, 'Менеджмент', 1);''')
    conn.execute('''INSERT INTO "main"."discipline" VALUES (17, 'Учет и аудит', 1);''')


def downgrade():
    pass
