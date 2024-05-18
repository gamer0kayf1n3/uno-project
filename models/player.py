"""
What is a player?

A player is a class where:
 - it has a name
 - it has a set of cards
 - it can perform actions that can significantly modify the deck and the round
  - place a card on the working deck
   - given that it is checked that the card placed is a card that the player actually owns
   - given that the card placed by the player is a valid one
  - pull a card from the pull deck
  - when a player places a wild card, the player must have an option to change the color
  - the player must be given cards on start of the round
  - its cards must be placed on the pull deck if disconnected
  - it can win when the player runs out of cards
  - it can spectate the round
"""