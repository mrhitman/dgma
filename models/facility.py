from database import db


class Facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    img = db.Column(db.String(100))

    def __repr__(self):
        return '<Facility %r>' % self.name
