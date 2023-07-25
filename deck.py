from card import Card
import random

class Deck():
    cards = []
    card_titles = []
    def __init__(self):
        self.suit_counter = 0
        for suit in Card.POSSIBLE_SUIT:
            self.rank_counter = 0
            for rank in Card.POSSIBLE_RANK:
                card = Card(suit_index = self.suit_counter, rank_index = self.rank_counter)
                self.cards.append(card)
                self.card_titles.append(card.card_title)
                self.rank_counter += 1
            self.suit_counter += 1
    def shuffle(self):
        random.seed = 46
        random.shuffle(self.cards)
        random.shuffle(self.card_titles)
    
deck = Deck()

print(deck.card_titles)
print(len(deck.cards))

deck.shuffle()

print(deck.card_titles)
