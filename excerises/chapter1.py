import re
from random import randrange

class Game:


    def __init__(self, correct_number, re):
        self.correct_number = str(correct_number)
        self.valid_entries = '[0-9]+'
        self.re = re
    
    def random_game(self):
        guess_number = ''
        while guess_number != self.correct_number:
            response = input('Please Enter a Number:')
            if self.valid_input(response):
                guess_number = response
        print(str('Good Job!'))
       

    def valid_input(self, input_value):
        if self.re.search(self.valid_entries, input_value):
            return True
        raise Exception('Input needs to be a number')

if __name__ == '__main__':
    game1 = Game(randrange(0, 4), re)
    game1.random_game()
