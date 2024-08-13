"""Dictionaries for later or edit."""

TRIVIA_QUESTIONS = {
    "Easy": {
        {
            "question": "What country is the largest in the world?",
            "answer": "Russia",
        },
        {
            "question": "Which sport uses the terms, Spare and Strike?",
            "answer": "Bowling",
        },
        {
            "question": "What is the 4th letter in the English alphabet?",
            "answer": "D",
        },
        {
            "question": "What country did french fries originate?",
            "answer": "Belgium",
        },
        {"question": "Which galaxy do we live in?", "answer": "The Milky Way"},
        {
            "question": "What element do humans need to survive?",
            "answer": "Oxygen",
        },
        {
            "question": 'What does fast food chain, "KFC" stand for?',
            "answer": "Kentucky Fried Chicken",
        },
        {
            "question": "What is the name of the Greek Goddess of Love and Beauty?",
            "answer": "Aphrodite",
        },
        {
            "question": "What animal is the fastest in the world?",
            "answer": "Cheetah",
        },
        {"question": "Who discovered gravity?", "answer": "Isaac Newton"},
    },
    "Medium": {
        1:{
            "question": "What country is the only country with a triangular flag?",
            "answer": "Nepal",
        },
        2:{
            "question": "What is the 6th element in the periodic table?",
            "answer": "Nitrogen",
        },
        3:{
            "question": 'Which planet is known as the "Blue Planet"?',
            "answer": "Earth",
        },
        4:{"question": "What do you call baby kangaroos?", "answer": "Joey"},
        5:{
            "question": 'What year did the "y2k" problem occur?',
            "answer": "2000",
        },
        6:{
            "question": "What language did the ancient Romans speak?",
            "answer": "Latin",
        },
        7:{
            "question": "Which volcano in Indonesia caused the loudest sound in history?",
            "answer": "Krakatoa",
        },
        8:{
            "question": "What organ is the largest in the human body?",
            "answer": "Skin",
        },
    },
    "Hard": {
        1:{
            "question": 'In the film "Dead Poets Society"(1989), who played "Neil Perry?"',
            "answer": "Robert Sean Leonard",
        },
        2:{
            "question": "What is the only parrot that cannot fly?",
            "answer": "Kakapo",
        },
        3:{
            "question": "Which Asian country fought in 7 deadliests wars in history?",
            "answer": "China",
        },
        4:{"question": "How many hearts does an octopus have?", "answer": "3"},
        5:{
            "question": "Which country is the only one that has the bible on their flag?",
            "answer": "Dominician Republic",
        },
        6:{
            "question": 'Which greek philosopher famously said, "Man is the measure of all things?',
            "answer": "Protogoras",
        },
        7:{
            "question": "What shark species was the largest to have ever lived?",
            "answer": "Megalodon",
        },
        8:{
            "question": 'What character did Eliza Taylor play in the TV series, "The 100"?',
            "answer": "Clarke Griffins",
        },
    },
}

# The code for the bottom part of the game.
while valid_option is False:
    try:
        # User is asked for difficulty choice if they chose to play game.
        user_choice = int(input("\nEnter the number of your choice: "))
        if user_choice == 1:
            print(difficulty_page())
            
            difficulty_choice = str(input("Enter level difficulty: "))
            while valid_option is False:
                try:
                    if difficulty_choice.upper() == "E":
                    # Prints easy questions individually for user to answer.
                        for question in TRIVIA_QUESTIONS["Easy"]:
                            print("☆-----------------------☆")
                        print(question)
                        question_number += 1
                        easy_guess = input("Enter your guess/answer here: ").upper()
                        guesses.append(easy_guess)
                        # If answer is correct, user earns 10 diamonds.
                        # If answer is incorrect, answer is returned to user.
                        for answer in TRIVIA_QUESTIONS.values():
                            if easy_guess == answer:
                                print("✅ Correct! You earnt 10💎!")
                                diamond_count += 10
                        else:
                            print(f"❌ Incorrect! The answer is {answer}!")
                    elif difficulty_choice.upper() == "M":
                    # Prints medium questions out individually.
                        for question in TRIVIA_QUESTIONS["Medium"]:
                            print("☆-----------------------☆")
                            print(question)
                    medium_guess = input("Enter your guess/answer here: ").upper()
                    guesses.append(medium_guess)
                    # If answer is correct, user earns 10 diamonds.
                    # If answer is incorrect, answer is returned to user.
                    for answer in TRIVIA_QUESTIONS.values():
                        if medium_guess == answer:
                            print("✅ Correct! You earnt 10💎!")
                            diamond_count += 10
                        else:
                            print(f"❌ Incorrect! The answer is {answer}!")
                    elif difficulty_choice.upper() == "H":
                    # Prints hard trivia questions out individually.  
                    for question in TRIVIA_QUESTIONS["Hard"]:
                        print("☆-----------------------☆")
                        print(question)
                    hard_guess = input("Enter your guess/answer here: ").upper()
                    guesses.append(hard_guess)
                    # If answer is correct, user earns 10 diamonds.
                    # If answer is incorrect, answer is returned to user.
                    for answer in TRIVIA_QUESTIONS.values():
                        if hard_guess == answer:
                                print("✅ Correct! You earnt 10💎!")
                                diamond_count += 10
                        else:
                            print(f"❌ Incorrect! The answer is {answer}!")
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                        print("Invalid option. Please try again.")

            # Function prints shop menu.
        elif user_choice == 2:
            print(shop())
            print(f"You have {diamond_count}💎")
            valid_option = True
        # Function prints how to play instructions.
        elif user_choice == 3:
            print(how_to_play())
            valid_option = True
        # Game program ends.
        elif user_choice == 4:
            print("Thanks for playing! Hope you have enjoyed 👋")
            program_running = False
            valid_option = True
        else:
            print("Invalid option entered. Please try again.")
            
    except ValueError:
        print("Invalid option. Please try again.")
