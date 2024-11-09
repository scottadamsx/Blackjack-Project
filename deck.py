#! usr\bin\env python3
import random

# initializes the deck for every round 
def initialize_deck():
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    deck = []

    for suit in suits:
        for rank in ranks:
            if rank == "King" or rank == "Queen" or rank == "Jack":
                value = 10
            elif rank == "Ace":
                value = 0
            else:
                value = int(rank)

            card = [suit,rank,value]
            deck.append(card)

    return deck

# shuffles the deck 
def shuffle_deck(deck):
    shuffledDeck = random.shuffle(deck)
    return shuffledDeck

# pops a card from the deck into a hand variable, dev decides which hand to place the card in
def deal_card(hand, deck, numOfCards=1):
    for i in range(numOfCards):
        card = random.choice(deck)
        deck.pop(card)
        hand.append(card)




