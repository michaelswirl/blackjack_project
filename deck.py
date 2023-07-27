from card import Card
import random
from typing import Dict

class Deck():
    COUNT_VALUES: Dict[str, int] = {'A': -1, '2': 1, '3': 1,'4': 1,'5': 1, '6': 1,'7': 0,'8': 0,'9':0, '10':-1, 'J':-1,'Q':-1,'K':-1}
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
    def shuffle(self, times):
        random.seed = 46
        for i in range(times):
            random.shuffle(self.cards)
    def display(self):
        titles = []
        for c in self.cards:
            titles.append(c.card_title)
        return titles
    def deal(self):
        self.current_card = self.cards.pop(0)
        self.count += self.COUNT_VALUES[self.current_card.rank]
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
    def hit(self, player):
        card = self.deal()
        print(card.card_title)
        return card

        

