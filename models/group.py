from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    cathedra_id = db.Column(db.Integer, ForeignKey('cathedra.id'))
    cathedra = relationship("Cathedra")
    students = relationship("Student", back_populates="group")

    def __repr__(self):
        return '<Group %r %r>' % (self.name, self.cathedra.name)
