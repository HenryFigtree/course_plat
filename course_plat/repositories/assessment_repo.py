"""
Assessment repository

Contains database operations for retrieving and creating assessments
"""
class AssessmentRepository:
    def __init__(self, db):
        self.db = db

    def get_assessment(self, assessment_id):
        assessment = self.db.execute(
            """SELECT title, instructions, submission_type
            FROM assessments
            WHERE id = ?""",
            (assessment_id,)
        ).fetchone()

        if assessment is None:
            return None

        if assessment["submission_type"] == "online":
            return OnlineAssessment(
                assessment["title"],
                assessment["instructions"]
            )

        return Assessment(
            assessment["title"],
            assessment["instructions"]
        )

    def add_assessment(self,module_id, assessment, category):
        submission_type = "" 
        if isinstance(assessment, OnlineAssessment):
            submission_type = "online"

        self.db.execute(
            """INSERT INTO assessments 
            (module_id, category, submission_type, title, instructions)
            VALUES (?, ?, ?, ?, ?)""",
            (
                module_id,
                category,
                submission_type,
                assessment.title,
                assessment.instructions
            )
        )



