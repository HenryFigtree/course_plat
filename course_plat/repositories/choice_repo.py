class ChoiceRepository:
    def __init__(self, repo):
        self.repo = repo

    def select_choices(self, exam_id, question_number):
        return self.repo.execute(
                        "SELECT choice, is_correct FROM choice WHERE exam_id = ? AND question_number = ?",
                        (exam_id, question_number)
                        ).fetchall()

    def add_choice(self, exam_id, question_number, index, choice, is_correct):
        self.repo.execute(
                """INSERT INTO choice
                (exam_id, question_number, choice_number, choice, is_correct)
                VALUES (?, ?, ?, ?, ?)""",
                (exam_id, question_number, index, choice, is_correct)
        )

    def edit_choice(self, choice_number, choice, is_correct, exam_id, question_number):
        self.repo.execute(
                """UPDATE choice
                SET choice = ?, is_correct = ?
                WHERE exam_id = ?
                AND question_number = ?
                AND choice_number = ?""",
                (choice, is_correct, exam_id, question_number, choice_number)
        )
