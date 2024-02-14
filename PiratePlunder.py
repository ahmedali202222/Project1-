import random

class PiratesPlunder:
    def __init__(self):
        self.treasure_chest = []
        self.bank_account = 1000  # Initial bank account balance

    def build_treasure_chest(self, items):
        self.treasure_chest.extend(items)

    def place_wager(self, wager):
        if wager <= 0:
            print("Invalid wager amount!")
            return False
        if wager > self.bank_account:
            print("Not enough funds to place wager!")
            return False
        return True

    def spin_treasure_chest(self):
        if not self.treasure_chest:
            print("The treasure chest is empty!")
            return None
        return random.choice(self.treasure_chest)

    def play_game(self, wager):
        if not self.place_wager(wager):
            return
        
        print("\nPlacing a wager of ${}...".format(wager))
        item = self.spin_treasure_chest()
        if item:
            print("You grabbed:", item)
            if item == 'diamond':
                print("Congratulations! You found a diamond! You win double your wager!")
                self.bank_account += wager
            else:
                print("Better luck next time!")
                self.bank_account -= wager
        else:
            print("Sorry, no items left in the treasure chest.")

        print("Current bank account balance: ${}".format(self.bank_account))

# Create an instance of PiratesPlunder
game = PiratesPlunder()

# Build the treasure chest with items
game.build_treasure_chest(['gold coin', 'silver coin', 'ruby', 'emerald', 'diamond'])

# Play the game multiple times with different wagers
game.play_game(100)  # First play with a $100 wager
game.play_game(200)  # Second play with a $200 wager
game.play_game(500)  # Third play with a $500 wager
