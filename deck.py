from card import Card
import random

class Deck():
    def __init__(self):
        self.current_card = None
        self.count = None
        self.cards = []
        self.suit_counter = 0
        for suit in Card.POSSIBLE_SUIT:
            self.rank_counter = 0
            for rank in Card.POSSIBLE_RANK:
                card = Card(suit_index = self.suit_counter, rank_index = self.rank_counter)
                self.cards.append(card)
                self.rank_counter += 1
            self.suit_counter += 1
        self.count = len(self.cards)
    def shuffle(self):
        random.seed = 46
        random.shuffle(self.cards)
    def display(self):
        titles = []
        for c in self.cards:
            titles.append(c.card_title)
        return titles
    def deal(self):
        self.current_card = self.cards.pop(0)
        self.count = len(self.cards)
    
deck = Deck()
print("Number of Cards in Deck:")
print(deck.count)
print("Unshuffled Deck:")
print(deck.display())
print("Shuffled Deck:")
deck.shuffle()
print(deck.display())
deck.deal()
print("Dealt Card:")
print(deck.current_card.card_title)
print("Number of Cards Left in Deck:")
print(len(deck.cards))
print("Remaining Deck:")
print(deck.display())

