import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(cards)

def boom(hand):
    if sum(hand) > 21:
        return True
    return False

def win(players):
    hand = []
    maximum = 0
    max_hand = []
    draw = False
    for player in players:
        if not boom(player):
            hand.append(player)
    for subHands in hand:
        if sum(subHands) > maximum:
            maximum = sum(subHands)
            max_hand = subHands
            draw = False
        elif sum(subHands) == maximum:
            draw = True
    if draw:
        print("It is a Draw.")
    else:
        print(f"Player {players.index(max_hand)+1} Wins with hand {max_hand} which has total score of {maximum}")


def player(n):
    player_hand = []
    print(f"Welcome, you are player {n}")
    for i in range(2):
        player_hand.append(draw_card())
        print(f"You drew card {player_hand[i]}")
        print(f"Your current hand is {player_hand}")
    while True:
        continue_draw = input("Do you want to draw another card? Y/N ").upper()
        if continue_draw == "Y":
            player_hand.append(draw_card())
            print(f"You drew card {player_hand[-1]}")
            print(f"Your current hand is {player_hand}")
        if continue_draw == "N":
            break
        if 11 in player_hand and sum(player_hand) > 21:
            player_hand[player_hand.index(11)] = 1
        elif sum(player_hand) > 21:
            print("Boom, You lose.")
            break
        else:
            print("Only enter Y or N ")
    return player_hand

def play_the_game():
    print(logo)
    player_list = []
    player_number = int(input("Welcome! How many players would you like to have in the game? "))
    for num in range(player_number):
        player_list.append(player(num+1))
    win(player_list)

play_the_game()