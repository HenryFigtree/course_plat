DROP TABLE IF EXISTS classroom;
DROP TABLE IF EXISTS classroom_members;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS modules;
DROP TABLE IF EXISTS resources;
DROP TABLE IF EXISTS links;
DROP TABLE IF EXISTS files;
DROP TABLE IF EXISTS sections;
DROP TABLE IF EXISTS assessments;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS choices;
DROP TABLE IF EXISTS true_false_answers;
DROP TABLE IF EXISTS text_answers;

-----------------------------------------------------------------------------
-- Classrooms are the center of the schema when a user creates it
-----------------------------------------------------------------------------

CREATE TABLE classroom (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	owner_id INTEGER,

	FOREIGN KEY (owner_id) REFERENCES users(id)
);


-----------------------------------------------------------------------------
-- Users table mainly for authentication
-----------------------------------------------------------------------------

CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	is_admin INTEGER NOT NULL DEFAULT 0
);


-----------------------------------------------------------------------------
-- Classroom members are assigned in classrooms, the owner of a classroom is a teacher
-- itself but have the aditional privileges of classroom administration.
-- Then there is the other members which are students enrolled to courses.
-----------------------------------------------------------------------------

CREATE TABLE classroom_members (
	user_id INTEGER,
	classroom_id INTEGER,
	role TEXT NOT NULL,

	PRIMARY KEY (user_id, classroom_id),

	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (classroom_id) REFERENCES classroom(id)
);


-----------------------------------------------------------------------------
-- Modules serve as a way to organize topics in the classroom. A module can
-- - contain a resource for learning such as a link to a website, a file like a 
--   presentation or simply a section is the classroom written in markdown
--
-- - contain an exam or exercise made in the webapp
-----------------------------------------------------------------------------

CREATE TABLE modules (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	classroom_id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	position INTEGER,

	FOREIGN KEY (classroom_id) REFERENCES classroom(id),
	UNIQUE (classroom_id, position)
);

CREATE TABLE resources (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	module_id INTEGER NOT NULL,
	resource_type TEXT NOT NULL,

	FOREIGN KEY (module_id) REFERENCES modules(id)
);

CREATE TABLE links (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	resource_id INTEGER,
	url TEXT NOT NULL,
	link_text TEXT NOT NULL,
	position INTEGER,

	FOREIGN KEY (resource_id) REFERENCES resources(id)
);

gREATE TABLE files (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	resource_id INTEGER,
	file_name TEXT NOT NULL,
	file_path TEXT NOT NULL,
	position INTEGER,

	FOREIGN KEY (resource_id) REFERENCES resources(id)
);

CREATE TABLE sections (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	resource_id INTEGER,
	content TEXT NOT NULL,
	position INTEGER,

	FOREIGN KEY (resource_id) REFERENCES resources(id)
);

-----------------------------------------------------------------------------
-- Assessments are contained in modules too and can be made in the webapp,
-- they can be:
--
-- - Multiple choice questions and open answer questions
-- - The exercise can be either an exam or just an exercise
-- - Other submission types that include uploads are also included 
-----------------------------------------------------------------------------

CREATE TABLE assessments (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	module_id INTEGER NOT NULL,
	category TEXT NOT NULL,
	submission_type TEXT NOT NULL,
	title TEXT NOT NULL,
	instructions TEXT NOT NULL,

	FOREIGN KEY (module_id) REFERENCES modules(id)
);

-----------------------------------------------------------------------------
-- Online submissions include online questions, which could be either true or
-- false, multiple choice or text based answers.
-- It can also include posts but that can be included in text based answers
-----------------------------------------------------------------------------

CREATE TABLE questions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	assessment_id INTEGER NOT NULL,
	position INTEGER NOT NULL,
	question TEXT NOT NULL,
	answer_type TEXT NOT NULL,

	UNIQUE (assessment_id, position),

	FOREIGN KEY (assessment_id) REFERENCES assessments(id)
);

CREATE TABLE choices (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	question_id INTEGER NOT NULL,
	position INTEGER NOT NULL,
	choice TEXT NOT NULL,
	is_correct INTEGER NOT NULL DEFAULT 0,

	UNIQUE (question_id, position),
	FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE true_false_answers (
	question_id INTEGER PRIMARY KEY,
	correct_answer INTEGER NOT NULL DEFAULT 0,
	CHECK (correct_answer IN (0, 1)),

	FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE text_answers (
	question_id INTEGER PRIMARY KEY,
	content TEXT,

	FOREIGN KEY (question_id) REFERENCES questions(id)
);
