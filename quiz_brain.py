# todo: asking the questions
# todo: checking if the answer was correct
# todo: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        # Initialize attributes
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        # self.question_number += 1
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = bool(input(f'Q.{self.question_number}: {current_question.text} (True/False):  '))

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
