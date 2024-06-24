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

# bool dictates whether if program is running.
program_running: bool = True

# Stores shop items from a dictionary.
SHOP_ITEMS: dict[str, dict[str, int | int]] = {
    "Small Ruby from the King's Crown": {"Price": 250, "Quantity Owned": 0},
    "item 2": {"Price": 500, "Quantity Owned": 0},
    "item 3": {"Price": 750, "Quantity Owned": 0},
    "item 4": {"Price": 1000, "Quantity Owned": 0},
}

# Trivia Quiz game menu.
print("""
    Trivia Quiz Game!
    1. Play game 🎮
    2. Visit shop 🛒🛍️
    3. How to play instructions 📜
    4. Exit game 🏃
    """)

print("""
                    Trivia Quiz Game!

    ---------------------       -------------------------
    || Play Game 🎮 (1)||      || Visit Shop 🛒🛍️ (2) || 
    ---------------------       -------------------------

    -------------------------------------     ---------------------
    || How to play instructions 📜 (3) ||    || Exit Game 🏃 (4) || 
    -------------------------------------     ---------------------
    """)

print("""
                    » Trivia Quiz Game! «

                    (P) ↪ Play game 🎮

    (V) ↪ Visit Shop 🛒🛍️             (H) ↪ How to Play instructions 📜

                    (E) ↪ Exit game 🏃

""")

user_choice: int = int(input("\nEnter the number of your choice: "))

# Bool dictates whether if the user input is valid  
valid_option: bool = False

# Valid option remains True until user enters invalid choice. 
while user_choice == "":
    if user_choice <= 5:
        print("text")
    else:
        print("Invalid choice. Please try again")
    valid_option = False

if user_choice == 1:
        print(difficulty_page())

# Function prints shop menu.
elif user_choice == 2:
    print(shop())

# Function prints how to play instructions. 
elif user_choice == 3:
    print(how_to_play())  

# Game program ends. 
elif user_choice == 4:
    print("Thanks for playing! Hope you have enjoyed 👋")
    program_running = False

else:
    print("Invalid choice. Please try again.")





