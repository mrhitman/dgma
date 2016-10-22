from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    cathedra_id = db.Column(db.Integer, ForeignKey('cathedra.id'))
    cathedra = relationship("Cathedra")
    credits = db.Column(db.Integer)

    def __repr__(self):
        return '<Subject %r >' % self.name
