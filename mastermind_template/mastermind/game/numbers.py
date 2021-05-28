import random
class Numbers:
    """ Create and generate random code. Takes in a guess and compares. """

    def __init__(self):
        self.code = random.randint(1000, 9999)
        self.output = '****'

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
        return (''.join(self.output))
            
    def winner(self):
        won = ['x'] * len(self.output)
        return self.code == won

    def board(self, player1, player2):
        text = ('\n---------')
        text += (f'\nPlayer {player1.get_name()}: {player1.get_move.get_guess()}, {player1.get_move.get_answer()} ')
        text += (f'\nPlayer {player2.get_name()}: {player2.get_move.get_guess()}, {player2.get_move.get_answer()}')
        text += ('\n--------')

        return text