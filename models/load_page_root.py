from sqlalchemy import ForeignKey

from database import db


class LoadPageRoot(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    start_period = db.Column(db.Integer, ForeignKey('user.id'))
    end_period = db.Column(db.Integer, ForeignKey('user.id'))

    def __repr__(self):
        return '<LoadPage %r>' % self.id

