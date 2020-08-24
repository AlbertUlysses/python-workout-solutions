import re
from random import randrange


class Game:

    def __init__(self, correct_number, re):
        self.correct_number = str(correct_number)
        self.valid_entries = '[0-9]+'
        self.re = re
    
    def random_game(self):
        guess_number = ''
        guess_number = self.guess_input(guess_number)
        while guess_number != self.correct_number:
            if guess_number < self.correct_number:
                print(f'The number {guess_number} is too low')
            elif guess_number > self.correct_number:
                print(f'The number {guess_number} is too High')
            guess_number = self.guess_input(guess_number)
        print(str('Just right!'))
       
    def valid_input(self, input_value):
        if self.re.search(self.valid_entries, input_value):
            return True
        raise Exception('Input needs to be a number')

    def guess_input(self, guess_number):
        response = input('Please enter a number:')
        if self.valid_input(response):
            guess_number = response
            return guess_number


if __name__ == '__main__':
    game1 = Game(randrange(0, 4), re)
    game1.random_game()
