from game.casting.Tile import Tile
import pytest

tile = Tile()

def test_peek_at_bomb():
    assert tile.peek_at_bomb() == 0

def test_set_bomb():
    tile.set_bomb(9)
    assert tile.peek_at_bomb() == "Bomb"

def test_setup_tile():
    tile.setup_tile(8)
    assert tile.get_text() == "#"
