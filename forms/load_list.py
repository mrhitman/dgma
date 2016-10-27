from flask_wtf import FlaskForm
from wtforms import validators, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from models.load_page_work_type import possible_works


class LoadListAddForm(FlaskForm):
    work_type = QuerySelectField('Вид работ', query_factory=possible_works, get_label='name')
    mark = IntegerField('Факт, балов', [validators.NumberRange(min=1)])
    count = IntegerField('Количество, шт.', [validators.NumberRange(min=1)])
