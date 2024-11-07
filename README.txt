

PROJECT FILE STRUCTURE

blackjack_project/
├── main.py              # Main entry point of the program
├── deck.py              # Module for deck-related functions
├── db.py                # Module for reading/writing player money
├── game_logic.py        # Module for game-specific functions
├── data/
│   └── money.txt        # Text file for storing player's money
└── README.md            # Project documentation


File and Module Breakdown



main.py

PROGRAM STRUCTURE

    initilize deck
    create a playerHand and dealerHand
    grab players money from file

    while game runs
        place bet

        deal 2 cards to player and dealer
        ask player if they want to hit or stand (call hit_or_stand function)
        


    
    



This will be the main entry point for running the game.
Initialize game settings and player money.
Set up game loop: handle each round of Blackjack where the player and dealer take turns.
Call functions for dealing cards, validating bets, and updating the player's money.




deck.py

This module will contain functions related to creating, shuffling, and managing the deck.
Key functions:
initialize_deck(): Initializes the deck with 52 cards.
shuffle_deck(deck): Shuffles the deck.
Card Representation: A list of cards where each card represents a list (with suit, rank, and point value).



db.py

Handles reading and writing the player’s money to money.txt.
Key functions:
read_money(): reads from the money.txt file
write_money(): writes new amount of money
This module should also handle file-related exceptions (e.g., missing money.txt).




game_logic.py


Contains the main game functions, such as validating bets, checking hand values, and handling Blackjack payouts.
Key functions:

buy_chips(): a function that prompts a user to buy more chips



data/money.txt

A simple text file to store the player's money between game sessions.
Start with a default amount, like 1000, if the file doesn’t exist.