"""Add cathedras

Revision ID: 639cbad12905
Revises: acbb697476a1
Create Date: 2016-05-19 15:33:32.460936

"""

# revision identifiers, used by Alembic.
revision = '639cbad12905'
down_revision = 'acbb697476a1'

from alembic import op


def upgrade():
    conn = op.get_bind()
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (1, 'Кафедра автоматизации производственных процессов', 'АПП', 'cathedra/app.jpg', 1);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (2, 'Кафедра интеллектуальных систем принятия решений', 'ИСПР', 'cathedra/ispr.jpg', 1);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (3, 'Кафедра электромеханических систем автоматизации', 'ЭСА', 'cathedra/esa.jpg', 1);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (4, 'Кафедра компьютерных информационных технологий', 'КИТ', 'cathedra/it.jpg', 1);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (5, 'Кафедра информатики и инженерная графика', 'ИиИг', 'cathedra/iiig.jpg', 1);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (6, 'Кафедра технологии машиностроения', 'ТМ', 'cathedra/tm.jpg', 1);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (7, 'Кафедра автоматизированных металлургических машин и оборудования', 'АММО', 'cathedra/ammio.jpg', 2);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (8, 'Кафедра подъемно-транспортных машин', 'ПТМ', 'cathedra/ptm.jpg', 2);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (9, 'Кафедра компьютеризированных мехатронных системы, инструменты и технологии', 'КМСИиТ', 'cathedra/msi.jpg', 2);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (10, 'Кафедрой высшей математики', 'ВМ', 'cathedra/vm.jpg', 2);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (11, 'Кафедра инженерной и компьютерной графики', 'ИГ', 'cathedra/graf.jpg', 2);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (12, 'Кафедра физики', 'КФ', 'cathedra/fiz.jpg', 2);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (13, 'Кафедра технической механики', 'ТМ', 'cathedra/tm_1.jpg', 3);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (14, 'Кафедра оборудования и технологий сварочного производства им. профессора в. м. Карпенк', 'ОиТПС', 'cathedra/sp.jpg', 3);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (15, 'Кафедра обработки металлов давлением', 'ОМД', 'cathedra/omd.jpg', 3);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (16, 'Кафедра технологии и оборудование литейного производства', 'ТОЛП', 'cathedra/lp.jpg', 3);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (17, 'Кафедра химии и охраны труда', 'ХиОТ', 'cathedra/hiop.jpg', 3);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (18, 'Кафедра основы проектирования машин', 'ОПМ', 'cathedra/opm.jpg', 3);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (19, 'Кафедра финансы', 'Финансы', 'cathedra/f.jpg', 4);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (20, 'Кафедра учета и аудита', 'УиА', 'cathedra/yia.jpg', 4);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (21, 'Кафедра менеджмента', 'Менеджмент', 'cathedra/logo_kaf.png', 4);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (22, 'Кафедра экономики предприятия', 'ЭП', 'cathedra/ep.jpg', 4);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (23, 'Кафедра «механика и пластического формования»', 'МПФ', 'cathedra/eng.jpg', 4);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (24, 'Кафедра физической подготовки', 'ФВ', 'cathedra/fv.jpg', 4);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (25, 'Кафедра экономической теории', 'ЭТ', 'cathedra/et.jpg', 4);''')
    conn.execute('''INSERT INTO "main"."cathedra" VALUES (26, 'Кафедра философии', 'Философия', 'cathedra/fil.jpg', 4);''')


def downgrade():
    pass
