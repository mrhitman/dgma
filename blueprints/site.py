from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required

from database import db
from forms.login import LoginForm
from login_manger import login_manager
from models.professor import Professor
from models.user import User

site = Blueprint('site', __name__, template_folder='templates')


@site.route('/')
def index():
    return render_template('site/index/index.html')


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@site.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # password = hashlib.md5(bytes(form.password.data, 'utf-8')).hexdigest()
        user = User.query.filter_by(email=form.email.data, password=form.password.data).first()
        if user is None:
            flash('No such user')
            return render_template('site/login/login.html', form=form)
        login_user(user)
        return redirect(url_for('professor_page.personal_page'))
    return render_template('site/login/login.html', form=form)


@login_required
@site.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@site.route('/register', methods=['GET', 'POST'])
def register():
    from forms.registration import RegistrationForm
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.name = form.name.data
        user.second_name = form.second_name.data
        user.middle_name = form.middle_name.data
        user.birthday = form.birthday.data
        user.password = form.password.data
        user.email = form.email.data
        professor = Professor()
        professor.post = form.post.data
        professor.academic_degree = form.academic_degree.data
        professor.rank = form.rank.data
        professor.cathedra_id = form.cathedra.data.id
        professor.user = user
        db.session.add(user)
        db.session.add(professor)
        try:
            db.session.commit()
        except Exception:
            flash('Problem with registering')
            return redirect(url_for('site.register'))
        flash('Thanks for registering')
        return redirect(url_for('site.login'))
    return render_template('site/register/register.html', form=form)
