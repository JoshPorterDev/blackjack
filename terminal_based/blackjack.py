from deck import Deck
import sys

class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.playerBalance = 100
        self.houseBalance = 1000

    def playHand(self):
        total = 0
        choice = " "

        initialCard = self.deck.drawCard()
        initialCardValue = initialCard.getNumericValue()
        total += initialCardValue

        print(initialCard)
        print(total)

        while choice != 'p' or total < 21:
            choice = input("\nHit, Pass, Or Double (h, p, d) ")

            if choice == 'h':
                card = self.deck.drawCard()
                cardValue = card.getNumericValue()
                total += cardValue
                print(f"You drew a {card}")
                print(f"Total is now: {total}")

                if total == 21:
                    print("Perfect")
                    break


                elif total > 21:
                    print("You busted")
                    break


            elif choice == 'd':
                card = self.deck.drawCard()
                cardValue = card.getNumericValue()
                total += cardValue
                print(f"You finished with a {total}")
                break

            elif choice == 'p':
                print(f"You finished with a {total}")
                break

        return total

    def houseHand(self):
        total = 0
        busted = False
        shownCard = self.deck.drawCard()
        shownCardValue = shownCard.getNumericValue()
        total += shownCardValue

        while total < 21:
            card = self.deck.drawCard()
            cardValue = card.getNumericValue()
            total += cardValue

            if total == 21:
                break

            if total > 21:
                break

        return total




    def test(self, playerScore, houseScore, wager):
        print(f"\nYou scored a {playerScore}")
        print(f"House scored a {houseScore}")

        if playerScore > 21 and houseScore > 21:
            print("No one wins")

        elif playerScore <= 21 and houseScore > 21:
            print("You win!")
            self.playerBalance += wager
            self.houseBalance -= wager

        elif playerScore > houseScore and playerScore <= 21:
            print("You win!")
            self.playerBalance += wager
            self.houseBalance -= wager

        elif playerScore == houseScore:
            print("push")

        elif houseScore > playerScore and houseScore <= 21:
            print("House wins")
            self.playerBalance -= wager
            self.houseBalance += wager

        print(f"You have ${self.playerBalance}")
        print(f"House has ${self.houseBalance}")

    def playRound(self):
        wager = int(input(f"How much would you like to wager? (10 - {self.playerBalance}) "))
        self.deck.shuffleDeck()
        playerHand = self.playHand()
        houseHand = self.houseHand()
        self.test(playerHand, houseHand, wager)

    def main(self):
        ans = input("Do you want to play blackjack? (y/n) ")

        while ans == 'y':
            self.deck = Deck() # If the user wants to play another hand, we create a new, full deck to play with
            self.deck.shuffleDeck() # Shuffle the new deck
            self.playRound()
            ans = input("\nDo you want to play another hand? (y/n) ")

        print("Thanks for playing")
        print(f"You took home ${self.playerBalance}")
        sys.exit()


game = Blackjack()

game.main()
