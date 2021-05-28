from game.console import Console
from game.move import Move
from game.numbers import Numbers
from game.player import Player
from game.roster import Roster 
import os
from colorama import Fore,Back,Style

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        numbers (Numbers): An instance of the class of objects known as Numbers.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (player): An instance of the class of objects known as Move.
        roster (player): An instance of the class of objects known as Roster.

    """
    
    def __init__(self):
        """ The class constructor.
        
        Args:
            self (Director): an instance of Director.       
        """
        self.numbers = Numbers()
        self.roster = Roster()
        self._keep_playing = True
        self.move = None
        self.console = Console()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.prepare_game()
        while self._keep_playing:
            self.get_inputs()
            self.get_outputs()

    def prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        self.guess = '----'
        for n in range(2):
            name = self.console.read(f'Enter name for player {n+1}: ')
            player = Player(name)
            player.set_move(Move())
            self.roster.add_player(player)

    def get_inputs(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
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
