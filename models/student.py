from collections import defaultdict

from flask import json
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db
from models.trimester import Trimester
from models.student_subject_mark import StudentSubjectMark
import numpy



class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = relationship("User")
    group_id = db.Column(db.Integer, ForeignKey('group.id'))
    group = relationship("Group")
    photo = db.Column(db.String(100))
    receipt_trimester_id = db.Column(db.Integer, ForeignKey('trimester.id'))
    receipt_trimester = relationship("Trimester")
    marks = relationship("StudentSubjectMark", back_populates='student')


    def __repr__(self):
        return '<Student %r %r %r>' % (self.user.name, self.user.second_name, self.user.middle_name)


    def get_avg_mark(self):
        marks = StudentSubjectMark.query.filter_by(student_id=self.id).all()
        if len(marks) == 0:
            return 0
        return sum([m.mark for m in marks]) / len(marks)
    
    
    def get_prediction_mark(self):
        marks = StudentSubjectMark.query.filter_by(student_id=self.id).order_by(StudentSubjectMark.date).all()
        if len(marks) == 0:
            return 0
        y = numpy.array([m.mark for m in marks])
        x = numpy.array(range(len(marks)))
        z = numpy.polyfit(x, y, 1)
        return z[1]
        
        
    def get_subjects_json(self):
        data = defaultdict(list)
        for subject_mark in self.marks:
            data.setdefault(subject_mark.subject.name, [])
            data[subject_mark.subject.name].append(subject_mark.mark)
        for subject_name in data:
            data[subject_name] = sum(data[subject_name]) / len(data[subject_name])
        return json.dumps(data)


    def get_active_trimester(self):
        trimester = Trimester.get_active()
        return StudentSubjectMark.query.filter(trimester.end_date >= StudentSubjectMark.date, StudentSubjectMark.student_id == self.id).all()
