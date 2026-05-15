class CourseService:
    def __init__(self, repo):
        self.repo = repo

    def register_filepath(self, registered_course, filename):
        course_id = registered_course.lastrowid
        stored_filename = f"course_{course_id}_{filename}"
        self.repo.set_filepath(stored_filename, course_id)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], stored_filename)
        file.save(filepath)
        db.commit()
