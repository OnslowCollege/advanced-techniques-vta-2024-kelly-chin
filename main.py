"""
Trivia Quiz game || Project Management.

Created by: Kelly
Date: 6/06/2024
"""

print("""
    Trivia Quiz Game
    1. Play game 🎮
    2. Visit shop 🛒🛍️
    3. How to play instructions 📜
    4. Exit game """)

user_choice: int = int(input("\nEnter the number of your choice: "))

program_running = True

if user_choice == 1:
    pass

elif user_choice == 2:
    pass

elif user_choice == 3:
    print("""How to Play instructions: 

    Objective of game: Collect as many diamonds💎 as you can.

    Depending on the level difficulty you choose from easy, medium, and hard, 
    you will earn a random amount of diamonds per correct question. 
    Every answer you answer correct, If answering the next question correctly, 
    you will receive an uncertain reward, getting this question wrong, you will not
    receive your reward AND lose diamonds. Diamonds can be spent for goodies at the
    shop.
    Good Luck and have fun!   :)""")

# Game program ends. 
elif user_choice == 4:
    print("Thanks for playing! Hope you have enjoyed it! ")
    program_running = False

