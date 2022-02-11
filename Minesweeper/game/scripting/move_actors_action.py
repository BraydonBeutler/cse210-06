import constants
from game.scripting.action import Action


class MoveActorsAction:

    def __init__(self):
        """Constructs a new MoveActorsAction."""
        super().__init__()

    def execute(self , cast , script):
        """Overrides the execute function from the superclass.
        args:
            cast (Cast): The cast of actors to move.
            script (Script): The script of Actions in the game.
        """
        _all_actors = cast.get_all_actors()

        for actor in _all_actors:
            actor.move_next(constants.MAX_X , constants.MAX_Y)
