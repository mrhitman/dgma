from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = relationship("User")
    group_id = db.Column(db.Integer, ForeignKey('group.id'))
    group = relationship("Group")
    photo = db.Column(db.String(100))

    def __repr__(self):
        return '<Student %r %r %r>' % (self.user.name, self.user.second_name, self.user.middle_name)
