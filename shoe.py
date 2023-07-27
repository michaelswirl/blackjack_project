from card import Card
from deck import Deck

class Shoe(Deck):
    def __init__(self,number_of_decks):
        self.num_of_cards = 0
        self.count = 0 
        self.decks = []
        self.cards = []
        for i in range(number_of_decks):
            self.deck = Deck()
            self.decks.append(self.deck)
            self.cards += self.deck.cards
    def add_deck(self):
        deck = Deck()
        self.decks.append(deck)
    def get_shoe_size(self):
        self.num_of_cards = len(self.cards)
        return self.num_of_cards

#shoe = Shoe(8)

# use this to test
#print(shoe.count)
#print(len(shoe.cards))
#print(shoe.display())
#print(len(shoe.decks))
#print(shoe.decks)