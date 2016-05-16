from flask.ext.wtf import Form
from wtforms import PasswordField, validators, StringField


class LoginForm(Form):
    email = StringField('Почта', [validators.Length(min=6, max=50), validators.Email()])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
    ])
