from flask import Blueprint, render_template, url_for
from flask.ext.login import current_user
from flask_login import login_required
from werkzeug.utils import secure_filename, redirect

from database import db
from forms.edit_professor import EditProfessorForm
from models.professor import Professor

professor = Blueprint('professor', __name__, template_folder='templates')


@professor.route('/index')
def index():
    return render_template('professor/index/index.html')


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
        photo = 'static/photos/user_' + str(person.id) + '_' + filename
        form.photo.data.save(photo)
        person.photo = 'photos/user_' + str(person.id) + '_' + filename
        db.session.add(person)
        db.session.commit()
        return redirect(url_for('professor.personal_page'))
    else:
        form.name.data = person.user.name
        form.second_name.data = person.user.second_name
        form.middle_name.data = person.user.middle_name
        form.birthday.data = person.user.birthday
        form.email.data = person.user.email
        # form.cathedra.data = person.facility
        form.rank.data = person.rank
        form.academic_degree.data = person.academic_degree
        form.post.data = person.post
        form.photo.data = person.photo
    return render_template('professor/edit/edit.html', form=form)
