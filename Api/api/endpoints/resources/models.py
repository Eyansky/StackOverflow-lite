"""
The Database
"""

questions = [
    {
        "id":0,
        "question":"This is a question. Isnt it?"
    },
    {
        "id":1,
        "question":"This is a question. Isnt it?"
    }
]

answers = []

def view_questions():
    return questions

def addQuestion(title, question):
    id = random.randint(0, 7777777)
    data = {
        "id": id,
        "title": title,
        "question": question}
    questions.append(data)
    return True


