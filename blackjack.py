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
            choice = input("Hit, Pass, Or Double (h, p, d) ")

            if choice == 'h':
                card = self.deck.drawCard()
                cardValue = card.getNumericValue()
                total += cardValue
                print(f"You drew a {card}")
                print(f"total is {total}")

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




    def test(self, playerScore, houseScore):
        print(f"You scored a {playerScore}")
        print(f"House scored a {houseScore}")

        if playerScore > 21 and houseScore > 21:
            print("No one wins")

        elif playerScore <= 21 and houseScore > 21:
            print("Player wins")

        elif playerScore > houseScore and playerScore <= 21:
            print("\nYou win!")

        elif playerScore == houseScore:
            print("push")

        elif houseScore > playerScore and houseScore <= 21:
            print("House wins")

    def playRound(self):
        self.deck.shuffleDeck()
        playerHand = self.playHand()
        houseHand = self.houseHand()
        self.test(playerHand, houseHand)

    def main(self):
        ans = input("Do you want to play blackjack? (y/n) ")

        while ans == 'y':
            self.deck.shuffleDeck()
            self.playRound()
            ans = input("Do you want to play another hand? (y/n) ")

        print("Thanks for playing")
        sys.exit()


game = Blackjack()

game.main()
