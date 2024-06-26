question_prompts = [
    "What color are apples\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n?",
    "What color are bananas\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n?",
    "What color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n?",
]
# question consists of 2 parts: actual question and answer to the question
from Question import Question
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("you got " + str(score) +" questions right out of " +  str(len(questions)) + " right!")
    
run_test(questions)




