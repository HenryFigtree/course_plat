DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS exams;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS choice;

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	is_admin INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE courses (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	course TEXT UNIQUE NOT NULL,
	file_name TEXT NOT NULL,
	file_path TEXT
);

CREATE TABLE exams (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	course_id INTEGER UNIQUE NOT NULL,
	FOREIGN KEY (course_id) REFERENCES courses(id)
);
	

CREATE TABLE questions (
	exam_id INTEGER,
	question_number INTEGER,
	question TEXT NOT NULL,
	PRIMARY KEY (exam_id, question_number),
	FOREIGN KEY (exam_id) REFERENCES exams(id)
);

CREATE TABLE choice (
	exam_id INTEGER,
	question_number INTEGER,
	choice_number INTEGER,
	choice TEXT NOT NULL,
	is_correct INTEGER DEFAULT 0,
	PRIMARY KEY (exam_id, question_number, choice_number),
	FOREIGN KEY (exam_id, question_number) REFERENCES questions(exam_id, question_number)
);
