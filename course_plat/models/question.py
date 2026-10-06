"""
Classes Question and Choice

Used to represent questions and their associated answers
"""

#To do: Create an enum for question type so that Question Class knows what kind of question it is
#Then move to create the answer types
#Finally create the construction validation methods
#Dont forget to now write type annotations since its important

from enum import Enum

class QuestionType(enum):
    MULTIPLE_CHOICE = "multiple choice"
    TRUEFALSE = "true false"
    TEXT = "text"

class Question:
    """
    Represents a question and its associated choices
    """
    def __init__(self, question_type, text, ans_data, correct_choice=None):
        self.text = text
        self.question_type = question_type
        if question_type == QuestionType.MULTIPLE_CHOICE:
            self.choices = ans_data
            self.correct_choice = correct_choice
        self.validate()

    def answer(self):
        if self.question_type == QuestionType.MULTIPLE_CHOICE:
            return self.correct_choice
        return None

    def validate(self):
        """
        Validates a question checking
        - if both question and choices are not empty
        - if there are exactly 4 choices and exactly 1 correct answer

        Raises:
            ValueError: if any validation rule is violated
        """

        if not self.text.strip():
            raise ValueError("Question cannot be empty")

        if self.question_type == QuestionType.MULTIPLE_CHOICE:
            for choice in self.choices:
                if not choice:
                    raise ValueError("There cannot be empty choices")
            if self.correct_choice = None:
                raise ValueError("No correct choice has been specified")

class Choices:
    """
    Represents a possible group of choices for a mutltiple choice question
    """
    def __init__(self, *choices):
        self._choices = list(choices)

    @property
    def choices(self):
        return tuple(self._choices)

    def edit(self, choice_num, new_choice):
        self._choices[choice_num] = new_choice

    def add_choice(self, *choices):
        for choice in choices:
            if len(self.choices) == 4:
                raise ValueError("Maximum number of choices already reached")
            self._choices.append(choice)

    def remove_choice(self, choice_num):
        del self._choices[choice_num]

