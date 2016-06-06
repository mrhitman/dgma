from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from models.facility import Facility
from models.load_page import LoadPage
from models.cathedra import Cathedra
from models.load_page_work_types import LoadPageWorkTypes
from models.professor import Professor
from models.student import Student
from models.student_mark import StudentMark
from models.discipline import Discipline

from config import Config
from database import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
