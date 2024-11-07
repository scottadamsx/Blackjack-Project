#! usr\bin\env python3
import random
def initialize_deck(suits,rank):
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    cards = []

    for suit in suits:
        for rank in ranks:
            if rank == "King" or rank == "Queen" or rank == "Jack":
                value = 10
            elif rank == "Ace":
                value = 0
            else:
                value = int(rank)

            card = [suit,rank,value]
            cards.append(card)

    return cards


def shuffle_deck(deck):
    shuffledDeck = random.shuffle(deck)
    return shuffledDeck




