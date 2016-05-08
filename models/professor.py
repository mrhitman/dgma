from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database import db


class Professor(db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = relationship("User")
    facility = db.Column(db.String(50))
    post = db.Column(db.String(50))
    academic_degree = db.Column(db.String(50))
    rank = db.Column(db.String(50))

    def __repr__(self):
        return '<Professor %r %r %r>' % (self.user.name, self.user.second_name, self.user.middle_name)