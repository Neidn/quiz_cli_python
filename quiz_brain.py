import random


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        random.shuffle(q_list)
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
