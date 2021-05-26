import random
class Numbers:
    """ Create and generate random code. Takes in a guess and compares. """

    def __init__(self):
        self.code = random.randint(1000, 9999)
        # print(self.code)

    def get_hint(self, guess):
        guess = str(guess)
        self.code = str(self.code)
        self.output = []

        for index, number in enumerate(guess):
            if number == self.code[index]:
                self.output.append('x')
            elif number in self.code:
                self.output.append('o')
            else:
                self.output.append('*')
            
    def winner(self):
        won = ['x'] * len(self.output)
        return self.code == won

    def display(self, player, guess):
        print('-----------------')
        output = (''.join(self.output))

number = Numbers()
guess = '1234'

number.compare(guess)