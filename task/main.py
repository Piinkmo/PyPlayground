import random
import art

'''Deal two cards to players first.'''
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

'''Calculate total scores'''
def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

'''Main game'''
def main_game():
    print(art.logo)
    player_hand = [deal_cards(), deal_cards()]
    dealer_hand = [deal_cards(), deal_cards()]

    print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
    print(f"Computer's first card: {dealer_hand[0]}")

    if calculate_score(player_hand) == 21:
        print("Win with a BlackJack!")
        return
    if calculate_score(dealer_hand) == 21:
        print(f"You lose... Dealer's card: {dealer_hand}, dealer has BlackJack.")
        return


    '''Player Round'''
    while calculate_score(player_hand) < 21:
        action = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if action == 'y':
            player_hand.append(deal_cards())
            print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
        else:
            break

    if calculate_score(player_hand) > 21:
        print("You went over. You lose 😭")
        return


    '''Dealer Round'''
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_cards())

    print(f"Dealer cards: {dealer_hand}, dealer current score: {calculate_score(dealer_hand)}")

    if calculate_score(dealer_hand) > 21 or calculate_score(player_hand) > calculate_score(dealer_hand):
        print("Player win! 😄")

    elif calculate_score(player_hand) < calculate_score(dealer_hand):
        print("Dealer win! You lose. 😭")

    else:
        print("Draw")

main_game()



