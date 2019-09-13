import DistancePointBl
import math


def test_distance():
    p1 = 3
    p2 = 5
    expected = math.sqrt(p1 * p1 + p2 * p2)
    assert expected == DistancePointBl.distance(p1, p2)
