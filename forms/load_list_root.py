from flask.ext.wtf import FlaskForm
from wtforms import validators, StringField
from wtforms.fields.html5 import DateField


class LoadListRootAddForm(FlaskForm):
    name = StringField('Название', [validators.Length(min=3, max=50)])
    start_period = DateField('Начало периода', [validators.DataRequired()])
    end_period = DateField('Конец периода', [validators.DataRequired()])


class LoadListRootSearchForm(FlaskForm):
    start_period = DateField('C', [])
    end_period = DateField('По', [])
