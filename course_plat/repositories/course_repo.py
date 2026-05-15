class CourseRepository:
    def __init__(self, db):
        self.db = db

    def register_course(self, course, filename):
        return self.db.execute(
                "INSERT INTO courses (course, file_name) VALUES (?, ?)",
                (course, filename)
               )

    def set_filepath(self, stored_filename, course_id):
        self.db.execute(
                "UPDATE courses SET file_path = ? WHERE id = ?",
                (stored_filename, course_id)
        )

    def get_courses(self):
        return self.db.execute(
                "SELECT id, course FROM courses"
               ).fetchall()

    def get(self, course_id):
        return self.db.execute(
                "SELECT * FROM courses Where id = ?", (course_id,)
               ).fetchone()

   
