"""add load page work types

Revision ID: 7641a3820b40
Revises: 639cbad12905
Create Date: 2016-05-19 15:50:02.495354

"""

# revision identifiers, used by Alembic.
revision = '7641a3820b40'
down_revision = '639cbad12905'

from alembic import op
import sqlalchemy as sa


def upgrade():
    conn = op.get_bind()
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (1, 'Читання лекцій, до 50 год.', 'За звітній період', 1, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (2, 'Читання лекцій, до 100 год.', 'За звітній період', 2, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (3, 'Читання лекцій, до 150 год.', 'За звітній період', 3, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (4, 'Читання лекцій, більше 150 год.', 'За звітній період', 4, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (5, 'Робота опонентом на захистах дисертацій', 'За звітній період', 1, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (6, 'Наявність почесних звань, нагород: почесні знаки МОНУ', 'За звітній період', 5, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (7, 'Наявність почесних звань, нагород: відмінник освіти України, грамота МОНУ', 'За звітній період', 4, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (8, 'Наявність почесних звань, нагород: заслужений професор ДДМА', 'За звітній період', 6, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (9, 'Наявність почесних звань, нагород: почесний професор ДДМА', 'За звітній період', 6, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (10, 'Наявність почесних звань, нагород: заслужений викладач ДДМА', 'За звітній період', 6, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (11, 'Наявність почесних звань, нагород: заслужений працівник ДДМА', 'За звітній період', 6, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (12, 'Наявність почесних звань, нагород: почесний доктор інших ВНЗ', 'За звітній період', 6, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (13, 'Наявність почесних звань, нагород: почесні звання закордонних орг-й', 'За звітній період', 6, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (14, 'Наявність почесних звань, нагород: кращий працівник ДДМА: декан, зав. кафедри, викладач тощо', 'За звітній період', 2, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (15, 'за кращу методрозробку: 1 місце', 'Кіл-ть балів поділити на кількість авторів', 4, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (16, 'за кращу методрозробку: 2 місце', 'Кіл-ть балів поділити на кількість авторів', 3, 1);''')
    conn.execute('''INSERT INTO "main"."load_page_work_types" VALUES (17, 'за кращу методрозробку: 3 місце', 'Кіл-ть балів поділити на кількість авторів', 2, 1);''')


def downgrade():
    pass
