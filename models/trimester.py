# coding=utf-8
from database import db


class Trimester(db.Model):
    '''' Учебный триместр '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    num = db.Column(db.Integer)
