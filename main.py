#! usr/bin/env python3

# import all the modules
import db
import random
from deck import *


# a simple function that displays the opening message when the program loads up
def display_title():
    print("BLACKJACK! \nBlackjack payout is 3:2\n")

# creates deck and shuffles it for the round, deals two cards to the dealer and player, and asks for an initial bet
def start_round(playerMoney):

    deck = initialize_deck()

    print(f"money: {playerMoney}")
    bet = float(input("bet amount: "))

    playerHand = []
    deal_card(playerHand, deck, 2)
    dealerHand = []
    deal_card(dealerHand, deck, 2)

    # include the display of the first data

    return playerHand, dealerHand, bet






# ==========================================================================================
def main(): 

    display_title()

    playerMoney = db.read_money()
    print("player has: ", playerMoney)

    playerHand, dealerHand, bet = start_round(playerMoney)
    print(playerHand, dealerHand, bet)

if __name__ == "__main__":
    main()