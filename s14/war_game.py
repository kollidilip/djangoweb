## generate the card
import random

# Two useful variables for creating Cards.
# suite = 'H D S C'.split()
# ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
deck = [];
############################################################
class Deck:
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
    pass
############################################################
############################################################
class Hand:

    def __init__(self,player_name):
        self.player_name = player_name

    def add_card_fromhand(self,pl_current_deck,cards_to_add):
        self.pl_current_deck = pl_current_deck
        self.cards_to_add = cards_to_add

        ## adding cards to the current deck of player
        for i in self.cards_to_add:
            self.pl_current_deck.append(i)
        return pl_current_deck

    def remove_card_fromhand(self,pl_current_deck,cards_to_delete):
        self.pl_current_deck = pl_current_deck
        self.cards_to_delete = cards_to_delete

        ## adding cards to the current deck of player
        for i in self.cards_to_delete:
            self.pl_current_deck.remove(i)
        return pl_current_deck

    pass
############################################################
############################################################
class Player:

    def __init__(self,playername,playerhand):
        self.playername = playername;
        self.playerhand = playerhand;


    pass


############################## Objects and the logic ##############################
# generate deck for each player
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


# Each player has a Hand
p1_hand = Hand("player1");
print("Player 1 name : ", p1_hand.player_name)
p2_hand = Hand("player2");
print("Player 2 name : ", p2_hand.player_name)
# add card to players Hand based on the result of whether to add or remove
cards_to_add_delete = ['to delete1', 'to delete2']

## if player 1 wins
p1_deck_afterHand = list(p1_hand.add_card_fromhand(players_deck[0],cards_to_add_delete))
p2_deck_afterHand = list(p2_hand.remove_card_fromhand(players_deck[1],cards_to_add_delete))

## if player 2 wins
# p1_deck_afterHand = list(p1_hand.remove_card_fromhand(players_deck[0],cards_to_add_delete))
# p2_deck_afterHand = list(p2_hand.add_card_fromhand(players_deck[1],cards_to_add_delete))

print(p1_deck_afterHand)
print(p2_deck_afterHand)
