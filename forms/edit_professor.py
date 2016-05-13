from flask.ext.wtf import Form
from wtforms import validators, StringField, DateField, FileField


class EditProfessorForm(Form):
    name = StringField('Имя', [validators.Length(min=4, max=50)])
    second_name = StringField('Фамилия', [validators.Length(min=4, max=50)])
    middle_name = StringField('Отчество', [validators.Length(min=4, max=50)])
    email = StringField('Почта', [validators.Length(min=6, max=50), validators.Email()])
    birthday = DateField('Дата рождения', [])
    facility = StringField('Факультет', [validators.Length(min=4, max=50)])
    post = StringField('Должность', [validators.Length(min=4, max=50)])
    academic_degree = StringField('Ученая степень', [validators.Length(min=1, max=50)])
    rank = StringField('Ученое звание', [validators.Length(min=4, max=50)])
    photo = FileField('Фотография', [])
