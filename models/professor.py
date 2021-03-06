from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = relationship("User")
    cathedra_id = db.Column(db.Integer, ForeignKey('cathedra.id'))
    cathedra = relationship("Cathedra")
    post = db.Column(db.String(50))
    academic_degree = db.Column(db.String(50))
    rank = db.Column(db.String(50))
    photo = db.Column(db.String(100))

    def __repr__(self):
        return '<Professor %r %r %r>' % (self.user.name, self.user.second_name, self.user.middle_name)
