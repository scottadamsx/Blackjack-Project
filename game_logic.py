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

def buy_chips():
        chips = input("Would you like to buy more chips? (y/n): ").lower()
        if chips == 'y':
            try:
                amount = float(input("How much would you like to buy?: $"))
                money += amount
                db.write_money(money)
                print(f"You bought ${amount}. You now have: ${money}")
            except ValueError:
                print("Invalid input. You must enter a number.")
        else:
            print("Thanks for playing!")
        return money

def win_check(player_total, dealer_total, bet, money, hand):
    if len(hand) == 2 and player_total == 21:
        print("BLACKJACK!")
        payout = round(bet * 1.5, 2)
        money += payout
        db.write_money(money)
    elif dealer_total > 21 or player_total > dealer_total and player_total <= 21:
        print("You win!")
        payout = round(bet * 1.5, 2)
        money += payout
        db.write_money(money)
    elif player_total > 21 or dealer_total > player_total and dealer_total <=21:
        print("You lose!")
        money -= bet
        db.write_money(money)
    elif player_total == dealer_total:
        print("tie")
    return money

def place_bet(money):
    while True:
        try:
            bet = float(input(f"Money: ${money}\nBet amount:"))
            if bet >= 5 and bet <= 1000:
                print("Dealers show card:")
            elif bet > money:
                print("Bet can't be larger than your current money")
            else:
                print("error, bet cannot be less than 5, or more than 1000")
        except ValueError:
            print("Error: Please enter a valid integer.")
    
def hit_or_stand(deck, hand):
    while True:
        action = input("\nHit or stand? (hit/stand): ").lower()
        if action == 'h':
            hand.append(deck.pop())
            return True
        elif action == 's':
            return False
        else:
            print("Invalid input. Please enter 'h' to Hit or 's' to Stand.")