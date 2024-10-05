import random
from art import logo, vs
from game_data import data

def get_entries():
    entry1 = random.choice(data)
    entry2 = random.choice(data)

    while entry1 ==  entry2:
        entry2 = random.choice(data)

    return entry1, entry2

def display_entries(entry1, entry2):
    print(logo)
    print(f"Compare A: {entry1['name']}, a {entry1['description']}, from {entry1['country']}")
    print(vs)
    print(f"Against B: {entry2['name']}, a {entry2['description']}, from {entry2['country']}")

def get_user_guess():
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return guess

def check_guess(guess, entry1, entry2):
    if (guess == 'A' and entry1['follower_count'] > entry2['follower_count']) or \
        (guess == 'B' and entry2['follower_count'] > entry1['follower_count']):
        return True
    else:
        return False

def update_score(current_score, correct):
    if correct:
        return current_score + 1
    else:
        return current_score


'''Main Game'''
def play_game():
    score = 0

    while True:
        entry1, entry2 = get_entries()
        display_entries(entry1, entry2)

        guess = get_user_guess()
        correct = check_guess(guess, entry1, entry2)

        score = update_score(score, correct)

        if correct:
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. {entry1['name']} has {entry1['follower_count']}M followers and {entry2['name']} has {entry2['follower_count']}M followers.")
            print(f"Game over! Your final score is: {score}")
            break


play_game()



