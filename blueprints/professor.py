from flask import Blueprint, render_template
from flask.ext.login import current_user
from models.professor import Professor

professor = Blueprint('professor', __name__, template_folder='templates')


@professor.route('/personal_page')
def personal_page():
    person = Professor.query.get_or_404(current_user.get_id())
    return render_template('professor/personal_page/personal_page.html', person=person)
