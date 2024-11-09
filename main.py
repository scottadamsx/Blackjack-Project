#! usr/bin/env python3

# import all the modules
import db


# a simple function that displays the opening message when the program loads up
def display_title():
    print("BLACKJACK! \nBlackjack payout is 3:2\n")







# ==========================================================================================
def main(): 

    display_title()

    playerMoney = db.read_money()
    print("player has: ", playerMoney)

if __name__ == "__main__":
    main()