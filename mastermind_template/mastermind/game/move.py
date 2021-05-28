class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
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
        """Returns the pile to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return self._guess

    def get_answer(self):
    
        
        return self._answer