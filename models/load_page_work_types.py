from database import db


def possible_works():
    return LoadPageWorkTypes.query


class LoadPageWorkTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25))
    info = db.Column(db.String(30))
    mark = db.Column(db.Integer)

    def __repr__(self):
        return '<LoadPage %r>' % self.id
