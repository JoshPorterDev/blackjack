numericValues = {'ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10}

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def showRank(self):
        return self.rank

    def getNumericValue(self):
        return numericValues[self.rank]

    def test(self):
        number = numericValues[self.rank]

        return f"{self.suit} {number}"
