"""
Assessment repository

Contains database operations for retrieving and creating assessments
"""
class AssessmentRepository:
    def __init__(self, db):
        self.db = db

    def get_assessments(self, module_id):
        rows = self.db.execute(
            """SELECT title, instructions, submission_type
            FROM assessments
            WHERE module_id = ?""",
            (module_id,)
        ).fetchall()

        assessments = Assessments()

        for row in rows:
            if row["submission_type"] == "online":
                assessment = OnlineAssessment(
                    row["title"],
                    row["instructions"]
                )
            else:
                assessment = Assessment(
                    row["title"],
                    row["instructions"]
                )

            assessments.add(assessment)

        return assessments

    def add_assessment(self, module_id, assessment, category):
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
