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

# Stores shop items from a dictionary.
SHOP_ITEMS: dict[str, dict[str, int | int]] = {
    "Small Ruby of the King's Crown": {"Price": 250, "Quantity Owned": 0},
    "item 2": {"Price": 500, "Quantity Owned": 0},
    "item 3": {"Price": 750, "Quantity Owned": 0},
    "item 4": {"Price": 1000, "Quantity Owned": 0},
}

# 2d list for trivia questions.

easy_questions: list[list[str]] = [
["What country is the largest in the world?", "Which sport uses the terms, Spare and Strike?", ]



]


medium_questions: list[list[str]] = [



]

hard_questions: list[list[str]] = [



]

easy_answers: list[list[str]] = [



]

medium_answers: list[list[str]] = [



]

hard_answers: list[list[str]] = [



]
# Function that asks users easy trivia questions.
def ask_easy_questions() -> str:
    """Asks user easy questions."""
    for question in "Easy":
        print(TRIVIA_QUESTIONS[question])

    return("")

# Function that asks users medium trivia questions.
def ask_medium_questions() -> str:
    """Asks user easy questions."""
    print(TRIVIA_QUESTIONS["Medium"])

    return ("")


# Function that asks users hard trivia questions.
def ask_hard_questions() -> str:
    """Asks user easy questions."""
    for question in TRIVIA_QUESTIONS:
        print(question)

    return ("")
# Score counter and number of guesses for the user. 
score = 0
guesses = 0
question_num = 0 

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
            difficulty_choice = str(input("Enter your choice of level difficulty: "))
            if difficulty_choice.upper() == "E":
                # Prints easy questions.
                print(ask_easy_questions())
                user_answer = input("Answer here: ")
                # Prints medium trivia questions.
            elif difficulty_choice.upper() == "M":
                print(ask_medium_questions())
                # Prints hard trivia questions.
            elif difficulty_choice.upper() == "H":
                print(ask_hard_questions())
            else:
                print("Invalid choice. Please try again.")
            valid_option = True
            # Function prints shop menu.
        elif user_choice == 2:
            print(shop())
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
