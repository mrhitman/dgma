from sqlalchemy import ForeignKey
from database import db


def possible_works():
    return LoadPageWorkTypes.query


class LoadPageWorkTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25))
    info = db.Column(db.String(30))
    mark = db.Column(db.Integer)
    type_id = db.Column(db.Integer, ForeignKey('load_page_type.id'))

    def __repr__(self):
        return '<LoadPage %r>' % self.id
