"""
Onslow on Demand.

Created by Matua Doc.
Created on 2024-04-22.
"""

# Functions.

def range_input(prompt: str, min_char_count: int, max_char_count: int) -> str:
    """
    Asks the user a question and returns a string with a given length range.

    Arguments:
    ---------
        prompt: the question to ask the user.
        min_char_count: the minimum number of characters.
        max_char_count: the maximum number of characters.

    Returns:
    -------
        A string whose length is within the specified range.

    """
    # This Boolean governs whether or not the loop below repeats.
    # While it is False, the user is repeatedly asked for a string.
    valid_string_found: bool = False

    # Ask for the string.
    while not valid_string_found:
        user_input: str = input(prompt)
        count = len(user_input)
        
        # Make sure the length of the string is within the specified range.
        if count >= min_char_count and count <= max_char_count:
            valid_string_found = True
        else:
            # Warn the user if they entered an invalid value.
            a, b = min_char_count, max_char_count
            print(f"You must enter a string between {a} and {b} characters.")
    
    return user_input


def int_input(prompt: str, min_value: int, max_value: int) -> int:
    """
    Asks the user a question and returns a valid integer.

    Arguments:
    ---------
        prompt: the question to ask the user.
        min_value: the minimum number that the user may enter.
        max_value: the maximum number that the user may enter.
    
    Returns:
    -------
        The number that the user entered.

    """
    # This Boolean governs whether or not the loop below repeats.
    # While it is False, the user is repeatedly asked for a number.
    valid_number_found: bool = False

    # Ask for the number.
    while not valid_number_found:
        user_input: str = input(prompt)
        try:
            # Attempt casting from string to integer.
            number: int = int(user_input)
            # If the cast succeeded, check if the number is in the valid range.
            # Otherwise, raise a ValueError to move into the except block and
            # print the error message.
            if number >= min_value and number <= max_value:
                valid_number_found = True
            else:
                raise ValueError
        except ValueError:
            # Warn the user if they entered an invalid value.
            a, b = min_value, max_value
            print(f"You must enter a valid number between {a} and {b}")
    
    return number

# Variables and constants.

# This Boolean governs whether the main program loop repeats.
running: bool = True

# The videos stored in the program.
videos: dict[str, dict[str, str | int]] = {
    "Toy Story": {"director": "Mr Toyman", "duration": 90},
    "A Bug's Life": {"director": "Mr Ladybird", "duration": 87}
}

# The minimum and maximum string lengths for video information.
MIN_CHAR_COUNT: int = 1
MAX_CHAR_COUNT: int = 255

# The minimum and maximum duration of videos.
MIN_DURATION: int = 1
MAX_DURATION: int = 1440

# String to let user skip.
TITLE_PROMPT: str = "Enter the title (or press Enter to skip): "
DIRECTOR_PROMPT: str = "Enter the director's name (or press Enter to skip): "
DURATION_PROMPT: str = "Enter the duration in minutes (or enter 0 to skip): "

# Welcome the user to the program.
print("Welcome to Onslow On Demand.")

# Repeat showing the options and asking for a task until the user quits.
while running:
    # Show a list of options to the user.
    print("""
    1. Add a new video.
    2. Edit a video.
    3. Remove a video.
    4. List all videos.
    Q. Quit.
    """)

    # Ask the user which option to do.
    user_input: str = input("Enter a choice: ")

    # Do the selected task.
    if user_input == "1":
        # Add a new video to the database.
        print("=== ADD A VIDEO ===")

        # Ask for the video's details.
        new_title: str = range_input("Enter the title: ",
                                     MIN_CHAR_COUNT, MAX_CHAR_COUNT)
        new_director: str = range_input("Enter the director's name: ",
                                  MIN_CHAR_COUNT, MAX_CHAR_COUNT)
        new_duration: int = int_input("Enter the duration in minutes: ",
                                MIN_DURATION, MAX_DURATION)
        
        # Add the new video to the database.
        videos[new_title] = {"director": new_director,
                             "duration": new_duration}
        print(f"--- Added '{new_title}'! ---")

    elif user_input == "2":
        # Edit a video's details.
        print("=== EDIT A VIDEO ===")

        # Ask the user for the title to remove, then check if it exists.
        user_input = input("Enter the video title to edit: ")
        if user_input in videos:
            # Ask for the new details.
            edit_title: str = range_input(TITLE_PROMPT, 0, MAX_CHAR_COUNT)
            edit_director: str = range_input(DIRECTOR_PROMPT, 0,
                                             MAX_CHAR_COUNT)
            edit_duration: int = int_input(DURATION_PROMPT, 0, MAX_DURATION)
            
            # Get the existing video information.
            video = videos.pop(user_input)

            # Check if the director and duration were updated. If so,
            # change the videos in the existing video information.
            if len(edit_director) > 0:
                video["director"] = edit_director
            if edit_duration != 0:
                video["duration"] = edit_duration

            # Re-add the video information to the database, specifying either
            # the new or old key whether the user provided a new title.
            final_title: str = edit_title if len(edit_title) > 0 \
                else user_input
            videos[final_title] = video

            # Print the new information.
            print(f"--- Edited '{user_input}' ---")
            print(f"'{final_title}' by {video['director']} ({video['duration']} minutes)")  # noqa: E501
        else:
            print(f"--- No such video found with title '{user_input}' ---")

    elif user_input == "3":
        # Remove a video from the database.
        print("=== REMOVE A VIDEO ===")

        # Ask the user for the title to remove, then check if it exists.
        user_input = input("Enter the video title to remove: ")
        if user_input in videos:
            # Remove the video that was found.
            videos.pop(user_input)
            print(f"--- Removed '{user_input}'! ---")
        else:
            print(f"--- No such video found with title '{user_input}' ---")

    elif user_input == "4":
        # List the details of all the videos in the database.
        print("=== LIST ALL VIDEOS ===")
        # Loop over each video in the database. Make sure it is sorted A-Z.
        for title in sorted(videos):
            video = videos[title]
            director = video["director"]
            duration = video["duration"]
            print(f"- '{title}' by {director} ({duration} minutes)")

    elif user_input.upper() == "Q":
        # End the program.
        running = False
        print("Bye bye!")

    else:
        # Warn if the user typed something invalid when making a choice.
        print("Invalid selection. Please try again.")