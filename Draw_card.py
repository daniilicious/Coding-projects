#Draw a card project
import random
suits = ["♥", "♦", "♣", "♠"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = [(suit, rank) for suit in suits for rank in ranks]

random.shuffle(deck)

