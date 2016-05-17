from flask import Blueprint, render_template

facility = Blueprint('facility', __name__, template_folder='templates')


@facility.route('/index')
def index():
    return render_template('professor/index/index.html')
