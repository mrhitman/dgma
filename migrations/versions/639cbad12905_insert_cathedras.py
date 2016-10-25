"""Add cathedras

Revision ID: 639cbad12905
Revises: acbb697476a1
Create Date: 2016-05-19 15:33:32.460936

"""

# revision identifiers, used by Alembic.
revision = '639cbad12905'
down_revision = 'acbb697476a1'

from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

def upgrade():
    conn = op.get_bind()
    cathedra = table('cathedra',
        column('id', Integer),
        column('name', String),
        column('short_name', String),
        column('image', String),
        column('facility_id', Integer)
    )
    op.bulk_insert(cathedra, 
        [
            {'id':1,'name': 'Кафедра автоматизации производственных процессов', 'short_name': 'АПП','image': 'cathedra/app.jpg', 'facility_id': 1},
            {'id':2,'name': 'Кафедра интеллектуальных систем принятия решений', 'short_name': 'ИСПР','image': 'cathedra/ispr.jpg', 'facility_id': 1},
            {'id':3,'name': 'Кафедра электромеханических систем автоматизации', 'short_name': 'ЭСА','image': 'cathedra/esa.jpg', 'facility_id': 1},
            {'id':4,'name': 'Кафедра компьютерных информационных технологий', 'short_name': 'КИТ','image': 'cathedra/it.jpg', 'facility_id': 1},
            {'id':5,'name': 'Кафедра информатики и инженерная графика', 'short_name': 'ИиИг','image': 'cathedra/iiig.jpg', 'facility_id': 1},
            {'id':6,'name': 'Кафедра технологии машиностроения', 'short_name': 'ТМ','image': 'cathedra/tm.jpg', 'facility_id': 1},
            {'id':7,'name': 'Кафедра автоматизированных металлургических машин и оборудования', 'short_name': 'АММО','image': 'cathedra/ammio.jpg', 'facility_id': 2},
            {'id':8,'name': 'Кафедра подъемно-транспортных машин', 'short_name': 'ПТМ','image': 'cathedra/ptm.jpg', 'facility_id': 2},
            {'id':9,'name': 'Кафедра компьютеризированных мехатронных системы, инструменты и технологии', 'short_name': 'КМСИиТ','image': 'cathedra/msi.jpg', 'facility_id': 2},
            {'id':10,'name': 'Кафедрой высшей математики', 'short_name': 'ВМ','image': 'cathedra/vm.jpg', 'facility_id': 2},
            {'id':11,'name': 'Кафедра инженерной и компьютерной графики', 'short_name': 'ИГ','image': 'cathedra/graf.jpg', 'facility_id': 2},
            {'id':12,'name': 'Кафедра физики', 'short_name': 'КФ','image': 'cathedra/fiz.jpg', 'facility_id': 2},
            {'id':13,'name': 'Кафедра технической механики', 'short_name': 'ТМ','image': 'cathedra/tm_1.jpg', 'facility_id': 3},
            {'id':14,'name': 'Кафедра оборудования и технологий сварочного производства им. профессора в. м. Карпенк', 'short_name': 'ОиТПС','image': 'cathedra/sp.jpg', 'facility_id': 3},
            {'id':15,'name': 'Кафедра обработки металлов давлением', 'short_name': 'ОМД','image': 'cathedra/omd.jpg', 'facility_id': 3},
            {'id':16,'name': 'Кафедра технологии и оборудование литейного производства', 'short_name': 'ТОЛП','image': 'cathedra/lp.jpg', 'facility_id': 3},
            {'id':17,'name': 'Кафедра химии и охраны труда', 'short_name': 'ХиОТ','image': 'cathedra/hiop.jpg', 'facility_id': 3},
            {'id':18,'name': 'Кафедра основы проектирования машин', 'short_name': 'ОПМ','image': 'cathedra/opm.jpg', 'facility_id': 3},
            {'id':19,'name': 'Кафедра финансы', 'short_name': 'Финансы','image': 'cathedra/f.jpg', 'facility_id': 4},
            {'id':20,'name': 'Кафедра учета и аудита', 'short_name': 'УиА','image': 'cathedra/yia.jpg', 'facility_id': 4},
            {'id':21,'name': 'Кафедра менеджмента', 'short_name': 'Менеджмент','image': 'cathedra/logo_kaf.png', 'facility_id': 4},
            {'id':22,'name': 'Кафедра экономики предприятия', 'short_name': 'ЭП','image': 'cathedra/ep.jpg', 'facility_id': 4},
            {'id':23,'name': 'Кафедра «механика и пластического формования»', 'short_name': 'МПФ','image': 'cathedra/eng.jpg', 'facility_id': 4},
            {'id':24,'name': 'Кафедра физической подготовки', 'short_name': 'ФВ','image': 'cathedra/fv.jpg', 'facility_id': 4},
            {'id':25,'name': 'Кафедра экономической теории', 'short_name': 'ЭТ','image': 'cathedra/et.jpg', 'facility_id': 4},
            {'id':26,'name': 'Кафедра философии', 'short_name': 'Философия','image': 'cathedra/fil.jpg', 'facility_id': 4},
            {'id':27,'name': 'Кафедра иностранного языка', 'short_name': 'Английский язык','image': 'cathedra/fil.jpg', 'facility_id': 4},
            {'id':28,'name': 'Кафедра украинского языка', 'short_name': 'Украинский язык','image': 'cathedra/fil.jpg', 'facility_id': 4},
        ]
    )
   


def downgrade():
    pass
