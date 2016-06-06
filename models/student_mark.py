from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db


class StudentMark(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, ForeignKey('student.id'))
    student = relationship("Student")
    discipline_id = db.Column(db.Integer, ForeignKey('discipline.id'))
    discipline = relationship("Discipline")
    mark = db.Column(db.Integer)

    def __repr__(self):
        return '<StudentMark %r %r %r>' % (self.student.user.name, self.discipline.name, self.mark)
