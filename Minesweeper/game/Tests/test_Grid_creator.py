from game.Grid_creator import grid
import pytest
import constants

Grid = grid(constants)

def test_get_grid():
    assert type(Grid.get_grid()) == list

def test_get_gridsize():
    assert Grid.get_gridsize() == constants.GRID_SIZE
