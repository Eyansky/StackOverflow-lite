# StackOverflow-lite

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Eyansky/StackOverflow-lite) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Eyansky/StackOverflow-lite) [![Build Status](https://travis-ci.org/Eyansky/StackOverflow-lite.svg?branch=ch-tests-159846739)](https://travis-ci.org/Eyansky/StackOverflow-lite) [![Coverage Status](https://coveralls.io/repos/github/Eyansky/StackOverflow-lite/badge.svg?branch=ch-tests-159846739)](https://coveralls.io/github/Eyansky/StackOverflow-lite?branch=ch-tests-159846739) [![Maintainability](https://api.codeclimate.com/v1/badges/1aa773e735e851af212f/maintainability)](https://codeclimate.com/github/Eyansky/StackOverflow-lite/maintainability)

StackOverflow-lite is a platform where people can ask questions and provide answers.

# Live Preview of UI

[https://eyansky.github.io/StackOverflow-lite/](https://eyansky.github.io/StackOverflow-lite/)

## Prerequisites

These are HTML pages and can run in any browser that supports HTML.

## UI Built With

1.  HTML
2.  CSS
3.  JAVASCRIPT

## API Built With

1. Flask Restful

# Features

The users can perform the following functions:

- Users can create an account and log in.
- Users can post questions.
- Users can delete the questions they post.
- Users can post answers.
- Users can view the answers to questions.
- Users can accept an answer out of all the answers to his/her question as the preferred answer.

#### Installation

To clone and run this application, you will need [Git](https://git-scm.com/) installed on your computer. From your command line:

- Clone this repository to your local machine

```bash
$ git clone https://github.com/Eyansky/StackOverflow-lite
```

- Navigate to the folder that contains the app

```bash
$ cd StackOverflow-lite
```

- Open the challenge 2 branch

```bash
$ git checkout Challenge2
```

- Create a virtual environment and activate it

```bash
$ virtualenv env
```

- Activate the virtual environment

```bash
$ source env/bin/activate
```

- Install the requirements

```bash
$ pip install -r requirements.txt
```

- Launch the application

```bash
$ python run.py
```

- Run the tests

```bash
$ nosetests --exe -v
```

# API endpoints

#### Questions Endpoints

| Method | Endpoint                                    | Functionality       |
| ------ | ------------------------------------------- | ------------------- |
| POST   | /api/v1/users/questions                     | Add a question      |
| POST   | /api/v1/users/questions/question-ID/answers | Add an answer       |
| GET    | /api/v1/users/questions                     | Lists all questions |
| GET    | /api/v1/users/questions/questionID          | List a question     |

#### StackOverFlowLite hosted on Heroku

- [Open Heroku](https://stackoverflow-lite-eyansky.herokuapp.com)

## Contributing

1.  Fork this project to your account.
2.  Create a branch for the change you intend to make.
3.  Make your changes to your fork.
4.  Send a pull request from your fork's branch to my master branch.

## Guidelines

- Provide a link to the application or project's homepage.
- Provide links to documentation.
- Explain why you're making a change.
- Please consider the scope of your change.
- Please modify only one template per pull request.

The more you can make me understand the change you're making, the more likely I'll be to accept your contribution quickly.

## Author

- Ian Mwangi

# Acknowledgments

1.  Andela Kenya
