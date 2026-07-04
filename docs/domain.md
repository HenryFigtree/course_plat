# Future Domain

This document describes the application structure as planned.

Some parts of this architecture are still under design ir have not tet entered development.

For the current structure that is being worked on, see `current_domain.md`.

## Design

The application is centered around classrooms.

All educational content belongs to a classroom through a module.
Modules organize either learning resources or assessments, providing a consistent structure for both teachers and students.

Hierarchy goes as follows:

```text
Application
│
├─Users
│ ├─Authentication
│ └─Classroom Memberships
│
├─Classrooms
│ │
│ ├─Members
│ │ ├─Owner
│ │ ├─Teachers
│ │ └─Students
│ │
│ └─Modules
│   ├─Resources
│   │ ├─Links
│   │ ├─Files
│   │ └─Sections
│   │
│   └─Assessments
│     ├─Online Questions
│     │ ├─Multiple Choice
│     │ ├─True / False
│     │ └─Text
│     │
│     ├─Upload Submission (tentative domain architecture)
│     │ ├─Homework
│     │ ├─Exam
│     │ └─Project
│     │
│     └─Assessment Attempts (tentative domain architecture)
│       ├─Student Answers
│       ├─Grades
│       └─Feedback
│
│
└─Administration
  └─Site Administration (design in progress)
```

