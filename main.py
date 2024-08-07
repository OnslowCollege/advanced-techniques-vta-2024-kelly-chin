"""
Trivia Quiz game || Project Management.

Created by: Kelly
Date: 6/06/2024
"""

# Function prints shop items.
def shop() -> str:
    """Print a shop."""
    print("== ITEMS FOR SALE! ==")
    for item in SHOP_ITEMS:
        print(item)
    return("")

# How to play instructions defined.
def how_to_play() -> str:
    """How to play instructions."""

    return ("""
    How to Play instructions: ❓ 

    » Objective of game: Collect as many diamonds 💎 as you can. «

    Depending on the level difficulty you choose from easy, medium, and hard, 
    you will earn a random amount of diamonds per correct question.
    
    Every answer you answer correct, If answering the next question correctly, 
    you will receive an uncertain reward, getting this question wrong, you
    will not receive your reward AND lose diamonds. Diamonds can be spent for
    goodies at the shop.

    Good Luck and have fun! 🤖""")

# Function for difficulty page before game starts.
def difficulty_page() -> str:
    """Print difficulty of quiz game."""

    return ("""

                    Quiz Difficulty:
        
        » Easy 😊 (E) «          » Medium 😐 (M) «

                    » Hard 😡 (H) «
        
""")


# Bool dictates whether if the user input is valid  
valid_option: bool = False

# bool dictates whether if program is running.
program_running: bool = True

# Score counter and number of guesses for the user.
diamond_count: int = 0
guesses = []
question_number: int = 0

# Stores shop items from a dictionary.
SHOP_ITEMS: dict[str, dict[str, int | int]] = {
    "Small Ruby of the King's Crown": {"Price": 250, "Quantity Owned": 0},
    "item 2": {"Price": 500, "Quantity Owned": 0},
    "item 3": {"Price": 750, "Quantity Owned": 0},
    "item 4": {"Price": 1000, "Quantity Owned": 0},
}

# Dictionary of trivia questions, including easy, medium and hard difficulty.
TRIVIA_QUESTIONS = {
    "Easy": {
        1: {
            "question": "What country is the largest in the world?",
            "answer": "Russia",
        },
        2: {
            "question": "Which sport uses the terms, Spare and Strike?",
            "answer": "Bowling",
        },
        3: {
            "question": "What is the 4th letter in the English alphabet?",
            "answer": "D",
        },
        4: {
            "question": "What country did french fries originate?",
            "answer": "Belgium",
        },
        5: {"question": "Which galaxy do we live in?", "answer": "The Milky Way"},
        6: {
            "question": "What element do humans need to survive?",
            "answer": "Oxygen",
        },
        7: {
            "question": 'What does fast food chain, "KFC" stand for?',
            "answer": "Kentucky Fried Chicken",
        },
        8: {
            "question": "What is the name of the Greek Goddess of Love and Beauty?",
            "answer": "Aphrodite",
        },
        9: {
            "question": "What animal is the fastest in the world?",
            "answer": "Cheetah",
        },
        10: {"question": "Who discovered gravity?", "answer": "Isaac Newton"},
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

# Trivia Quiz game menu.
print("""
                    Trivia Quiz Game!

    -------------------------------------     -------------------------
    ||           Play Game 🎮      (1) ||    || Visit Shop 🛒🛍️ (2) || 
    -------------------------------------     -------------------------

    -------------------------------------     -------------------------
    || How to play instructions 📜 (3) ||    ||    Exit Game 🏃 (4) || 
    -------------------------------------     -------------------------
    """)

# Valid option remains True until user enters invalid choice. 
while valid_option is False:
    try:
        user_choice = int(input("\nEnter the number of your choice: "))
        if user_choice == 1:
            print(difficulty_page())
            difficulty_choice = str(input("Enter level difficulty: "))
            if difficulty_choice.upper() == "E":
                # Prints easy questions individually for user to answer.
                for k, v in TRIVIA_QUESTIONS["Easy"].values():
                    for lol, lol2 in k.get(key):
                        print("☆-----------------------☆")
                        print(lol)
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
                # Prints medium trivia questions individually.
            elif difficulty_choice.upper() == "M":
                for question in TRIVIA_QUESTIONS["Medium"]:
                    print("☆-----------------------☆")
                    print(question)
                    medium_guess = input("Enter your guess/answer here: ").upper()
                    guesses.append(medium_guess)
                # Prints hard trivia questions individually. 
            elif difficulty_choice.upper() == "H":
                for question in TRIVIA_QUESTIONS["Hard"]:
                    print("☆-----------------------☆")
                    print(question)
                    hard_guess = input("Enter your guess/answer here: ").upper()
                    guesses.append(hard_guess)
            else:
                print("Invalid choice. Please try again.")
            valid_option = True
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
