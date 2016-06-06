from database import db


class LoadPageType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Varchar(50))

    def __repr__(self):
        return '<LoadPageType %r>' % self.name
