from game.casting.cast import Cast
cast = Cast()

def test_get_all_actors():
    assert cast.get_all_actors() == []

def test_get_first_actor():
    cast.add_actor("test" , "test first")
    assert "test first" in cast.get_first_actor("test")

def test_add_actor():
    cast.add_actor("test" , "test add")
    assert "test add" in cast.get_all_actors()

def test_get_actors():
    cast.add_actor("test" , "test get")
    assert "test get" in cast.get_actors("test")

def test_remove_actor():
    cast.add_actor("test" , "first add")
    cast.add_actor("test" , "second add")
    cast.remove_actor("test" , "first add")
    assert "second add" in cast.get_actors("test")
