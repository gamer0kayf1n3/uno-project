"""
What is a round?

A round is a class where:
 - it holds the players, the deck, and all events that might occur
 - the round must wait for its players
 - the round must shuffle the cards in the start and every time a card is placed; except when a draw card is placed, and a player must pull
 - when a wild card is placed, the player must have an option to change the color of the allowed next card
 - a round must be able to follow skip and reverse cards
 - a round must verify if the card placed is a valid card
 - a round must know who must be the next player to place a card
 - a round must keep history of everything and save it in bytecode and base64
 - a round must acknowledge the order of which players win
 - a round must end once the second to last player wins
"""