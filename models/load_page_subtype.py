from database import db


class LoadPageSubtype(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<LoadPageSubtype %r>' % self.name
