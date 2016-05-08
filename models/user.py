from flask.ext.login import unicode
from database import db


class User(db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, index=True)
    birthday = db.Column(db.DateTime)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r %r %r>' % (self.name, self.second_name, self.middle_name)