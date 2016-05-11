from flask import Blueprint, render_template, app
from flask.ext.login import current_user
from flask_login import login_required
from werkzeug.utils import secure_filename

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
def edit():
    person = Professor.query.get_or_404(current_user.get_id())
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template('professor/edit/edit.html', person=person)
