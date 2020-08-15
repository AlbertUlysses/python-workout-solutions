from excerises.chapter1 import Game
import pytest

game1 = Game(0, 100, 5)
   
guess_number = 5
   
assert guess_number > game1.lower_bound
assert guess_number < game1.upper_bound

def test_valid_input():

    game1 = Game(0, 100, 5)
   
    guess_number = 5

    assert game1.valid_input('k') == False
    assert game1.valid_input('5') == True
