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
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

def upgrade():
    conn = op.get_bind()
    subject = table('subject',
        column('id', Integer),
        column('name', String),
        column('cathedra_id', Integer),
        column('credits', Integer)
    )
    op.bulk_insert(subject,
        [
            {'id': 1,'name': 'Высшая математика','cathedra_id': 10, 'credits': 50},
            {'id': 2,'name': 'Дискретная математика','cathedra_id': 10, 'credits': 70},
            {'id': 3,'name': 'Физика','cathedra_id': 1, 'credits': 50},
            {'id': 4,'name': 'Украинский язык','cathedra_id': 28, 'credits': 100},
            {'id': 5,'name': 'Английский язык','cathedra_id': 27, 'credits': 150},
            {'id': 6,'name': 'Численные методы','cathedra_id': 4, 'credits': 80},
            {'id': 7,'name': 'Алгоритмы и структуры данных','cathedra_id': 2, 'credits': 90},
            {'id': 8,'name': 'Анализ данных и знаний','cathedra_id': 2, 'credits': 70},
            {'id': 9,'name': 'Архитектура вычислительных систем','cathedra_id': 2, 'credits': 80},
            {'id': 10,'name': 'Методы оптимизации и исследование операций','cathedra_id': 2, 'credits': 80},
            {'id': 11,'name': 'Методы искусственного интеллекта','cathedra_id': 2, 'credits': 50},
            {'id': 12,'name': 'Моделирование сложных систем','cathedra_id': 2, 'credits': 70},
            {'id': 13,'name': 'Организация баз данных и знаний','cathedra_id': 2, 'credits': 80},
            {'id': 14,'name': 'Основы системного анализа','cathedra_id': 2, 'credits': 100},
            {'id': 15,'name': 'Охрана труда и безопасность жизнедеятельности','cathedra_id': 17, 'credits': 100},
            {'id': 16,'name': 'Основы охраны труда','cathedra_id': 17, 'credits': 60},
            {'id': 17,'name': 'Учет и аудит','cathedra_id': 1, 'credits': 70},
            {'id': 18,'name': 'Программирование и алгоритмические языки','cathedra_id': 2, 'credits': 70},
            {'id': 19,'name': 'Теория управления','cathedra_id': 2, 'credits': 80},
            {'id': 20,'name': 'Теория принятия решений','cathedra_id': 2, 'credits': 90},
            {'id': 21,'name': 'Операционные системы','cathedra_id': 4, 'credits': 90},
            {'id': 22,'name': 'WEB-технологии и WEB-дизайн','cathedra_id': 4, 'credits': 90},
            {'id': 23,'name': 'Экономическая информатика','cathedra_id': 4, 'credits': 100},
            {'id': 24,'name': 'Электронная коммерция','cathedra_id': 4, 'credits': 60},
            {'id': 25,'name': 'Компьютерная графика','cathedra_id': 4, 'credits': 90},
            {'id': 26,'name': 'Компьютерные сети','cathedra_id': 4, 'credits': 100},
            {'id': 27,'name': 'Нейросетевые технологии','cathedra_id': 2, 'credits': 110},
            {'id': 28,'name': 'Основы научных исследований','cathedra_id': 4, 'credits': 120},
            {'id': 29,'name': 'Проектирование информационных систем','cathedra_id': 4, 'credits': 100},
            {'id': 30,'name': 'Технологии защиты информации','cathedra_id': 4, 'credits': 80},
            {'id': 31,'name': 'Технология создания программных продуктов','cathedra_id': 4, 'credits': 70},
            {'id': 32,'name': 'Управление IT-проектами','cathedra_id': 4, 'credits': 110},
        ])

def downgrade():
    pass
