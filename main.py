from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config
from blueprints import site, professor
from database import db
from login_manger import login_manager

app = Flask(__name__)
app.config.from_object(Config)

login_manager.init_app(app)

db.init_app(app)
Bootstrap(app)
app.register_blueprint(site.site)
app.register_blueprint(professor.professor)

if __name__ == "__main__":
    app.run()
