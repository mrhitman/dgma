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


def upgrade():
    conn = op.get_bind()
    conn.execute('''INSERT INTO `load_page_type` (`name`) VALUES ('Учебно-методическая работа')''')
    conn.execute('''INSERT INTO `load_page_type` (`name`) VALUES ('Организационно-методическая работа')''')
    conn.execute('''INSERT INTO `load_page_type` (`name`) VALUES ('Научная работа')''')
    conn.execute('''INSERT INTO `load_page_type` (`name`) VALUES ('Воспитательная работа')''')
    conn.execute('''INSERT INTO `load_page_type` (`name`) VALUES ('Другие виды работ')''')


def downgrade():
    pass
