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
