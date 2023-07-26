from card import Card
from deck import Deck
from shoe import Shoe
from players import Player, Dealer, Gambler
import random




class Game:
    def __init__(self,num_of_players, num_of_decks,min_bet,max_bet):
        """Establishes a blackjack table that generates random players sitting in seats at the table."""
        self.table = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}
        self.minimum_bet = min_bet
        self.maximum_bet = max_bet
        self.first_index = random.randint(0,99)
        self.last_index = random.randint(0,99)
        self.dealer = Dealer(first=Dealer.POSSIBLE_FIRST_NAMES[self.first_index],
                        last=Dealer.POSSIBLE_LAST_NAMES[self.last_index])
        self.counter = 1
        for gambler in range(num_of_players):
            first_index = random.randint(0,99)
            last_index = random.randint(0,99)
            bankroll = random.randint((min_bet*10),(min_bet*30))
            gambler = Gambler(
                first=Gambler.POSSIBLE_FIRST_NAMES[first_index],
                last=Gambler.POSSIBLE_LAST_NAMES[last_index],
                bank = bankroll,
                position = self.counter,
                min= self.minimum_bet,
                max=self.maximum_bet
                )
            self.table[self.counter] = gambler
            self.counter += 1
        self.shoe = Shoe(num_of_decks)
    def display_table(self):
        for seat, player in self.table.items():
            print("Seat number: " + str(seat))
            print("Player name: " + player.full_name)
            print("Bankroll: " + str(player.bankroll))
            print("Current Hand: " + ', '.join(player.current_cards))

    


game = Game(num_of_players=7,num_of_decks=8,min_bet=2,max_bet=10)
print(game.display_table())





            

            




