import pytest
from shadowfleet.common.geo import haversine_m

ONE_DEGREE_M = 111195.0

def test_identical_point():
    distance = haversine_m(0, 0, 0, 0)
    assert distance == 0.0

def test_one_degree_latitude():
    distance = haversine_m(0, 0, 1, 0)
    assert pytest.approx(distance, rel=1e-3) == ONE_DEGREE_M

def test_one_degree_longitude_at_60_north():
    distance = haversine_m(60, 0, 60, 1)
    assert pytest.approx(distance, rel=1e-4) == ONE_DEGREE_M*0.5