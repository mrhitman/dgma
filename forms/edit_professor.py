from flask_wtf import FlaskForm
from wtforms import validators, StringField, DateField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models.cathedra import possible_cathedras


class EditProfessorForm(FlaskForm):
    name = StringField('Имя', [validators.Length(min=4, max=50)])
    second_name = StringField('Фамилия', [validators.Length(min=4, max=50)])
    middle_name = StringField('Отчество', [validators.Length(min=4, max=50)])
    email = StringField('Почта', [validators.Length(min=6, max=50), validators.Email()])
    birthday = DateField('Дата рождения', [])
    cathedra = QuerySelectField('Кафедра', query_factory=possible_cathedras, get_label='short_name')
    post = StringField('Должность', [validators.Length(min=4, max=50)])
    academic_degree = StringField('Ученая степень', [validators.Length(min=1, max=50)])
    rank = StringField('Ученое звание', [validators.Length(min=4, max=50)])
    photo = FileField('Фотография', [])
