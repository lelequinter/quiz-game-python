# todo: asking the questions
# todo: checking if the answer was correct
# todo: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        # Initialize attributes
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        # self.question_number += 1
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False):  ')
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('you got it right')
            self.score += 1
        else:
            print('you got it wrong')
        print(f'the correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')
