from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    # create a question object
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

# Create the quiz brain
quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f'Your final score is {quiz.score} / {len(quiz.question_list)}')
