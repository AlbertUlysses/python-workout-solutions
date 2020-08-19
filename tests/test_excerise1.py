from excerises.chapter1 import Game
import pytest
import re

def test_valid_input():

    game1 = Game(100, re)
   
    guess_number = '5'

    assert game1.valid_input(guess_number)
    with pytest.raises(Exception) as exception_info:
        game1.valid_input('k')
    assert exception_info.match('Input needs to be a number')

