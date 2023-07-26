from card import Card
from deck import Deck

class Shoe(Deck):
    def __init__(self,number_of_decks):
        self.decks = []
        self.cards = []
        for i in range(number_of_decks):
            self.deck = Deck()
            self.decks.append(self.deck)
            self.cards += self.deck.cards
            self.count = len(self.cards)
    def add_deck(self):
        deck = Deck()
        self.decks.append(deck)

shoe = Shoe(8)

print(shoe.count)
print(len(shoe.cards))
print(shoe.display())
print(len(shoe.decks))
print(shoe.decks)