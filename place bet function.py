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
