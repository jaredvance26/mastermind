import random
from colorama import Fore,Back,Style

class Numbers:
    """ Create and generate random code. Takes in a guess and compares.
    Stereotype: Information Holder """

    def __init__(self):
        self.code = random.randint(1000, 9999)
        self.output = '****'

    def get_hint(self, guess):
        """ Compares the guess to the answer then gives hints accordinglyl
        x = right number right index
        o = right number wrong index
        * = wrong number wrong index
        """
        guess = str(guess)
        self.code = str(self.code)
        self.output = []

        for index, number in enumerate(guess):
            if number == self.code[index]:
                self.output.append(f'{Fore.GREEN}x{Style.RESET_ALL}')
            elif number in self.code:
                self.output.append(f'{Fore.YELLOW}o{Style.RESET_ALL}')
            else:
                self.output.append(f'{Fore.RED}*{Style.RESET_ALL}')
        return (''.join(self.output))
            
    def winner(self):
        """Determines if the game is won by a player. """
        won = ['x'] * len(self.output)
        if won == self.output:
            return True
        else:
            return False

    def board(self, player1, player2):
        """creates the board"""
        text = ('\n---------')
        text += (f'\nPlayer {Fore.MAGENTA}{player1.get_name()}{Style.RESET_ALL}: {player1.get_move().get_guess()}, {player1.get_move().get_answer()} ')
        text += (f'\nPlayer {Fore.MAGENTA}{player2.get_name()}{Style.RESET_ALL}: {player2.get_move().get_guess()}, {player2.get_move().get_answer()}')
        text += ('\n--------')
        return text