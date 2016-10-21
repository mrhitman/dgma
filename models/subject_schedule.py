# coding=utf-8
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db


class SubjectSchedule(db.Model):
    ''' Расписание предмета '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.Integer, ForeignKey('subject.id'))
    subject = relationship('Subject')
    day_number = db.Column(db.Integer)
    lesson_number = db.Column(db.Integer)