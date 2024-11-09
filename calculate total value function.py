def calculate_total(hand):
    total = sum([card[2] for card in hand if card[1] != "Ace"])
    aces = [card for card in hand if card[1] == "Ace"]
    while aces:
        ace_choice = int(input("Do you want this Ace to be a 1 or 11?: "))
        if ace_choice == 11 and total + 11 <= 21:
            total += 11
        else:
            total += 1
        break
    return total
