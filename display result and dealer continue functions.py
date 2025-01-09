def display_result(playerTotal, dealerTotal, dealerHand):
    print("DEALER'S CARDS:")
    for card in dealerHand:
        print(f"{card[1]} of {card[0]}")
    print("")

    print(f"YOUR POINTS:\t {playerTotal}")
    print(f"DEALER'S POINTS: {dealerTotal}")

def dealer_continue(dealerTotal, dealerHand, deck):
    while dealerTotal < 17:
            dealerHand.append(deck.pop())
            dealerTotal = calculate_total(dealerHand)
