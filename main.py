from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap

from blueprints import site, professor, facility
from config import Config
from database import db
from login_manger import login_manager
from models import User, Student, Professor

app = Flask(__name__)
app.config.from_object(Config)

login_manager.init_app(app)

db.init_app(app)
Bootstrap(app)

app.register_blueprint(site.site)
app.register_blueprint(professor.professor)
app.register_blueprint(facility.facility)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(Professor, db.session))

if __name__ == "__main__":
    app.run(port=9000)
