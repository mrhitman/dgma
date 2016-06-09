from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db
from models.student_mark import StudentMark


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = relationship("User")
    group_id = db.Column(db.Integer, ForeignKey('group.id'))
    group = relationship("Group")
    photo = db.Column(db.String(100))

    def __repr__(self):
        return '<Student %r %r %r>' % (self.user.name, self.user.second_name, self.user.middle_name)

    def get_avg_mark(self):
        marks = StudentMark.query.filter_by(student_id=self.id).all()
        if len(marks) == 0:
            return 0
        return sum([m.mark for m in marks]) / len(marks)