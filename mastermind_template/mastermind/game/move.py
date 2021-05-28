class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the guesses
    
    Stereotype: 
        Information Holder

    Attributes:
        
    """
    def __init__(self, guess="----", answer="****"):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = guess
        self._answer = answer

    def get_guess(self):
        """Returns the guess of the user

        Args:
            self (Move): an instance of Move.
        """
        return self._guess

    def get_answer(self):
        """ Returns the answer"""
        
        return self._answer