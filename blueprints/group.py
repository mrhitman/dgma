from flask import Blueprint, render_template

from models import Group

group = Blueprint('group_page', __name__, template_folder='templates')


@group.route('/group/<int:id>')
def group_students(id):
    group = Group.query.get_or_404(id)
    return render_template('group/students/students.html', group=group)
