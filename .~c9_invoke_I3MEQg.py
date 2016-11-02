import os
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap

from blueprints import site, professor, facility, student, group
from config import Config
from database import db
from login_manger import login_manager
from models import User, Student, Professor, Cathedra, Facility, LoadPage, LoadPageWorkType, LoadPageSubtype, Group, \
    Subject, Trimester, StudentSubjectMark

app = Flask(__name__)
app.config.from_object(Config)

login_manager.init_app(app)

db.init_app(app)
Bootstrap(app)

app.register_blueprint(site.site)
app.register_blueprint(professor.professor)
app.register_blueprint(student.student)
app.register_blueprint(facility.facility)
app.register_blueprint(group.group)

admin = Admin(app, name='dgma admin', template_mode='bootstrap3')
admin.add_view(ModelView(Facility, db.session, 'Факультет'))
admin.add_view(ModelView(Cathedra, db.session, 'Кафедра'))
admin.add_view(ModelView(Group, db.session, 'Группа'))
admin.add_view(ModelView(LoadPage, db.session, 'Загрузочный лист'))
admin.add_view(ModelView(LoadPageWorkType, db.session, 'Типы работ для загр.л.'))
admin.add_view(ModelView(LoadPageSubtype, db.session, 'Подтипы загр.л.'))
admin.add_view(ModelView(Subject, db.session, 'Предмет'))
admin.add_view(ModelView(User, db.session, 'Пользователь'))
admin.add_view(ModelView(Student, db.session, 'Студент'))
admin.add_view(ModelView(StudentSubjectMark, db.session, 'Оценки студентов'))
admin.add_view(ModelView(Professor, db.session, 'Преподаватель'))
admin.add_view(ModelView(Trimester, db.session, 'Триместры'))

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
