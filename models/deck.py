"""
What is a deck?

A deck is a class where:
 - it is specific to a round
 - it holds all the possible cards (112)
  - 26 of each color (2 0-9s, 2 skips, 2 reverses, and 2 draw 2s) (104)
  - 8 black cards (4 wildcards and 4 draw 4s) (8)
  - total: 112
 - it holds the working deck
 - it holds the pull deck
 - it must ensure that all the cards are still in the system
 - it must shuffle the card first
 - it must distribute the cards to each player
 - it must distribute cards to the next player when a draw card is placed
"""