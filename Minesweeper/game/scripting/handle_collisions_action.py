import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the Rider collides with a trail,
    or the Rider collides with another rider, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            # self._handle_trail(cast , user)
            # self._handle_rider_collision(cast)
            # self._handle_trail_collision(cast)
            self._handle_game_over(cast)

    # def _handle_trail(self , cast , user):
    #     """As the rider moves, make a new trail space behind him.
    #
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     player = cast.get_first_actor(user)
    #     player.grow_tail()


    # def _handle_rider_collision(self, cast):
    #     """If the two riders collide, it is a draw and neither win.
    #
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     player_2 = cast.get_first_actor("player_2")
    #     player_1 = cast.get_first_actor("player_1")
    #     rider_1 = player_1.get_rider()
    #     rider_2 = player_2.get_rider()
    #
    #     if rider_1.get_position().equals(rider_2.get_position()):
    #         self._is_game_over = True
    #
    # def _handle_trail_collision(self, cast):
    #     """Sets the game over flag if a rider collides with a trail.
    #
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     player_1 = cast.get_first_actor("player_1")
    #     segments_1 = player_1.get_spaces()[1:]
    #     rider_1 = player_1.get_spaces()[0]
    #
    #     player_2 = cast.get_first_actor("player_2")
    #     segments_2 = player_2.get_spaces()[1:]
    #     rider_2 = player_2.get_spaces()[0]
    #
    #     for trail in [segments_1 , segments_2]:
    #         for space in trail:
    #             if rider_1.get_position().equals(space.get_position()):
    #                 self._is_game_over = True
    #                 self._winner = "player_2"
    #
    #             elif rider_2.get_position().equals(space.get_position()):
    #                 self._is_game_over = True
    #                 self._winner = "player_1"


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player_1 = cast.get_first_actor("player_1")
            spaces1 = player_1.get_spaces()

            player_2 = cast.get_first_actor("player_2")
            spaces2 = player_2.get_spaces()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for trail in [spaces1 , spaces2]:
                for segment in trail:
                    segment.set_color(constants.WHITE)

            score = cast.get_first_actor("score")
            score.add_points(self._winner)
