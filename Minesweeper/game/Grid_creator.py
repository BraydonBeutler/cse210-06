import random
import constants

class grid():
    """A board that contains bombs and numbers.
    The responsibility of the grid is to make and return a certain sized square grid for playing.
    Attributes:
        _gridsize (int) the number of collumns and rows to put in the grid
        _grid (list): The grid to play on
    """

    def __init__(self , constants):
        """Create a new grid"""
        self._gridsize = constants.GRID_SIZE
        self._grid = []
        self._setup_grid()

    def get_grid(self):
        """return the grid"""
        return self._grid

    def get_gridsize(self):
        """return the size of the Grid from the constants."""
        return self._gridsize

    def _update_right(self , grid , x , y):
        """update the right of the selected square."""
        if grid[x][y+1] != 9:
            grid[x][y+1] += 1

    def _update_left(self , grid , x , y):
        """update the left of the selected square."""
        if grid[x][y-1] != 9:
            grid[x][y-1] += 1

    def _update_above(self , grid , x , y):
        """update the above of the selected square."""
        if grid[x-1][y] != 9:
            grid[x-1][y] += 1

    def _update_below(self , grid , x , y):
        """update the below of the selected square."""
        if grid[x+1][y] != 9:
            grid[x+1][y] += 1

    def _update_tl(self , grid , x , y):
        """update the top left of the selected square."""
        if grid[x-1][y-1] != 9:
            grid[x-1][y-1] += 1

    def _update_tr(self , grid , x , y):
        """update the top right of the selected square."""
        if grid[x-1][y+1] != 9:
            grid[x-1][y+1] += 1

    def _update_bl(self , grid , x , y):
        """update the bottom left of the selected square."""
        if grid[x+1][y-1] != 9:
            grid[x+1][y-1] += 1

    def _update_br(self , grid , x , y):
        """update the bottom right of the selected square."""
        if grid[x+1][y+1] != 9:
            grid[x+1][y+1] += 1


    def _update_numbers(self):
        """Updates the list to tell nearby bombs"""

        # set nearby numbers to tell how many bombs are adjacent
        # test = [[9,9] , [9,9]]
        x = 0
        y = 0

        for column in self._grid:
            y = 0


            for tile in range(len(column)):

                # print(x,y)

                if self._grid[x][y] == 9:
                    # The top left corner
                    if (x == 0 and y == 0):
                        self._update_right(self._grid , x , y)
                        self._update_below(self._grid , x , y)
                        self._update_br(self._grid , x , y)

                    # The top right corner
                    elif (x == 0 and y == self._gridsize-1):
                        self._update_left(self._grid , x , y)
                        self._update_below(self._grid , x , y)
                        self._update_bl(self._grid , x , y)

                    # The lower left corner
                    elif (x == self._gridsize-1 and y == 0):
                        self._update_right(self._grid , x , y)
                        self._update_above(self._grid , x , y)
                        self._update_tr(self._grid , x , y)

                    # The lower right corner
                    elif (x == self._gridsize-1 and y == self._gridsize-1):
                        self._update_left(self._grid , x , y)
                        self._update_above(self._grid , x , y)
                        self._update_tl(self._grid , x , y)

                    # the left edge
                    elif x == 0:
                        self._update_right(self._grid , x , y)
                        self._update_above(self._grid , x , y)
                        self._update_below(self._grid , x , y)
                        self._update_br(self._grid , x , y)
                        self._update_tr(self._grid , x , y)

                    # the right edge
                    elif y == self._gridsize-1:
                        self._update_left(self._grid , x , y)
                        self._update_above(self._grid , x , y)
                        self._update_below(self._grid , x , y)
                        self._update_bl(self._grid , x , y)
                        self._update_tl(self._grid , x , y)

                    # the top edge
                    elif y == 0:
                        self._update_left(self._grid , x , y)
                        self._update_right(self._grid , x , y)
                        self._update_below(self._grid , x , y)
                        self._update_bl(self._grid , x , y)
                        self._update_br(self._grid , x , y)

                    # the bottom edge
                    elif x == self._gridsize-1:
                        self._update_left(self._grid , x , y)
                        self._update_right(self._grid , x , y)
                        self._update_above(self._grid , x , y)
                        self._update_tl(self._grid , x , y)
                        self._update_tr(self._grid , x , y)

                    # anywhere in the center
                    else:
                        self._update_above(self._grid , x , y)
                        self._update_below(self._grid , x , y)
                        self._update_left(self._grid , x , y)
                        self._update_right(self._grid , x , y)
                        self._update_tl(self._grid , x , y)
                        self._update_tr(self._grid , x , y)
                        self._update_bl(self._grid , x , y)
                        self._update_br(self._grid , x , y)
                # move to next y
                y += 1
            # move to next x and reset y
            x += 1
            y = 0

    def _setup_grid(self):
            """create a new grid with numbers and bombs
            Returns a list with 0s and 9s
            """

            # create a list for the columns and rows
            for column in range(self._gridsize):
                self._grid.append([])
                for space in range(self._gridsize):
                    chance = random.randint(1 , 100)
                    if chance < 20:
                        self._grid[column].append(9)
                    else:
                        self._grid[column].append(0)

            for column in self._grid:
                random.shuffle(column)

            self._update_numbers()


# grid = grid(constants)
# for list in grid.get_grid():
#     print(list)
