from flask import Blueprint, render_template

from models.student import Student

student = Blueprint('student_page', __name__, template_folder='templates')


@student.route('/student/all')
def student_all():
    students = Student.query.all()
    return render_template('student/list/list.html', students=students)


@student.route('/student/<int:id>')
def detail(id):
    student = Student.query.get_or_404(id)
    return render_template('student/detail/detail.html', student=student)


@student.route('/student/<int:id>/group')
def group(id):
    student = Student.query.get_or_404(id)
    return render_template('group/students/students.html', student=student)
