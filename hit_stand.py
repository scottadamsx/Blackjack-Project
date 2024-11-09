def hit_or_stand(deck, hand):
    while True:
        action = input("\nHit or stand? (hit/stand): ").lower()
        if action == 'hit':
            return action
        elif action == 'stand':
            return action
        else:
            print("Invalid input. Please enter 'hit' to Hit or 'stand' to Stand.")

