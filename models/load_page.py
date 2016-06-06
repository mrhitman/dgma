from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import relationship

from database import db
from models.load_page_work_types import LoadPageWorkTypes


class LoadPage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    work_type_id = db.Column(db.Integer, ForeignKey(LoadPageWorkTypes.id))
    work_type = relationship('LoadPageWorkTypes')
    count = db.Column(db.Integer)
    mark = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    load_page_root_id = db.Column(db.Integer, ForeignKey('load_page_root.id'))

    def __repr__(self):
        return '<LoadPage %r>' % self.id
