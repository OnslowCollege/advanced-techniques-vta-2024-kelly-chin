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

# Questions to ask user, return the 
def ask_easy_questions(question) -> str:
    """Asks user easy questions."""
# Prints easy trivia questions.
    for question in TRIVIA_QUESTIONS["Easy"]:
        print(question)

    return("user input")

# bool dictates whether if program is running.
program_running: bool = True

# Stores shop items from a dictionary.
SHOP_ITEMS: dict[str, dict[str, int | int]] = {
    "Small Ruby of the King's Crown": {"Price": 250, "Quantity Owned": 0},
    "item 2": {"Price": 500, "Quantity Owned": 0},
    "item 3": {"Price": 750, "Quantity Owned": 0},
    "item 4": {"Price": 1000, "Quantity Owned": 0},
}

# Dictionary of trivia questions, including easy, medium and hard difficulty.
TRIVIA_QUESTIONS: dict[str, dict[str, str]] = {
    "Easy": {
        "What country is the largest in the world?": "Russia",
        "Which sport uses the terms, Spare and Strike?": "Bowling",
        "What is the 4th letter in the English alphabet?": "D",
        "What country did french fries originate?": "Belgium",
        "Which galaxy do we live in?": "The Milky Way",
        "What element do humans need to survive?": "Oxygen",
        'What does the fast food chain, "KFC" stand for?': "Kentucky Fried Chicken",
        "What is the name of the Greek Goddess of Love and Beauty?": "Aphrodite",
        "What animal is the fastest in the world?": "Cheetah",
        "Who discovered gravity?": "Isaac Newton",
    },
    "Medium": {
        "What country is the only country with a triangular flag?": "Nepal",
        "What is the 6th element in the periodic table?": "Nitrogen",
        'Which planet is known as the "Blue Planet"?': "Earth",
        "What do you call baby kangaroos?": "Joey",
        'What year did the "y2k" problem occur?': "2000",
        "What language did the ancient Romans speak?": "Latin",
        "Which volcano in Indonesia caused the loudest sound in history?": "Krakatoa",
        "What organ is the largest in the human body?": "Skin",
    },
    "Hard": {
        'In the film "Dead Poets Society", which actor played "Neil Perry?"': "Robert Sean Leonard",
        "What is the only parrot that cannot fly?": "Kakapo",
        "Which Asian country fought in 7 deadliests wars in history?": "China",
        "How many hearts does an octopus have?": "3",
        "Which country is the only one that has the bible on their flag?": "Dominician Republic",
        'Which greek philosopher famously said, "Man is the measure of all things?': "Protogoras",
        "What shark species was the largest to have ever lived?": "Megalodon",
        'What character did Eliza Taylor play in the TV series, "The 100"?': "Clarke Griffins",
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


user_choice: int = 0
# Valid option remains True until user enters invalid choice. 
while valid_option is False:
    try:
        user_choice = int(input("\nEnter the number of your choice: "))
        if user_choice == 1:
            print(difficulty_page())
            difficulty_choice = str(input("Enter your choice of level difficulty: "))
            if difficulty_choice.upper() == "E":
                pass
                # Prints medium trivia questions.
            elif difficulty_choice.upper() == "M":
                pass
                # Prints hard trivia questions.
            elif difficulty_choice.upper() == "H":
                pass
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
