from flask import (
        Blueprint, flash, g, render_template, request, url_for, send_from_directory, current_app, abort
)
from course_plat.decorators import login_required
from course_plat.db import get_db
from course_plat.repositories.course_repo import CourseRepository

bp = Blueprint('courses', __name__)

@bp.route('/', methods = ('GET',  'POST'))
def index():

    db = get_db()
    repo = CourseRepository(db)
    courses = repo.get_courses()
    return render_template('courses/index.html', courses = courses)

@bp.route('/courses/<int:course_id>/download')
@login_required
def download_course(course_id):
    db = get_db()
    repo = CourseRepository(db)
    course = repo.get(course_id)

    if course is None:
        abort(404)

    return send_from_directory(
            current_app.config['UPLOAD_FOLDER'],
            course['file_path'],
            as_attachment = True,
            download_name = course['file_name']
    )


