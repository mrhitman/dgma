from flask.ext.wtf import Form
from wtforms import validators, StringField
from wtforms.fields.html5 import DateField


class LoadListRootAddForm(Form):
    name = StringField('Название', [validators.Length(min=3, max=50)])
    start_period = DateField('Начало периода', [validators.DataRequired()])
    end_period = DateField('Конец периода', [validators.DataRequired()])


class LoadListRootSearchForm(Form):
    start_period = DateField('C', [])
    end_period = DateField('По', [])
