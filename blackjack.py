from deck import Deck
import sys

class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.playerBalance = 100
        self.houseBalance = 1000

    def main(self):
        ans = input("Do you want to play blackjack? (y/n) ")

        if ans == 'y':
            self.deck.shuffleDeck()
            print(f"You drew a {self.deck.drawCard()}")
            print(f"You have ${self.playerBalance}")
            print(f"The house has ${self.houseBalance}")

        if ans == 'n':
            print("Thanks for playing")
            sys.exit()


game = Blackjack()

game.main()
