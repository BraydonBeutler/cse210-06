from game.casting.actor import Actor
import pytest

actor = Actor()

def test_get_font_size():
    assert actor.get_font_size() == 15


def test_get_text():
    assert actor.get_text() == ""


def test_set_font_size():
    actor.set_font_size(5)
    assert actor.get_font_size() == 5


def test_set_text():
    actor.set_text("Penguin easter egg.") # Message darehsav@gmail.com if you see this :P
    assert actor.get_text() == "Penguin easter egg."

