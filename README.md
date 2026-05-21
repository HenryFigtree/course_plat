# WIP Course and Exam Management System

Flask Web Application for creating and managing courses and exams.

## Features

- User authentication
- Course and exam creation
- Create, delete and edit question from exam
- Multiple choice questions
- File uploads

## Installation

Clone repository

```bash
git clone https://github.com/HenryFigtree/course_plat.git
cd course_plat
```

create and activate virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Database must be initialized

```bash
flask --app course_plat init-db
```

Run the following to run the app

```
flask --app course_plat run
```

## WIP

Working on users course tracking and exam taking.

## Future Improvements

- Add unit tests
- Search functionality
- Post creation by users and teachers
- API support
