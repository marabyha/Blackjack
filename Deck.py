from itertools import product
from random import shuffle

from const import RANKS, SUITS


class Card:
    def __init__(self, rank, points):
        self.rank = rank
        self.points = points

    def __str__(self):
        message = 'Points: ' + str(self.points)
        # message = self.picture + '\nPoints: ' + str(self.points)
        return message


class Deck:

    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    @staticmethod
    def _generate_deck():
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            c = Card(rank=rank, points=points)
            cards.append(c)
        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def new_deck(self):
        self.cards.clear()
        self.cards = self._generate_deck()
