from game.console import Console
from game.move import Move
from game.numbers import Numbers
from game.player import Player
from game.roster import Roster 
import os
from colorama import Fore,Back,Style

class Director:
    def __init__(self):
        self.numbers = Numbers()
        self.roster = Roster()
        self._keep_playing = True
        self.move = None
        self.console = Console()

    def start_game(self):
        self.prepare_game()
        while self._keep_playing:
            self.get_inputs()
            self.get_outputs()

    def prepare_game(self):
        self.guess = '----'
        for n in range(2):
            name = self.console.read(f'Enter name for player {n+1}: ')
            player = Player(name)
            player.set_move(Move())
            self.roster.add_player(player)

    def get_inputs(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        current_player = self.roster.get_current()
        Board = self.numbers.board(self.roster.players[0], self.roster.players[1])
        self.console.write(Board)
        Guess = self.console.read(f"{Fore.MAGENTA}{current_player.get_name()}{Style.RESET_ALL} What is your Guess? ")
        Answer = self.numbers.get_hint(Guess)
        move = Move(Guess,Answer)
        current_player.set_move(move)

    def get_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        
        if self.numbers.winner():
            winner = self.roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self.roster.next_player()
