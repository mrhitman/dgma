from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db


def possible_works():
    return LoadPageWorkTypes.query


class LoadPageWorkTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25))
    info = db.Column(db.String(30))
    mark = db.Column(db.Integer)
    subtype_id = db.Column(db.Integer, ForeignKey('load_page_subtype.id'))
    subtype = relationship("LoadPageSubtype")

    def __repr__(self):
        return '<LoadPageWorkType %r>' % self.name
