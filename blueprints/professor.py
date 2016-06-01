from flask import Blueprint, render_template, url_for
from flask.ext.login import current_user
from flask_login import login_required
from werkzeug.utils import secure_filename, redirect

from database import db
from forms.edit_professor import EditProfessorForm
from forms.load_list import LoadListAddForm
from forms.load_list_root import LoadListRootAddForm, LoadListRootSearchForm
from models.load_page import LoadPage
from models.load_page_root import LoadPageRoot
from models.professor import Professor

professor = Blueprint('professor_page', __name__, template_folder='templates')


@login_required
@professor.route('/personal_page')
def personal_page():
    person = Professor.query.get_or_404(current_user.get_id())
    return render_template('professor/personal_page/personal_page.html', person=person)


@login_required
@professor.route('/personal_guest_page/<int:id>')
def personal_guest_page(id):
    person = Professor.query.get_or_404(id)
    return render_template('professor/personal_page/personal_page.html', person=person)


@login_required
@professor.route('/edit', methods=['POST', 'GET'])
def edit():
    person = Professor.query.get_or_404(current_user.get_id())
    form = EditProfessorForm()
    if form.is_submitted():
        filename = secure_filename(form.photo.data.filename)
        if filename:
            photo = 'static/photos/user_' + str(person.id) + '_' + filename
            form.photo.data.save(photo)
            person.photo = 'photos/user_' + str(person.id) + '_' + filename
        person.user.name = form.name.data
        person.user.second_name = form.second_name.data
        person.user.middle_name = form.middle_name.data
        person.user.birthday = form.birthday.data
        person.cathedra_id = form.cathedra.data.id
        person.rank = form.rank.data
        person.post = form.post.data
        person.academic_degree = form.academic_degree.data
        db.session.add(person)
        db.session.commit()
        return redirect(url_for('professor_page.personal_page'))
    else:
        form.name.data = person.user.name
        form.second_name.data = person.user.second_name
        form.middle_name.data = person.user.middle_name
        form.birthday.data = person.user.birthday
        form.email.data = person.user.email
        form.cathedra.data = person.cathedra_id
        form.rank.data = person.rank
        form.academic_degree.data = person.academic_degree
        form.post.data = person.post
        form.photo.data = person.photo
    return render_template('professor/edit/edit.html', form=form)


@login_required
@professor.route('/load_page/<int:id>')
def load_page(id):
    page = LoadPage.query.filter_by(user_id=current_user.get_id(), load_page_root_id=id).all()
    return render_template('professor/load_page/load_page.html', load_page=page, load_page_id=id)


@login_required
@professor.route('/load_page_root', methods=['GET', 'POST'])
def load_page_root():
    search_form = LoadListRootSearchForm()
    if search_form.is_submitted():
        page = LoadPageRoot.query.filter_by(user_id = current_user.get_id())
        if search_form.start_period.data:
            page = page.filter(LoadPageRoot.start_period >= search_form.start_period.data)
        if search_form.end_period.data:
            page = page.filter(LoadPageRoot.end_period <= search_form.end_period.data)

        return render_template('professor/load_page/load_page_root.html', load_page=page.all(), form=search_form)
    else:
        page = LoadPageRoot.query.filter_by(user_id=current_user.get_id()).all()
    return render_template('professor/load_page/load_page_root.html', load_page=page, form=search_form)


@login_required
@professor.route('/add_load_page_root', methods=['GET', 'POST'])
def add_load_page_root():
    form = LoadListRootAddForm()
    if form.validate_on_submit():
        page_root = LoadPageRoot()
        page_root.name = form.name.data
        page_root.start_period = form.start_period.data
        page_root.end_period = form.end_period.data
        page_root.user_id = current_user.get_id()
        db.session.add(page_root)
        db.session.commit()
        return redirect(url_for('professor_page.load_page_root'))
    return render_template('professor/load_page/add_load_page_root.html', form=form)


@login_required
@professor.route('/add_load_page/<int:id>', methods=['GET', 'POST'])
def add_load_page(id):
    form = LoadListAddForm()
    if form.validate_on_submit():
        page = LoadPage()
        page.count = form.count.data
        page.mark = form.mark.data
        page.work_type_id = form.work_type.data.id
        page.user_id = current_user.get_id()
        page.load_page_root_id = id
        db.session.add(page)
        db.session.commit()
        return redirect(url_for('professor_page.load_page', id=id))
    return render_template('professor/load_page/add_load_page.html', form=form, load_page_id=id)
