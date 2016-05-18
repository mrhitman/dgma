from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db


class Cathedra(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    short_name = db.Column(db.String(15))
    image = db.Column(db.String(100))
    facility_id = db.Column(db.Integer, ForeignKey('facility.id'))
    facility = relationship('Facility')

    def __repr__(self):
        return '<Cathedra %r>' % self.name
