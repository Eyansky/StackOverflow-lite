DROP TABLE IF EXISTS tbl_replies, tbl_answers, tbl_questions, tbl_users CASCADE;

DROP TYPE IF EXISTS e_is_correct;

CREATE TYPE e_is_correct AS ENUM
(
  'Yes',
  'No'
);

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
	question_id SERIAL PRIMARY KEY,
	question_title VARCHAR(255) NOT NULL,
	question_details VARCHAR(255) NOT NULL,
  date_posted timestamp without time zone default current_timestamp,
	posted_by INTEGER,
	FOREIGN KEY(posted_by) REFERENCES tbl_users (user_id)
);
CREATE TABLE tbl_answers
(
  answer_id SERIAL PRIMARY KEY,
  answered_by INTEGER,
  question INTEGER,
  answer_details VARCHAR(255) NOT NULL,
  date_answered timestamp without time zone default current_timestamp,
  upvote INTEGER,
  downvote INTEGER,
  is_correct e_is_correct DEFAULT 'No',
  FOREIGN KEY(answered_by) REFERENCES tbl_users (user_id),
  FOREIGN KEY(question) REFERENCES tbl_questions(question_id)
);
CREATE TABLE tbl_replies
(
  reply_id SERIAL PRIMARY KEY,
  r_answer_id INTEGER,
  r_question_id INTEGER,
  r_user_id INTEGER,
  reply VARCHAR(255) NOT NULL,
  date_replied timestamp without time zone default current_timestamp,
  FOREIGN KEY(r_answer_id) REFERENCES tbl_answers (answer_id),
  FOREIGN KEY(r_question_id) REFERENCES tbl_questions(question_id),
  FOREIGN KEY(r_user_id) REFERENCES tbl_users(user_id)
);
CREATE TABLE tbl_voters
(
	voter_id SERIAL PRIMARY KEY,
	voter_user_id INTEGER NOT NULL,
  voter_answer_id INTEGER NOT NULL
);