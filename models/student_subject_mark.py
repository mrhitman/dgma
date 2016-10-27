# coding=utf-8
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db


class StudentSubjectMark(db.Model):
    ''' Отметка студента по предмету '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, ForeignKey('student.id'))
    student = relationship("Student")
    subject_id = db.Column(db.Integer, ForeignKey('subject.id'))
    subject = relationship("Subject")
    mark = db.Column(db.Integer)
    date = db.Column(db.Date)

    def __repr__(self):
        return '%s: %d (%s)' % (self.subject.name, self.mark, self.date.strftime('%Y-%m-%d'))
