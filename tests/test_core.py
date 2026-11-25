import math
from fractions import Fraction
import pytest
from hdsim import Q3, cot, tan, height_one_point, height_two_points, height_two_points_float, distance_to_base, svg


def test_tan_cot_are_inverse():
    for a in (30, 45, 60):
        assert tan(a) * cot(a) == 1


def test_tan_values_match_floats():
    for a in (30, 45, 60):
        assert float(tan(a)) == pytest.approx(math.tan(math.radians(a)))


def test_one_point_45():
    assert height_one_point(20, 45) == 20


def test_one_point_60():
    assert height_one_point(10, 60) == Q3(0, 10)


def test_two_points_exact():
    # far 30, near 60, d = 10: h = 5 sqrt 3
    assert height_two_points(10, 30, 60) == Q3(0, 5)


def test_two_points_consistency_by_distances():
    h = height_two_points(10, 30, 60)
    x_near = distance_to_base(h, 60)
    x_far = distance_to_base(h, 30)
    assert x_far - x_near == 10


def test_two_points_matches_float():
    assert float(height_two_points(7, 45, 60)) == pytest.approx(height_two_points_float(7, 45, 60))


def test_inverse_of_zero_fails():
    with pytest.raises(ZeroDivisionError):
        Q3(0, 0).inverse()


def test_bad_angle_and_order():
    with pytest.raises(ValueError):
        cot(50)
    with pytest.raises(ValueError):
        height_two_points(5, 60, 30)


def test_str_and_fraction_input():
    assert str(Q3(Fraction(1, 2), -1)) == "1/2 - sqrt(3)"
    assert str(height_one_point(Fraction(3, 2), 45)) == "3/2"


def test_svg_has_angle():
    assert "30 deg" in svg(5, 10, 30)
