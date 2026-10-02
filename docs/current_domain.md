# Current application structure

This document describes the portion of the application currently under development.
For the complete planned architecture, see `domain.md`.
Hierarchy goes as follows:

```text
Classrooms
│
├─Members
│ ├─Owner
│ ├─Teachers
│ └─Student
│
└─Modules
  ├─Resources
  │ ├─Links
  │ ├─Files
  │ └─Sections
  │
  └─Assessments
    ├─Online Questions
    │ ├─Multiple Choice
    │ ├─True / False
    │ └─Text
    │
    └─Upload Submission
```

As implentation progresses, this document will evolve to reflect the current state of the application.
