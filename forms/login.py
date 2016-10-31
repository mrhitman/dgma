from flask_wtf import FlaskForm
from wtforms import PasswordField, validators, StringField, RadioField


class LoginForm(FlaskForm):
    email = StringField('Почта', [validators.Length(min=6, max=50), validators.Email()])
    role = RadioField('Login as', choices=[('professor','professor'),('student','student')], default='professor')
    password = PasswordField('Пароль', [
        validators.DataRequired(),
    ])