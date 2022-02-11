import constants
import random

from game.directing.director import Director
from game.casting.cast import Cast
from game.casting.Tile import Tile
from  game.casting.actor import Actor

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

def main():
    """starts the game."""

    # create the cast
    cast = Cast()

    # create the cursor
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    position = position.scale(constants.CELL_SIZE)

    cursor = Actor()
    cursor.set_text("|_|")
    cursor.set_font_size(constants.FONT_SIZE)
    cursor.set_color(constants.WHITE)
    cursor.set_position(position)
    cast.add_actor("cursor", cursor)

    # create the tiles
    grid = [[0 , 1 , 1 , 2 , 1 , 1] ,
            [1 , 2 , 9 , 2 , 9 , 1] ,
            [9 , 3 , 2 , 1 , 1 , 1] ,
            [2 , 9 , 1 , 1 , 1 , 1] ,
            [1 , 2 , 2 , 2 , 9 , 2] ,
            [0 , 1 , 9 , 2 , 2 , 9]]

    x = 0
    y = 0
    color = constants.GREEN

    for row in grid:
        x += 15
        for space in row:
            y += 15
            tile = Tile()
            tile.setup_tile(space)
            tile.set_color(color)
            position = Point(x , y)
            position.scale(constants.CELL_SIZE)
            cast.add_actor("tiles", tile)

    # tstl = cast.get_all_actors()
    # for item in range(len((tstl))):
    #     print(tstl[item].peek_at_bomb())



    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()
