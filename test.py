"""test."""
age: int = -1

while age == -1:
    try:
        # This code can raise an Exception.
        age = int(input("Enter your age: "))
    except ValueError:
        # If the ValueError exception is
        # raised, this block of code will run
        # instead of a crash happening.
        print("Invalid age provided.")
