import sys
from fractions import Fraction
from .core import height_one_point, height_two_points


def main(argv=None):
    a = sys.argv[1:] if argv is None else argv
    try:
        if a[0] == "one" and len(a) == 3:
            print("height =", height_one_point(Fraction(a[1]), int(a[2])))
            return 0
        if a[0] == "two" and len(a) == 4:
            print("height =", height_two_points(Fraction(a[1]), int(a[2]), int(a[3])))
            return 0
    except (IndexError, ValueError) as e:
        print("error:", e)
        return 2
    print("usage: python -m hdsim one D ANGLE | two D FAR_ANGLE NEAR_ANGLE")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
