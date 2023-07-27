from card import Card
import random

class Deck():
    def __init__(self):
        self.current_card = None
        self.count = 0
        self.cards = []
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
    def deal(self):
        self.current_card = self.cards.pop(0)
        self.count = len(self.cards)
        return self.current_card
    def deal_to_table(self, table, dealer):
        dealer.cards.append(self.deal())
        for i in range(0,2):
            for player in table.values():
                if player is None:
                    pass
                else:
                    card = self.deal()
                    player.cards.append(card)
        dealer.cards.append(self.deal())
        

