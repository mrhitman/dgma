from flask.ext.wtf import Form
from wtforms import PasswordField, validators, StringField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from models.cathedra import Cathedra


class RegistrationForm(Form):
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
    cathedra = QuerySelectField('Кафедра', query_factory=Cathedra.query.all, get_pk=lambda a: a.id,
                                get_label=lambda a: a.short_name)
    post = StringField('Должность', [validators.Length(min=4, max=50)])
    academic_degree = StringField('Ученая степень', [validators.Length(min=1, max=50)])
    rank = StringField('Ученое звание', [validators.Length(min=4, max=50)])
