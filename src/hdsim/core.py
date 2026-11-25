"""Heights and distances with exact arithmetic for 30, 45 and 60 degrees.

Numbers live in Q(sqrt 3): p + q*sqrt(3) with p, q exact Fractions, so
answers such as 5*sqrt(3) are exact, not 8.66.
"""
import math
from fractions import Fraction


class Q3:
    def __init__(self, p=0, q=0):
        self.p, self.q = Fraction(p), Fraction(q)

    def __add__(self, o):
        o = _q(o)
        return Q3(self.p + o.p, self.q + o.q)

    def __sub__(self, o):
        o = _q(o)
        return Q3(self.p - o.p, self.q - o.q)

    def __mul__(self, o):
        o = _q(o)
        return Q3(self.p * o.p + 3 * self.q * o.q, self.p * o.q + self.q * o.p)

    __radd__ = __add__
    __rmul__ = __mul__

    def inverse(self):
        n = self.p ** 2 - 3 * self.q ** 2
        if n == 0:
            raise ZeroDivisionError("zero has no inverse")
        return Q3(self.p / n, -self.q / n)

    def __truediv__(self, o):
        return self * _q(o).inverse()

    def __eq__(self, o):
        o = _q(o)
        return (self.p, self.q) == (o.p, o.q)

    def __float__(self):
        return float(self.p) + float(self.q) * math.sqrt(3)

    def __str__(self):
        if self.q == 0:
            return str(self.p)
        r = "sqrt(3)" if abs(self.q) == 1 else f"{abs(self.q)} sqrt(3)"
        if self.p == 0:
            return ("-" if self.q < 0 else "") + r
        return f"{self.p} {'-' if self.q < 0 else '+'} {r}"

    __repr__ = __str__


def _q(x):
    return x if isinstance(x, Q3) else Q3(x)


_COT = {30: Q3(0, 1), 45: Q3(1), 60: Q3(0, Fraction(1, 3))}


def cot(angle):
    if angle not in _COT:
        raise ValueError("exact angles are 30, 45 and 60 degrees")
    return _COT[angle]


def tan(angle):
    return cot(angle).inverse()


def height_one_point(d, angle):
    """Height of a tower seen at an angle of elevation from d metres away."""
    return _q(d) * tan(angle)


def distance_to_base(h, angle):
    return _q(h) * cot(angle)


def height_two_points(d, far_angle, near_angle):
    """Observer walks d towards the tower; elevation grows from far to near.
    h = d / (cot far - cot near)."""
    if not far_angle < near_angle:
        raise ValueError("the nearer angle must be larger")
    return _q(d) / (cot(far_angle) - cot(near_angle))


def height_two_points_float(d, far_deg, near_deg):
    f, n = math.radians(far_deg), math.radians(near_deg)
    return d / (1 / math.tan(f) - 1 / math.tan(n))


def svg(h, d, angle):
    """A simple SVG of the tower, the ground distance and the angle."""
    hf, df = float(h), float(d)
    s = 300 / max(hf, df)
    H, D = hf * s, df * s
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{D + 80:.0f}" height="{H + 60:.0f}">'
        f'<line x1="20" y1="{H + 30:.0f}" x2="{D + 20:.0f}" y2="{H + 30:.0f}" stroke="black"/>'
        f'<line x1="{D + 20:.0f}" y1="{H + 30:.0f}" x2="{D + 20:.0f}" y2="30" stroke="black"/>'
        f'<line x1="20" y1="{H + 30:.0f}" x2="{D + 20:.0f}" y2="30" stroke="black"/>'
        f'<text x="30" y="{H + 25:.0f}">{angle} deg</text></svg>'
    )
