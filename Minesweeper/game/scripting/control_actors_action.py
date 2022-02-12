import constants

from game.scripting.action import Action
from game.shared.point import Point


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

            if command == "Flag":
                if current_tile.get_text() == "#":
                    current_tile.flag()
                else:
                    current_tile.unflag()

            elif command == "Reveal":
                current_tile.uncover_tile()

