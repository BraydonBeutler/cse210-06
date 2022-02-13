import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color

class HandleGameStateAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCommandsAction is to check and update when the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCommandsAction."""
        self._is_game_over = False
        self._won = False

    def execute(self, cast, script):
        """Executes the handle Commands action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._check_tiles(cast)
            self._handle_game_over(cast)

        elif self._is_game_over and self._won:
            self._flash(cast)

    def _check_tiles(self , cast):
        """Go through all the tiles.
        If only all the bombs are flagged, you win.
        If any bomb has been revealed, you lose.
        """
        # Define the list of tiles
        tile_list = cast.get_actors("tiles")

        # Define the 3 parameters for ending
        uncovered_bomb = False
        flagged_tile = False
        any_bomb_covered = False

        for tile in tile_list:
            # If a bomb has been revealed
            if tile.get_text() == "X":
                uncovered_bomb = True

            # If a bomb isn't revealed
            tile_type = tile.peek_at_bomb()
            # If the tile is not a bomb
            try:
                int(tile_type)
                if tile.get_text() == "F":  # If any number is flagged
                    flagged_tile = True

            # If the bomb is covered
            except:
                if tile.get_text() == "#":
                    any_bomb_covered = True

            # If you revealed a bomb, you lose. End the check now.
            if uncovered_bomb == True:
                self._is_game_over = True
                return

        # If you won (Bombs all flagged, tiles all unflagged)
        if (flagged_tile == False and any_bomb_covered == False):
            self._is_game_over = True
            self._won = True



    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns all tiles to white and bombs to red.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            all_actors = cast.get_all_actors()

            x = 0
            y = 0
            position = Point(x, y)

            message = Actor()

            message.set_text("Game Over!")
            if self._won:
                message.set_text("You won!")

            message.set_position(position)
            cast.add_actor("messages", message)

            for actor in all_actors:
                if actor.get_text() != "X":
                    if self._won:
                        actor.set_color(constants.YELLOW)

                    else:
                        actor.set_color(constants.WHITE)

    def _flash(self , cast):
        """Flash the screen"""
        actors = cast.get_all_actors()
        for actor in actors:
            color = actor.get_color()
            r = color.to_tuple()[0]
            g = color.to_tuple()[1]
            b = color.to_tuple()[2]

            if r <= 25:
                r = 255
            else:
                r -= 25
            if g <= 50:
                g = 255
            else:
                g -= 50
            if b <= 10:
                b = 255
            else:
                b -= 10

            actor.set_color(Color(r , g , b))
