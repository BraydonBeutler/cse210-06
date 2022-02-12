import constants

from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # move the cursor
        cursor = cast.get_first_actor("cursor")
        velocity = self._keyboard_service.get_direction()
        cursor.set_velocity(velocity)

    # use a command
        command = self._keyboard_service.get_command()
        position = cursor.get_position()
        tile_list = cast.get_actors("tiles")

        if command != "":
            current_tile = ""

            for tile in tile_list:
                if (abs(tile.get_position().get_x() - position.get_x()) < 15 and abs(tile.get_position().get_y() - position.get_y()) < 15) :
                    current_tile = tile

            try: # If the tile isnt an actor
                if command == "Flag":
                    if current_tile.get_text() == "#":
                        self.flag_tile(current_tile)

                    elif current_tile.get_text() == "F":
                        self.flag_tile(current_tile)

                elif command == "Reveal":
                    self.reveal_tile(current_tile)

            except:
                pass

    def reveal_tile(self , tile):
        """Uncovers the tile.
        Returns if the player died.
        """
        # return the number of the tile. 0-8  is safe, 9 is bomb
        status = tile.peek_at_bomb()
        try:
            int(status)
            tile.set_text(str(status))
            tile.set_color(constants.BLUE)
        except:
            tile.set_text("X")
            tile.set_color(constants.RED)

    def flag_tile(self , tile):
        """switches between flagged and unflagged for a covered tile."""
        if tile.get_text() == "F":
            tile.set_text("#")
            tile.set_color(constants.GREEN)

        elif tile.get_text() == "#":
            tile.set_text("F")
            tile.set_color(constants.YELLOW)
