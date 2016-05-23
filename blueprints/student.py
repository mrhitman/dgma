from flask import Blueprint, render_template

from models.student import Student

student = Blueprint('student', __name__, template_folder='templates')


@student.route('/student/<int:cathedra_id>')
def list(cathedra_id):
    students = Student.query.filter_by(cathedra_id=cathedra_id).all()
    return render_template('student/list/list.html', students=students)


@student.route('/student/<int:id>')
def detail(id):
    student = Student.get_or_404(id)
    return render_template('student/detail/detail.html', student=student)
