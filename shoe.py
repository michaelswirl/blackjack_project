from card import Card
from deck import Deck

class Shoe(Deck):
    decks = []
    def __init__(self,number_of_decks):
        for i in range(1,number_of_decks):
            deck = Deck()
            self.decks.append(deck)

Shoe(8)

print(Shoe.cards)
