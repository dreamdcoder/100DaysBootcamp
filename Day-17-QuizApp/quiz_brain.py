# TODO: asking the questions
# TODO: checking if answer is correct
# TODO: checking is ended

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = question.answer.lower()
        self.question_number += 1
        user_answer = input(f"{self.question_number}.{question.text} (True/False?).").lower()
        self.check_answer(user_answer, answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("Your answer is wrong!")
        print(f"Correct answer was {answer}.")
        print(f"Your score is {self.score}/{self.question_number}.")
        print("\n")
