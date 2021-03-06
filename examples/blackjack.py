""" This is a simple implementation of a blackjack game.  The basic rules are:
the dealer deals you cards, starting with two, then adding one if you "hit".
Your goal is to reach, but not exceed, 21 points.  If the dealer has more
points than you without going over 21, they win.  If you have more points than
the dealer without going over 21, you win. """

import random

# my_deck = [('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts')...]

VALUES = [(str(num), num) for num in range(2,11)]
VALUES.extend([('J', 10), ('Q', 10), ('K', 10), ('A', 11)])

SUITS = ['diamonds', 'hearts', 'spades', 'clubs']

def make_deck():
    """ return a deck of card tuples """
    this_deck = []
    for suit in SUITS:
        for value in VALUES:
            this_card = (value[0], suit)
            this_deck.append(this_card)
    return this_deck


def deal_cards(deck, player1, player2):
    """ deal cards from the deck list, out to each of the players.  no return
    value """
    for _ in range(2):
        for player in (player1, player2):
            deal_card(deck, player)


def deal_card(deck, player_hand):
    """ deal a single card.  no return value. """
    this_card = deck[-1]
    player_hand.append(this_card)
    del(deck[-1])


def get_player_input(deck, hand):
    """ let the player hit as many times as they want """
    # show the player their hand
    answer = ''
    while answer != 's':
        print('Your cards:')
        points = get_hand_value(hand)
        for card in hand:
            print(card)
        print(f'You have {points} points')
        if points > 21:
            print('Bust!')
            return
        answer = input('Hit or stay? (h or s) ')
        if answer == 'h':
            deal_card(deck, hand)
    print('Your final hand:')
    for card in hand:
        print(card)


def get_dealer_hand(deck, hand):
    """ figure out the dealer's hand """
    while True:
        points = get_hand_value(hand)
        if points < 19:
            deal_card(deck, hand)
        elif points > 21:
            return "Bust"
        else:
            break


def get_hand_value(hand):
    """ determine the value of a hand """
    points = 0
    for card in hand:
        points += get_points(card)
    return points

def get_points(card):
    """ pass in a card tuple (value, suit), and return the number of points
    it's worth """
    value = card[0]
    for item in VALUES:
        if item[0] == value:
            return item[1]


def main():
    """ run the game """
    my_deck = make_deck()
    random.shuffle(my_deck)
    player_hand = []
    dealer_hand = []
    deal_cards(my_deck, player_hand, dealer_hand)
    # now, player and dealer each have two cards

    get_player_input(my_deck, player_hand)
    dealer_result = get_dealer_hand(my_deck, dealer_hand)
    print("Dealer's hand:")
    for card in dealer_hand:
        print(card)
    player_points = get_hand_value(player_hand)
    dealer_points = get_hand_value(dealer_hand)
    print(f"Dealer has {dealer_points} points")
    if dealer_result == "Bust":
        print("Dealer busts, you win!")
    else:
        if dealer_points > player_points:
            print("Dealer wins!")
        else:
            print("You win!")


def test_deal_cards():
    print('testing the deal_cards function')
    my_deck = make_deck()
    expected_player1 = []
    expected_player2 = []
    expected_player1.append(my_deck[-1])
    expected_player2.append(my_deck[-2])
    expected_player1.append(my_deck[-3])
    expected_player2.append(my_deck[-4])
    player1 = []
    player2 = []
    deal_cards(my_deck, player1, player2)
    print('checking assertions')
    assert(expected_player1[0] == player1[0])
    assert(expected_player1[1] == player1[1])
    assert(expected_player2[0] == player2[0])
    assert(expected_player2[1] == player2[1])


if __name__ == '__main__':
    main()
    #test_deal_cards()
