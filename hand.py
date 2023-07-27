from card import Card
from deck import Deck
from shoe import Shoe
from players import Player, Dealer, Gambler
import random

class Hand:
    ABOVE_21_RANK_VALUES = {'A': 1, '2': 2, '3': 3,'4': 4,'5': 5, '6': 6,'7': 7,'8': 8,'9':9, '10':10, 'J':10,'Q':10,'K':10}
    BELOW_21_RANK_VALUES = {'A': 11, '2': 2, '3': 3,'4': 4,'5': 5, '6': 6,'7': 7,'8': 8,'9':9,'10':10,  'J':10,'Q':10,'K':10}
    def __init__(self, name, player_cards):
        self.name = name
        self.hand = player_cards
        self.values = []
        self.ranks = []
        self.dealer_face_up_card = None
        self.dealer_face_down_card = None
        for card in player_cards:
            self.ranks.append(card.rank)
            value = Hand.BELOW_21_RANK_VALUES[card.rank]
            self.values.append(value)
        self.hand_value = sum(self.values)
        while self.hand_value > 21:
            if 11 in self.values:
                first_instance = self.values.index(11) 
                self.values[first_instance] = 1
                self.hand_value = sum(self.values)
    def get_value(self):
        return self.hand_value
    def add_card(self, card):
        self.hand.append(card)
        self.ranks.append(card.rank)
        value = Hand.BELOW_21_RANK_VALUES[card.rank]
        self.values.append(value)
        self.hand_value = sum(self.values)
        while self.hand_value > 21 and 11 in self.values:
            first_instance = self.values.index(11) 
            self.values[first_instance] = 1
            self.hand_value = sum(self.values)
    def display(self):
        card_titles = [card.card_title for card in self.hand]
        print(self.name + ' hand:')
        print(card_titles)
        print(self.hand_value)

            
                
#player_card_1 = Card(rank_index= 0,suit_index= 2)
#player_card_2 = Card(rank_index= 0,suit_index= 0)
#player_cards = [player_card_1,player_card_2]
#hand = Hand('Michael Curley',player_cards)

#hand.display()

