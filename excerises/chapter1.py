import re
from random import randrange


class Game:


    def __init__(self, lower_bound, upper_bound):
        self.random_value = randrange(lower_bound, upper_bound)
    
    def random_game():
        pass


    def valid_input(self, input_value):
        pattern = '[0-9]+'
        if re.search(pattern, input_value):
            return True
        raise Exception('Input needs to be a number')
