class Card:
    POSSIBLE_RANK = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
    POSSIBLE_SUIT = ['Clubs','Spades','Hearts','Diamonds']
    suit = ''
    rank = ''
    card_title = ''
    def __init__(self,rank_index,suit_index):
        self.rank = self.POSSIBLE_RANK[rank_index]
        self.suit = self.POSSIBLE_SUIT[suit_index]
        self.card_title = [self.suit, self.rank]
   