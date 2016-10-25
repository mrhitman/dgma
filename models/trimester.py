# coding=utf-8
import time

from database import db


class Trimester(db.Model):
    '''' Учебный триместр '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    num = db.Column(db.Integer)

    @classmethod
    def get_active(cls):
        now = time.strftime('%Y-%m-%d')
        return cls.query.filter(cls.start_date >= now, cls.end_date <= now).one()
