from flask import Flask
from flask_bootstrap import Bootstrap

from blueprints import site, professor, facility
from config import Config
from database import db
from login_manger import login_manager

app = Flask(__name__)
app.config.from_object(Config)

login_manager.init_app(app)

db.init_app(app)
Bootstrap(app)

app.register_blueprint(site.site)
app.register_blueprint(professor.professor)
app.register_blueprint(facility.facility)

if __name__ == "__main__":
    app.run(port=9000)
