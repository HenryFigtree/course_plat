from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.utils import secure_filename
import os
from course_plat.db import get_db
from course_plat.decorators import admin_required
from course_plat.repositories.question_repo import QuestionRepository
from course_plat.repositories.choice_repo import ChoiceRepository
from course_plat.repositories.course_repo import CourseRepository
from course_plat.repositories.exam_repo import ExamRepository
from course_plat.services.question_service import QuestionService
from course_plat.models.question import (
        Question, Choice
)

bp = Blueprint('admin', __name__, url_prefix = '/admin')

@bp.route('/dashboard')
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')

def allowed_file(filename):
    return( "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config['ALLOWED_EXTENTIONS'])

@bp.route('/uploadcourse', methods = ('GET', 'POST'))
@admin_required
def upload_course():
    if request.method == "POST":
        file = request.files.get("course_file")
        course = request.form['course']

        db = get_db()
        repo = CourseRepository(db)

        if not course:
            flash("Write a name for the course")
            return render_template('admin/uploadcourse.html')

        if not file:
            flash("No file type")
            return render_template('admin/uploadcourse.html')

        filename = secure_filename(file.filename)

        if not allowed_file(filename):
            flash("Invalid file type")
            return render_template('admin/uploadcourse.html')
        try:
            registered_course = repo.register_course(course, filename) 
            
        except db.IntegrityError:
            flash("Course already exists")
            return render_template('admin/uploadcourse.html')

        course_id = registered_course.lastrowid
        stored_filename = f"course_{course_id}_{filename}"
        repo.set_filepath(stored_filename, course_id)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], stored_filename)
        file.save(filepath)
        db.commit()

        flash("succesfully uploaded the course")
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/uploadcourse.html')


@bp.route('/examcreation', methods = ('GET', 'POST'))
@admin_required
def create_exam():
    db = get_db()
    
    if request.method == "POST":
        course_id = request.form['course_id']

        if not course_id:
            flash("No course for the exam selected")
            return render_template(url_for("admin.dashboard"))
        
        exam_repo = ExamRepository(db)
        exam_repo.new_exam(course_id)
        db.commit()

        flash("Exam created succesfully, time to add the questions")
        return redirect(url_for("admin.select_exam"))

    course_repo = CourseRepository(db)
    courses = course_repo.get_courses()
    return render_template('admin/examcreation.html', courses = courses)

@bp.route('/exameditor', methods = ('GET', 'POST'))
@admin_required
def select_exam():
    if request.method == "POST":
        exam_id = request.form['exam_id']

        if not exam_id:
            flash("Please select an exam to edit")
            return render_template('admin/exameditor.html')
        
        return redirect(url_for('admin.select_question', exam_id=exam_id))

    db = get_db()
    repo = ExamRepository(db)
    exams = repo.get_exams()

    return render_template('admin/exam_editor/select_exam.html', exams = exams)

@bp.route('/exameditor/<int:exam_id>', methods = ('GET', 'POST'))
@admin_required
def select_question(exam_id):

    db = get_db()
    question_repo = QuestionRepository(db)
    choice_repo = ChoiceRepository(db)

    if request.method == "POST":
        action = request.form['action']

        if action == "edit":
            question_number = request.form['question_number']
            return redirect(url_for('admin.question', exam_id = exam_id, question_number = question_number))

        elif action == "new":
            service = QuestionService(question_repo, choice_repo)
            question_number = service.next_question_number(exam_id)
            return redirect(url_for('admin.question', exam_id = exam_id, question_number = question_number))

    questions = question_repo.get_questions(exam_id)
    return render_template('admin/exam_editor/questions.html', questions = questions)

@bp.route('exameditor/<int:exam_id>/<int:question_number>', methods = ('GET', 'POST'))
@admin_required
def question(exam_id, question_number):
    db = get_db()
    question_repo = QuestionRepository(db)
    choice_repo = ChoiceRepository(db)

    if request.method == "POST":

        choice_text = [
            request.form['a'],
            request.form['b'],
            request.form['c'],
            request.form['d']
        ]
        correct_number = int(request.form['is_correct'])
        
        choices = []
        for i, text in enumerate(choice_text):
            choice = Choice(
                number = i,
                text = text,
                is_correct = (i == correct_number)
            )
            choices.append(choice)
            
        question = Question(
            exam_id = exam_id,
            number = question_number,
            text = request.form['question'],
            choices = choices
        )
        
        service = QuestionService(question_repo, choice_repo) 
        error = None

        try:
            service.save_question(question)
            db.commit()
        except ValueError as e:
            error = str(e)
            flash(error)
            return render_template('admin/exam_editor/edit_question.html')

        flash("Correctly edited question")
        return redirect(url_for('admin.select_question', exam_id = exam_id))

        flash(error)



    question = question_repo.select_question(exam_id, question_number) 

    choices = choice_repo.select_choices(exam_id, question_number)

    return render_template('admin/exam_editor/edit_question.html',
                           question = question, choices = choices, question_number = question_number
    )
