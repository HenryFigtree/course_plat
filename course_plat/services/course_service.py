import os
from flask import current_app
from werkzeug.utils import secure_filename
from course_plat.exceptions import (
        InvalidFileTypeError, CourseAlreadyExists
)

class CourseService:
    def __init__(self, repo):
        self.repo = repo

    def register_course(self, course, file):
        filename = secure_filename(file.filename)
        #If not allowed filename return an error
        if not allowed_file(filename):
            raise InvalidFileTypeError()

        try:
            registered_course = self.repo.write_course(course, filename)
        except self.repo.db.IntegrityError:
            raise CourseAlreadyExists()

        course_id = registered_course.lastrowid
        stored_filename = f"course_{course_id}_{filename}"
        self.repo.set_filepath(stored_filename, course_id)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], stored_filename)
        file.save(filepath)
        self.repo.db.commit()

def allowed_file(filename):
    return( "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS'])


