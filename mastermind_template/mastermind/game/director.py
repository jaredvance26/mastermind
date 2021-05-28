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
        self.move = Move()
        self.console = Console()

    def start_game(self):
        self.prepare_game()
        while self.keep_playing:
            self.get_inputs()
            self.get_updates()
            self.get_outputs()

    def prepare_game(self):
        self.guess = '----'
        for n in range(2):
            name = self.console.read(f'Enter name for player {n+1}: ')
            player = Player(name)
            player.set_move(self.move)
            self.roster.add_player(player)

    def get_inputs(self):
        
        # self.numbers.board(self.roster.players[0], self.roster.players[1])
        player1 = self.roster.players[0]
        player2 = self.roster.players[1]
        self.numbers.board(player1, player2)

        

    def get_updates(self):
        pass

    def get_outputs(self):
        pass