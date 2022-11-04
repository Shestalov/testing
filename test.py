"""pytest example"""

from main import Coordinates, line_length


def test_a1():
    a1 = Coordinates(3, 3)
    a2 = Coordinates(1, 1)
    assert line_length(a1, a2) == 2.8284271247461903


def test_a2():
    a1 = Coordinates(3, 3)
    a2 = Coordinates(3, 5)
    assert line_length(a1, a2) == 2.0
