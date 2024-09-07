import unittest
from card_game_helper import get_point_value

class CardGameHelperTest(unittest.TestCase):

    def test_get_point_value_joker(self):
        self.assertEqual(50, get_point_value('Joker'))

    def test_get_point_value_two(self):
        self.assertEqual(20, get_point_value('Two', 'Red'))

    def test_get_point_value_two(self):
        self.assertEqual(20, get_point_value('Two', 'Black'))

    def test_get_point_value_ace(self):
        self.assertEqual(20, get_point_value('Ace', 'Black'))

    def test_get_point_value_nine(self):
        self.assertEqual(10, get_point_value('Nine', 'Black'))

    def test_get_point_value_ten(self):
        self.assertEqual(10, get_point_value('Ten', 'Red'))

    def test_get_point_value_jack(self):
        self.assertEqual(10, get_point_value('Jack', 'Red'))

    def test_get_point_value_queen(self):
        self.assertEqual(10, get_point_value('Queen', 'Red'))

    def test_get_point_value_king(self):
        self.assertEqual(10, get_point_value('King', 'Red'))

    def test_get_point_value_four(self):
        self.assertEqual(5, get_point_value('Four', 'Red'))

    def test_get_point_value_five(self):
        self.assertEqual(5, get_point_value('Five', 'Black'))

    def test_get_point_value_six(self):
        self.assertEqual(5, get_point_value('Six'))

    def test_get_point_value_seven(self):
        self.assertEqual(5, get_point_value('Seven'))

    def test_get_point_value_eight(self):
        self.assertEqual(5, get_point_value('Eight', 'Red'))

    def test_get_point_value_black_three(self):
        self.assertEqual(5, get_point_value('Three', 'Black'))

    def test_get_point_value_three(self):
        self.assertEqual(0, get_point_value('Three', 'Red'))

    def test_get_point_value_bad_color(self):
        self.assertEqual(-1, get_point_value('Three', 'Purple'))

    def test_get_point_value_bad_rank(self):
        self.assertEqual(-1, get_point_value('Iris', 'Purple'))

if __name__ == '__main__':
    unittest.main()