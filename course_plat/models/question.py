"""
Classes Question and Choice

Used to represent questions and their associated choices
"""

class Question:
    """
    Represents a question and its associated choices
    """
    def __init__(self, exam_id, number, text, choices):
        self.exam_id = exam_id
        self.number = number
        self.text = text
        self.choices = choices

    def correct_choice(self):
        for choice in self.choices:
            if choice.is_correct:
                return choice
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

        if len(self.choices) != 4:
            raise ValueError("There must be 4 not empty choices")

        for choice in self.choices:
            if not choice:
                raise ValueError("There cannot be empty choices")
        
        correct = [c for c in self.choices if c.is_correct]
        if len(correct) != 1:
            raise ValueError("There must be exactly one correct answer")


class Choice:
    """
    Represents a possible choice for a questions answer
    """
    def __init__(self, number, text, is_correct):
        self.number = number
        self.text = text
        self.is_correct = is_correct

