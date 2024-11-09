import db

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



def win_check(playerTotal, dealerTotal, bet, money, playerHand, dealerHand):
    # instance where YOU gets a natural blackjack
    if len(playerHand) == 2 and playerTotal == 21:
        print("BLACKJACK!")
        payout = round(bet * 1.5, 2)
        money += payout
        db.write_money(money)

    # instance where dealer gets a natural blackjack
    elif len(dealerHand) == 2 and dealerTotal == 21:
        print("You lose!")
        money -= bet
        db.write_money(money)

    # instance where the dealer busts OR the player beats the dealer in value but DOESNT bust
    elif dealerTotal > 21 or playerTotal > dealerTotal and playerTotal <= 21:
        print("You win!")
        payout = round(bet * 1.5, 2)
        money += payout
        db.write_money(money)

    # instance where you bust or the dealer beats the player in value
    elif playerTotal > 21 or dealerTotal > playerTotal and dealerTotal <=21:
        print("You lose!")
        money -= bet
        db.write_money(money)
    
    elif playerTotal == dealerTotal:
        print("tie")


    return money



def place_bet(money):
    while True:
        try:
            bet = float(input("Bet amount:"))
            if bet >= 5 and bet <= 1000:
                return bet
                break
            elif bet > money:
                print("Bet can't be larger than your current money")
            else:
                print("error, bet cannot be less than 5, or more than 1000")
        except ValueError:
            print("Error: Please enter a valid integer.")



def calculate_total(hand):
    total = sum(card[2] for card in hand)
    return total



def check_for_ace(hand):
    total = calculate_total(hand)
    for card in hand:
        if card[1] == "Ace":
            ace_choice = int(input("Do you want this Ace to be a 1 or 11?: "))
            if ace_choice == 11 and total + 11 <= 21:
                card[2] = 11
            else:
                card[2] = 1
    



def hit_or_stand(deck, hand):
    while True:
        action = input("\nHit or stand? (hit/stand): ").lower()
        if action == 'hit':
            return action
        elif action == 'stand':
            return action
        else:
            print("Invalid input. Please enter 'hit' to Hit or 'stand' to Stand.")