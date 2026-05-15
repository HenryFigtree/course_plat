class QuestionRepository:
    def __init__(self, db):
        self.db = db

    def get_last_question(self, exam_id):
        return self.db.execute(
                "SELECT COUNT(*) FROM questions WHERE exam_id = ?",
                (exam_id,)
                ).fetchone()[0]

    def get_questions(self, exam_id):
        return self.db.execute(
                "SELECT question_number, question FROM questions WHERE exam_id = ?",
                (exam_id,)
                ).fetchall()

    def select_question(self, exam_id, question_number):
        return self.db.execute(
                "SELECT question FROM questions WHERE exam_id = ? AND question_number = ?",
                (exam_id, question_number)
                ).fetchone()

    def add_question(self, exam_id, question_number, text):
        self.db.execute(
                "INSERT INTO questions (exam_id, question_number, question) VALUES (?, ?, ?)",
                (exam_id, question_number, text)
        )

    def edit_question(self, text, exam_id, question_number):
        self.db.execute(
                "UPDATE questions SET question = ? WHERE exam_id = ? AND question_number = ?",
                (text, exam_id, question_number)
        )

        
