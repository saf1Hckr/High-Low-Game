from art import logo
from game_data import data
from art import vs
import random

print(logo)

# Initialize scores
current_score = 0

# Initialize random choices
random_dict_no_follower1 = random.choice(data)
C = random_dict_no_follower1.get("follower_count")

name1 = random_dict_no_follower1.get("name", "Unknown")
description1 = random_dict_no_follower1.get("description", "Unknown")
country1 = random_dict_no_follower1.get("country", "Unknown")

# Print initial Compare A
print(f"Compare A: {name1}, a {description1}, from {country1}")

print(vs)

random_dict_no_follower2 = random.choice(data)
D = random_dict_no_follower2.get("follower_count")

name2 = random_dict_no_follower2.get("name", "Unknown")
description2 = random_dict_no_follower2.get("description", "Unknown")
country2 = random_dict_no_follower2.get("country", "Unknown")

# Print initial Against B
print(f"Against B: {name2}, a {description2}, from {country2}")


def follower(C, D):
    global current_score

    # Get user input
    user_follower = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

    if user_follower == 'a':
        if C > D:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            return True
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            return False
    elif user_follower == 'b':
        if D > C:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            return True
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            return False
            exit()
    else:
        print(f"Invalid input. Final score: {current_score}")
        return False

follower(C,D)
# Game loop
is_game_on = True
while is_game_on:

    print(logo)
    # Move B to A
    random_dict_no_follower1 = random_dict_no_follower2

    # Print updated Compare A
    name1 = random_dict_no_follower1.get("name", "Unknown")
    description1 = random_dict_no_follower1.get("description", "Unknown")
    country1 = random_dict_no_follower1.get("country", "Unknown")
    print(f"Compare A: {name1}, a {description1}, from {country1}")

    print(vs)

    # Select a new B
    random_dict_no_follower2 = random.choice(data)
    D = random_dict_no_follower2.get("follower_count")

    name2 = random_dict_no_follower2.get("name", "Unknown")
    description2 = random_dict_no_follower2.get("description", "Unknown")
    country2 = random_dict_no_follower2.get("country", "Unknown")
    print(f"Against B: {name2}, a {description2}, from {country2}")

    # Check user answer
    is_game_on = follower(C, D)




