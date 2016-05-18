from flask import Blueprint, render_template

from models.cathedra import Cathedra
from models.facility import Facility

facility = Blueprint('facility', __name__, template_folder='templates')


@facility.route('/facility')
def index():
    faculties = Facility.query.all()
    return render_template('facility/index/index.html', faculties=faculties)


@facility.route('/cathedras/<int:id>')
def cathedras(id):
    cathedras = Cathedra.query.filter_by(facility_id=id).all()
    return render_template('facility/cathedras/cathedras.html', cathedras=cathedras)
