from game.console import Console
from game.move import Move
from game.numbers import Numbers
from game.player import Player
from game.roster import Roster 

class Director:
    def __init__(self):

        self.numbers = Numbers()
        self.roster = Roster()
        self.keep_playing = True
        self.move = None

    def start_game(self):
        self.prepare_game()
        while self.keep_playing:
            self.get_inputs()
            self.get_updates()
            self.get_outputs()

    def prepare_game(self):
        for n in range(2):
            name = self.cosole.read(f'Enter name for player {n+1}: ')
            player = Player(name)
            self.roster.add_player(player)

    def get_inputs(self):
        pass

    def get_updates(self):
        pass

    def get_outputs(self):
        pass