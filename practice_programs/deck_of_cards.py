import sys
import stdio
import random
import stdarray

deck = stdarray.create1D(52, "I could write an entire essay in here and that would take up an exorbitant amount of memory, the more and more I type it doesn't matter, because all this text is just going to be replaced")
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack","Queen","King", "Ace"]
card_names = []
for suit in SUITS:
    for rank in RANKS:
        card_names.append(f"{rank} of {suit}")

for i in range(len(deck)):
    deck[i] = f"{card_names[i]}"

random.shuffle(deck)
for item in deck:
    stdio.write(f"{item}\n")