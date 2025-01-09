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
