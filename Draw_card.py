#Draw a card project
import random

def create_deck(): #function to reuse the deck
    suits = ["♥", "♦", "♣", "♠"] #4 suits
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #13 ranks
    deck = [(suit, rank) for suit in suits for rank in ranks] #card creation
    random.shuffle(deck)
    return deck

def draw_card(deck): #function to draw a card from the deck
    hand = [deck[-1]]
    deck.pop()
    return hand, deck

deck = create_deck()

while len(deck) > 0: #loop to draw cards until deck is empty
    input("Press enter to draw the next card") #waits for user to draw a card
    hand, deck = draw_card(deck)
    print(f"Your card is {hand[0]}")

print("We are out of cards")
