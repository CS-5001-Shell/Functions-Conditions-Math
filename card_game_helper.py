"""
One of my favorite card games is called Hand and Foot. The goal of the game is to generate piles of cards of the same rank. Cards with different ranks have different values. For this question, you will implement a Hand and Foot helper that will prompt the user for a card rank and will output the value for the given card. The value for each rank is as follows:

Jokers - 50 points
Twos & Aces	- 20 points
Nine, Ten, Jack, Queen, King - 10 points
Four, Five, Six, Seven, Eight - 5 points
Black Threes - 5 points
Red Threes - No value

Note that the value of a Three will differ based upon the color. Your program will prompt the user for the rank and, if the rank is a Three, it will need to also prompt the user for the color.
"""

def get_point_value(rank: str, color: str=None):
    """Returns the value associated with the given rank and color.
    Ranks are: 
      Joker, Two, Ace, Nine, Ten, Jack, Queen, King, Four
      Five, Six, Seven, Eight, Three
    Colors are:
      Red, Black
    You may assume that the function is case sensitive.
    Parameters:
      rank (str): rank of the card
      color (str): color of the card (red or black) default to None
    Return:
      point value of the card or -1 if input is invalid.
    """
    pass

def main():
    pass

if __name__ == '__main__':
    main()