class ExamRepository:
    def __init__(self, db):
        self.db = db

    def new_exam(self, course_id):
        self.db.execute(
                "INSERT INTO exams (course_id) VALUES (?)",
                (course_id,)
        )

    def get_exams(self):
        return self.db.execute(
                """SELECT exams.id, courses.course
                FROM exams INNER JOIN courses ON exams.course_id = courses.id"""
               ).fetchall()
