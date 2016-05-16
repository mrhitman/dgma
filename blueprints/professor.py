from flask import Blueprint, render_template
from flask.ext.login import current_user
from flask_login import login_required
from werkzeug.utils import secure_filename

from database import db
from forms.edit_professor import EditProfessorForm
from models.professor import Professor
from config import Config

professor = Blueprint('professor', __name__, template_folder='templates')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in Config.ALLOWED_EXTENSIONS


@login_required
@professor.route('/personal_page')
def personal_page():
    person = Professor.query.get_or_404(current_user.get_id())
    return render_template('professor/personal_page/personal_page.html', person=person)


@login_required
@professor.route('/edit', methods=['POST', 'GET'])
def edit():
    person = Professor.query.get_or_404(current_user.get_id())
    form = EditProfessorForm()
    if form.is_submitted():
        filename = secure_filename(form.photo.data.filename)
        photo = 'static/user_' + str(person.id) + '_' + filename
        form.photo.data.save(photo)
        person.photo = 'user_' + str(person.id) + '_' + filename
        db.session.add(person)
        db.session.commit()
    return render_template('professor/edit/edit.html', form=form)
