"""
Trivia Quiz game || Project Management.

Created by: Kelly
Date: 6/06/2024
"""
# Function prints shop items
def shop() -> str:
    """Print a shop."""
    print("== XXX FOR SALE! ==")
    for item in SHOP_ITEMS:
        print(item)
    return("")

# How to play instructions defined
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

print("""
    Trivia Quiz Game
    1. Play game 🎮
    2. Visit shop 🛒🛍️
    3. How to play instructions 📜
    4. Exit game """)

SHOP_ITEMS: dict[str, int] = {
                             {"Name": "x",
                              "Price": 0,
                              "Quantity Owned": 0},

                              {"Name": "x",
                               "Price": 0,
                               "Quantity Owned": 0}}

user_choice: int = int(input("\nEnter the number of your choice: "))

program_running = True


if user_choice == 1:
    pass

elif user_choice == 2:
    print(shop())

elif user_choice == 3:
    # with the function, how to play instructions are printed. 
    print(how_to_play())  

# Game program ends. 
elif user_choice == 4:
    print("Thanks for playing! Hope you have enjoyed it! 👋")
    program_running = False


