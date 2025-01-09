def check_for_ace(hand):
    total = calculate_total(hand)
    for card in hand:
        if card[2] == 0:
            ace_choice = int(input("Do you want this Ace to be a 1 or 11?: "))
            if ace_choice == 11 and total + 11 <= 21:
                card[2] = 11
            else:
                card[2] = 1
    
