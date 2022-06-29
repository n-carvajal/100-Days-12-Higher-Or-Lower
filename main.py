# Imports
from random import randint
from game_data import data
import art


# Function Definitions
def pick_item():
    """
    Picks random item from data.
    """
    random_index = randint(0, 49)
    item = data[random_index]
    return item


def display_item(item):
    """
    Displays formatted string for item and returns followers.
    """
    print(f"{item['name']}: {item['description']} from {item['country']}.")
    return item['follower_count']


# Variables
top_trump = ""
score = 0
# While loop that restarts the game whilst winning:
winning = True
while winning:
    # Clears console on every new turn:
    print("\n" * 50)
    # Print Game Logo:
    print(art.logo)
    if top_trump == "":
        pass
    else:
        print(f"{top_trump['name']} was correct. Let's keep going...\n")
    # If player on first turn or has not won previous turn generate item_1:
    if top_trump == "":
        item1 = pick_item()
        follow1 = display_item(item1)
        # print(f"For testing purposes followers = {follow1}")
    # Else use top_trump value as item_1:
    else:
        item1 = top_trump
        follow1 = display_item(top_trump)
        # print(f"For testing purposes followers = {follow1}")
    # If player not on 1st turn show number of consecutive correct guesses:
    if score > 0:
        print(f"Your consecutive correct guesses are: {score}")
    # print VS logo:
    print(f"{art.vs}\n")
    # While loop that generates item_2 and checks if item_2 is a duplicate of item_1:
    duplicate_item = True
    while duplicate_item:
        item2 = pick_item()
        # If item_2 is a duplicate of item_1 continue loop and regenerate item_2:
        if item2 == item1:
            continue
        # Else break loop and use item_2:
        else:
            duplicate_item = False
    follow2 = display_item(item2)
    # print(f"For testing purposes followers = {follow2}")
    # While loop that prompts for guess from user of A or B:
    valid_guess = False
    while not valid_guess:
        print("\nWho has more instagram followers?")
        guess = input(f"Type 'A' for {item1['name']}, or 'B' for {item2['name']}: ").upper()
        # If guess is equal to A or B, guess is valid and break loop:
        if guess == 'A' or guess == 'B':
            valid_guess = True
        # Else if guess not equal to A or B continue loop:
        else:
            print("You did not enter 'A' or 'B'.")
            continue
    # Game Logic
    if guess == 'A':
        if follow1 == follow2:
            top_trump = ""
            print(f"\nYou chose {guess}. DRAW")
        elif follow1 > follow2:
            top_trump = item1
            score += 1
            print(f"\nYou chose {guess}. CORRECT")
        else:
            top_trump = ""
            print(f"\nYou chose {guess}. INCORRECT")
            print(f"You achieved {score} correct consecutive guesses.")
            winning = False
    if guess == 'B':
        if follow2 == follow1:
            top_trump = ""
            print(f"\nYou chose {guess}. DRAW")
        elif follow2 > follow1:
            top_trump = item2
            score += 1
            print(f"\nYou chose {guess}. CORRECT")
        else:
            top_trump = ""
            print(f"\nYou chose {guess}. INCORRECT")
            print(f"You achieved {score} correct consecutive guesses.")
            winning = False
        # If player NOT winning. Game Over.
print("\nGame Over")




