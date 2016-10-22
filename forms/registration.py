from flask.ext.wtf import FlaskForm
from wtforms import PasswordField, validators, StringField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models.cathedra import possible_cathedras
from wtforms.fields.html5 import DateField


class RegistrationForm(FlaskForm):
    name = StringField('Имя', [validators.Length(min=4, max=50)])
    second_name = StringField('Фамилия', [validators.Length(min=4, max=50)])
    middle_name = StringField('Отчество', [validators.Length(min=4, max=50)])
    email = StringField('Почта', [validators.Length(min=6, max=50), validators.Email()])
    birthday = DateField('Дата рождения', [validators.DataRequired()])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Подтверждение пароля')
    cathedra = QuerySelectField('Кафедра', query_factory=possible_cathedras, get_label='short_name')
    post = StringField('Должность', [validators.Length(min=4, max=50)])
    academic_degree = StringField('Ученая степень', [validators.Length(min=1, max=50)])
    rank = StringField('Ученое звание', [validators.Length(min=4, max=50)])
