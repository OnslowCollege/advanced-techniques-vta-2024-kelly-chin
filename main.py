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
    print("""Difficulty: 
            Easy 😊 (E) 
            Medium 😐 (M)
            Hard 😣 (H)""")

    difficulty_choice: str = str(input("Choose difficulty (E, M, or H): "))
    if difficulty_choice.upper() == "E":
        pass
    elif difficulty_choice.upper() == "M":
        pass
    elif difficulty_choice.upper() == "H":
        pass
    else:
        print("Invalid choice. Please try again.")
    return ("")

# Questions to ask user, return the 
def question() -> str:
    """Asking user a question."""
    return("user's input")

# bool dictates whether if program is running.
program_running: bool = True

# Stores shop items from a dictionary.
SHOP_ITEMS: dict[str, dict[str, int | int]] = {
    "Small Ruby from the King's Crown": {"Price": 250, "Quantity Owned": 0},
    "item 2": {"Price": 500, "Quantity Owned": 0},
    "item 3": {"Price": 750, "Quantity Owned": 0},
    "item 4": {"Price": 1000, "Quantity Owned": 0},
}

# Dictionary of trivia questions, including easy, medium and hard difficulty.
TRIVIA_QUESTIONS: dict[str, dict[str, str]] = {
    "Easy": {
        "What country is the largest in the world?": "Russia",
        "Which sport uses the terms, Spare and Strike?": "Bowling",
        },
    "Medium": {
        "What country is the only country with a triangular flag?": "Nepal",
        },
    "Hard": {
        'In the film, "Dead Poets Society", who played the character "Neil Perry?"': 
        "Robert Sean Leonard",
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

# Bool dictates whether if the user input is valid  
valid_option: bool = False
user_choice: int = 0
# Valid option remains True until user enters invalid choice. 
while valid_option is False:
    try:
        user_choice = int(input("\nEnter the number of your choice: "))
        if user_choice == 1:
            print(difficulty_page())
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
