from card import Card

class Deck(Card):
    cards = []
    card_titles = []
    def __init__(self):
        suit_counter = 0
        for suit in Card.POSSIBLE_SUIT:
            rank_counter = 0
            for rank in Card.POSSIBLE_RANK:
                card = Card(suit == Card.POSSIBLE_SUIT[suit_counter], rank == Card.POSSIBLE_RANK[rank_counter])
                self.cards.append(card)
                self.card_titles.append(card.card_title)


deck = Deck()

print(deck.card_titles)