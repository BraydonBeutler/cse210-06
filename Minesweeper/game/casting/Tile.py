import constants
from game.casting.actor import Actor
from game.shared.color import Color

class Tile(Actor):
    """A covered space, either a bomb or a number.

    The responsibililty of the Tile is to keep track of its own identity.

    Attributes:
        _is_bomb (bool): Whether or not the tile is a bomb.
        _nearby_bombs (int): How many bombs are adjacent to it.
        revealed (bool): whether or not the tile has been revealed
    """

    def __init__(self):
        """creates a new tile."""
        super().__init__()
        self._is_bomb = False
        self._nearby_bombs = 0

    def set_bomb(self , is_bomb):
        """sets whether the actor is a bomb or not."""
        if is_bomb == 9:
            self._is_bomb = True

    def peek_at_bomb(self):
        if self._is_bomb:
            return "Bomb"
        else:
            return self._nearby_bombs

    def setup_tile(self , bomb_number):
        """sets up the tile with a chance to be a bomb."""

        self.set_text("#")

        if bomb_number == 9:
            self.set_bomb(bomb_number)

        else:
            self._nearby_bombs = bomb_number
