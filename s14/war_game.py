## generate the card
import random

# Two useful variables for creating Cards.
# suite = 'H D S C'.split()
# ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
deck = [];
# generate deck for each player
class Deck():
    suite = 'H D S C'.split()
    ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self,player1_deck=None,player2_deck=None):
        self.player1_deck = player1_deck;
        self.player2_deck = player2_deck;

    def get_deckof_cards(self):
        for sym in self.suite:
            for num in self.ranks:
                deck.append(sym+num)
        return deck

    def shuffle_deck(self):
        random.shuffle(deck)
        return deck

    def split_deck(self,s_deck):
        # random.shuffle(deck)
        player1_deck = s_deck[:26]
        player2_deck = s_deck[26:]
        return player1_deck,player2_deck













############################## Objects and the logic ##############################

############### ---------- <deck class object> ---------- ###############
gdeck = Deck();
## get the shuffled deck and the plyers deck split
full_deck = list(gdeck.get_deckof_cards())
shuffled_deck = list(gdeck.shuffle_deck())
players_deck = list(gdeck.split_deck(shuffled_deck))
print("Full Deck is : ",full_deck)
print("Shuffled Deck is : ",shuffled_deck)
print("Player 1 Deck is : ",players_deck[0])
print("Player 2 Deck is : ",players_deck[1])

############### ---------- </deck class object>---------- ###############
