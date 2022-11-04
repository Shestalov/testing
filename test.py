"""pytest example"""

from main import Coordinates, line_length


def test_a1():
    a1 = Coordinates(1, 2)
    a2 = Coordinates(2, 2)
    assert line_length(a1, a2) == 5


def test_a2():
    a1 = Coordinates(1, 2)
    a2 = Coordinates(2, 2)
    assert line_length(a1, a2) == 1
