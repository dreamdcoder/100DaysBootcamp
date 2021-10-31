from data import *
from question_model import *
from quiz_brain import *

question_bank = []

for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You have Finished the quiz!")
print(f"Your Final Score is/{quiz.question_number}")