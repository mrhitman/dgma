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
from sqlalchemy import table, column
from sqlalchemy import String, Integer

def upgrade():
    conn = op.get_bind()
    load_page_subtype = table('load_page_subtype',
        column('id', Integer),
        column('name', String)
    )
    op.bulk_insert(load_page_subtype,
        [
            {'id': 1,'name': 'Учебно-методическая работа'},
            {'id': 2,'name': 'Организационно-методическая работа'},
            {'id': 3,'name': 'Научная работа'},
            {'id': 4,'name': 'Воспитательная работа'},
            {'id': 5,'name': 'Другие виды работ'},
        ]
    )
    load_page_work_type = table('load_page_work_type',
        column('id', Integer),
        column('name', String),
        column('info', String),
        column('mark', Integer),
        column('subtype_id', Integer),
    )
    op.bulk_insert(load_page_work_type,
        [
            {'id': 1,'name': 'Читання лекцій, до 50 год.', 'info': 'За звітній період', 'mark': 1, 'subtype_id': 1},
            {'id': 2,'name': 'Читання лекцій, до 100 год.', 'info': 'За звітній період', 'mark': 2, 'subtype_id': 1},
            {'id': 3,'name': 'Читання лекцій, до 150 год.', 'info': 'За звітній період', 'mark': 3, 'subtype_id': 1},
            {'id': 4,'name': 'Читання лекцій, більше 150 год.', 'info': 'За звітній період', 'mark': 4, 'subtype_id': 1},
            {'id': 5,'name': 'Робота опонентом на захистах дисертацій', 'info': 'За звітній період', 'mark': 1, 'subtype_id': 1},
            {'id': 6,'name': 'Наявність почесних звань, нагород: почесні знаки МОНУ', 'info': 'За звітній період', 'mark': 5, 'subtype_id': 1},
            {'id': 7,'name': 'Наявність почесних звань, нагород: відмінник освіти України, грамота МОНУ', 'info': 'За звітній період', 'mark': 4, 'subtype_id': 1},
            {'id': 8,'name': 'Наявність почесних звань, нагород: заслужений професор ДДМА', 'info': 'За звітній період', 'mark': 6, 'subtype_id': 1},
            {'id': 9,'name': 'Наявність почесних звань, нагород: почесний професор ДДМА', 'info': 'За звітній період', 'mark': 6, 'subtype_id': 1},
            {'id': 10,'name': 'Наявність почесних звань, нагород: заслужений викладач ДДМА', 'info': 'За звітній період', 'mark': 6, 'subtype_id': 1},
            {'id': 11,'name': 'Наявність почесних звань, нагород: заслужений працівник ДДМА', 'info': 'За звітній період', 'mark': 6, 'subtype_id': 1},
            {'id': 12,'name': 'Наявність почесних звань, нагород: почесний доктор інших ВНЗ', 'info': 'За звітній період', 'mark': 6, 'subtype_id': 1},
            {'id': 13,'name': 'Наявність почесних звань, нагород: почесні звання закордонних орг-й', 'info': 'За звітній період', 'mark': 6, 'subtype_id': 1},
            {'id': 14,'name': 'Наявність почесних звань, нагород: кращий працівник ДДМА: декан, зав. кафедри, викладач тощо', 'info': 'За звітній період', 'mark': 2, 'subtype_id': 1},
            {'id': 15,'name': 'за кращу методрозробку: 1 місце', 'info': 'Кіл-ть балів поділити на кількість авторів', 'mark': 4, 'subtype_id': 1},
            {'id': 16,'name': 'за кращу методрозробку: 2 місце', 'info': 'Кіл-ть балів поділити на кількість авторів', 'mark': 3, 'subtype_id': 1},
            {'id': 17,'name': 'за кращу методрозробку: 3 місце', 'info': 'Кіл-ть балів поділити на кількість авторів', 'mark': 2, 'subtype_id': 1},
        ]
    )



def downgrade():
    pass
