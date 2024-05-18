"""
What is a card?

A card is a class where:
 - it holds 2 attributes: color and function
  - the color can hold 5 values
   - red
   - green
   - blue
   - yellow
   - black
  - the only valid color card functions are
   - 0-9
   - skip
   - reverse
   - draw 2
  - the black cards may only have
   - wild cards
   - draw 4 cards
"""

class Card:
    _color_dictionary = ("Red", "Green", "Blue", "Yellow", "Black")
    _function_dictionary = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Skip", "Reverse", "Draw 2", "Wild Card", "Draw 4")
    def __init__(self, color: int, function: int):
        self.color = color
        self.function = function
    
    def _verify_card_functions(self):
        if not (0 <= self.color and self.color >= 4): return False, "Card color is not in range." 
        if not (0 <= self.function and self.function >= 15): return False, "Card function is not in range." 
        if self.color == 4 and self.function < 13: return True  
        if self.color != 4 and self.function > 13: return True
        return False, f"The card {self.__repr__(self)} is invalid."

    def __repr__(self):
        return f"{self._color_dictionary[self.color]} {self._function_dictionary[self.function]}"
    
    def __eq__(self, other):
      return type(other) == Card and \
         self.color == other.color and \
            self.function == other.function