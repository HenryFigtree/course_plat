"""
Question repository

Contains database operations for retrieving and creating questions
"""

class QuestionRepository:
    def __init__(self, db):
        self.db = db

    def get_question(self, question_id):
        question = self.db.execute(
            """SELECT question, answer_type
            FROM questions
            WHERE id = ?""",
            (question_id,)
        ).fetchone()

        if question is None:
            return None

        choices = self.db.execute(
            """SELECT choice, is_correct
            FROM choices
            WHERE question_id = ?
            ORDER BY position""",
            (question_id,)
        ).fetchall()

        question_type = QuestionType(question["answer_type"])

        if question_type == QuestionType.MULTIPLE_CHOICE:
            choices_data = Choices()
            correct_choice = None

            for row in choices:
                choice = row["choice"]
                choices_data.add_choice(choice)

                if row["is_correct"]:
                    correct_choice = choice

            return Question(
                question_type,
                question["question"],
                choices_data,
                correct_choice
            )

    def add_question(self, assessment_id, position, question):
        question_cursor = self.db.execute(
            """INSERT INTO questions
            (assessment_id, position, question, answer_type)
            VALUES (?, ?, ?, ?)""",
            (
                assessment_id,
                position,
                question.text,
                question.question_type.value
            )
        )

        question_id = question_cursor.lastrowid

        if question.question_type == QuestionType.MULTIPLE_CHOICE:
            for position, choice in enumerate(question.choices.choices):
                is_correct = choice == question.correct_choice

                self.db.execute(
                    """INSERT INTO choices
                    (question_id, position, choice, is_correct)
                    VALUES (?, ?, ?, ?)""",
                    (
                        question_id,
                        position,
                        choice,
                        is_correct
                    )
                )
