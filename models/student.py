from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db
from models.student_subject_mark import StudentSubjectMark
from models.trimester import Trimester


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = relationship("User")
    group_id = db.Column(db.Integer, ForeignKey('group.id'))
    group = relationship("Group")
    photo = db.Column(db.String(100))
    receipt_trimester_id = db.Column(db.Integer, ForeignKey('trimester.id'))
    receipt_trimester = relationship("Trimester")

    def __repr__(self):
        return '<Student %r %r %r>' % (self.user.name, self.user.second_name, self.user.middle_name)

    def get_marks(self):
        marks = StudentSubjectMark.query.filter_by(student_id=self.id).all()
        trimesters = Trimester.query.filter(Trimester.start_date >= self.receipt_date).all()
        trimesters = map(None, *([iter(trimesters)] * 3))
        return trimesters

    def get_trimester_marks(self, trimester_id):
        trimester = Trimester.query.get(trimester_id)
        marks = StudentSubjectMark.query.filter(
            trimester.start_date <= StudentSubjectMark.date <= trimester.end_date).all()

    def get_avg_mark(self):
        marks = StudentSubjectMark.query.filter_by(student_id=self.id).all()
        if len(marks) == 0:
            return 0
        return sum([m.mark for m in marks]) / len(marks)
