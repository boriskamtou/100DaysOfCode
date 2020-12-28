from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

brain = QuizBrain(question_bank)

while brain.still_has_question():
    brain.next_question()

print("You completed the quiz")
print(f"Your final score is: {brain.score} / {brain.question_number}")

