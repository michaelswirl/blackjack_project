from card import Card
import random

class Deck():
    cards = []
    def __init__(self):
        self.suit_counter = 0
        for suit in Card.POSSIBLE_SUIT:
            self.rank_counter = 0
            for rank in Card.POSSIBLE_RANK:
                card = Card(suit_index = self.suit_counter, rank_index = self.rank_counter)
                self.cards.append(card)
                self.rank_counter += 1
            self.suit_counter += 1
    def shuffle(self):
        random.seed = 46
        random.shuffle(self.cards)
    def display(self):
        titles = []
        for c in self.cards:
            titles.append(c.card_title)
        return titles
    
deck = Deck()
deck.shuffle()
print(deck.display())
deck.shuffle()
print(deck.display())
