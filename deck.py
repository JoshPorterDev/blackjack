import random
from card import Card

suits = ['spades', 'clubs', 'diamonds', 'hearts']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

class Deck:

    def __init__(self):
        self.deck = []
        for value in values:
            for suit in suits:
                self.deck.append(Card(value, suit))

    def __str__(self):
        return str([str(card) for card in self.deck])

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def drawCard(self):
        return self.deck.pop()
