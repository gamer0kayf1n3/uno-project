import unittest
from models.exceptions import *
from models.card import Card

class TestCard(unittest.TestCase):
    def test_HoldsColorAndFunction(self):
        card = Card(0, 3)
        self.assertEqual(card.color, 0)
        self.assertEqual(card.function, 3)
    
    def test_ColorValues(self):
        self.assertEqual(len(Card._color_dictionary), 5)

    def test_FunctionValues(self):
        self.assertEqual(len(Card._function_dictionary), 15)

    def test_FunctionValues(self):
        self.assertEqual(len(Card._function_dictionary), 15)
    
    def test_ValidColorRange(self):
        try: Card(0, 3)
        except Exception as e: self.fail(f"Threw an error {e}")

        with self.assertRaises(Exception):
            Card(10, 3)

    def test_ValidFunctionRange(self):
        try: Card(0, 3)
        except Exception as e: self.fail(f"Threw an error {e}")

        with self.assertRaises(Exception):
            Card(0, 18)
    
    def test_ValidColorCard(self):
        try: Card(0, 3)
        except Exception as e: self.fail(f"Threw an error {e}")

        with self.assertRaises(Exception):
            Card(2, 14)

    def test_ValidBlackCard(self):
        try: Card(4, 14)
        except Exception as e: self.fail(f"Threw an error {e}")

        with self.assertRaises(Exception):
            Card(4, 2)
    
    def test_CardRepr(self):
        card = Card(3, 9)
        self.assertEqual(repr(card), "Yellow 9")

        card = Card(4, 14)
        self.assertEqual(repr(card), "Black Draw 4")
    
    def test_CardEquality(self):
        card1 = Card(1, 4)
        card2 = Card(1, 4)
        badCard = Card(2, 4)

        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, badCard)

if __name__ == '__main__':
    unittest.main()
