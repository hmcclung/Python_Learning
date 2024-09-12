import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Creates an empty list which then pulls in the question and correct answer from the data.py file.
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Uses the QuizBrain class to initialize the quiz as the specified question bank
quiz = QuizBrain(question_bank)
# As long as questions are still remaining, continues quiz checking answers for correctness.
while quiz.still_has_questions_remaining():
    quiz.next_question()

# When quiz is complete display the users final score
print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")