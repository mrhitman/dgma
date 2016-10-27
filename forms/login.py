from flask_wtf import FlaskForm
from wtforms import PasswordField, validators, StringField


class LoginForm(FlaskForm):
    email = StringField('Почта', [validators.Length(min=6, max=50), validators.Email()])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
    ])
