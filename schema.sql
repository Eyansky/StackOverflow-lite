DROP TABLE IF EXISTS tbl_questions, tbl_answers, tbl_users CASCADE;

CREATE TABLE tbl_users
(
	user_id SERIAL PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL
);
CREATE TABLE tbl_questions
(
	questions_id SERIAL PRIMARY KEY,
	questions_title VARCHAR(255) NOT NULL,
	questions_description VARCHAR(255) NOT NULL,
	created_by INTEGER,
	FOREIGN KEY(created_by) REFERENCES tbl_users (user_id)
);
CREATE TABLE tbl_answers
(
  status_id SERIAL PRIMARY KEY,
  answers_status VARCHAR(50) NOT NULL,
  date_updated timestamp without time zone default current_timestamp,
  question INTEGER,
  FOREIGN KEY(question) REFERENCES tbl_questions (questions_id)
);