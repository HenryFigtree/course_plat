class QuestionService:
    def __init__(self, question_repo, choice_repo):
        self.question_repo = question_repo
        self.choice_repo = choice_repo

    def next_question_number(self, exam_id):
        last_question = self.question_repo.get_last_question(exam_id)
        return last_question + 1

    def save_question(self, question):
        question.validate()

        existing = self.question_repo.select_question(question.exam_id, question.number)
        if existing is None:
            self.question_repo.add_question(question.exam_id, question.number, question.text)

            for choice in question.choices:
                self.choice_repo.add_choice(question.exam_id, question.number, choice.number, choice.text, choice.is_correct)

        else:
            self.question_repo.edit_question(question.text, question.exam_id, question.number)

            for choice in question.choices:
                self.choice_repo.edit_choice(choice.number, choice.text, choice.is_correct, question.exam_id, question.number)
            


