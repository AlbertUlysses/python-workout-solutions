import re
class Game:


    def __init__(self, lower_bound, upper_bound, random_value):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.random_value = random_value

    def valid_input(self, input_value):
        pattern = '[0-9]+'
        if re.search(pattern, input_value):
            return True
        else:
            return False
