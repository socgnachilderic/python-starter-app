from assertpy import assert_that

from domain.hello import hello, world


def test_hello():
    assert_that(hello()).is_equal_to("Hello world!")


def test_world():
    assert_that(world()).is_equal_to("world")
