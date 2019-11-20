import random
from card import Card

suits = ['spades', 'clubs', 'diamonds', 'hearts']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

numericValues = {'ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10}

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

    def getRank(self):
        pass

    def getLength(self):
        return len(self.deck)
