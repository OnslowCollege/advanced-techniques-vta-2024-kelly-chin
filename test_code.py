"""Test again."""

import random
 
TRIVIA_QUESTIONS = {
    'easy': [
        {
            'question': 'What is the capital of France?',
            'answer': 'Paris'
        },
        {
            'question': 'What is the capital of Italy?',
            'answer': 'Rome'
        },
    ],
    'medium': [
        {
            'question': 'What is the capital of Spain?',
            'answer': 'Madrid'
        },
        {
            'question': 'What is the capital of Germany?',
            'answer': 'Berlin'
        },
    ],
}
 
difficultyLevel = input('Enter difficulty level: ')
 
if difficultyLevel not in TRIVIA_QUESTIONS:
    print('Invalid difficulty level. Exiting.')
    exit()
 
# Get the question pool based on the difficulty level
'''
e.g. if difficultyLevel is 'easy', questionPool will be:
    {
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    },
    {
        'question': 'What is the capital of Italy?',
        'answer': 'Rome'
    },
'''
questionPool = TRIVIA_QUESTIONS[difficultyLevel]
 
# Randomly select a question/answer dict from the question pool
'''
We have the pool of questions. Now we want to randomly grab one of the question/answer pairs.
The output of randomQuestionAnswer will be:
    {
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    }
'''
randomQuestionAnswer = random.choice(questionPool)
 
# Print the question and save the user's input.
userAnswer = input(randomQuestionAnswer['question'] + ' ')
 
# Check if the user's input matches the answer. We're using .lower() to make the comparison case-insensitive.
if userAnswer.lower() == randomQuestionAnswer['answer'].lower():
    print('Correct!')
else:
    print('Incorrect! The correct answer is ' + randomQuestionAnswer['answer'])