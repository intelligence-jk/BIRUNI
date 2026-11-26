# ICARUS: Inclination, Clinometer, Angles, Rise, Upward Sight

Formerly `heights-distances-sim`.

An exact solver for heights and distances problems with angles of elevation of 30, 45 and 60 degrees, plus a small SVG diagram.

## What it solves
Textbook answers are like 5 sqrt(3) metres, not 8.66. This tool keeps numbers in the form p + q sqrt(3) with exact fractions p and q, so answers match the textbook form and can be tested exactly. It handles one observation point and the classic two-point problem (the observer walks closer and the angle grows). Pure Python 3.10+, standard library only.

## Example
```bash
python -m hdsim two 10 30 60
```
```
height = 5 sqrt(3)
```
(Output pasted from a real run.)

## The maths behind it
From a point x metres from the foot of a tower of height h, tan(angle) = h/x, so x = h cot(angle). With two points d apart, x_far - x_near = d, so h (cot far - cot near) = d and h = d / (cot far - cot near). Here cot 30 = sqrt(3), cot 45 = 1, cot 60 = sqrt(3)/3, so for d = 10: h = 10 / (sqrt(3) - sqrt(3)/3) = 10 / (2 sqrt(3)/3) = 15/sqrt(3) = 5 sqrt(3). Division uses the inverse (p + q sqrt 3)^-1 = (p - q sqrt 3)/(p^2 - 3q^2).

## Install and run
```bash
python -m pip install -e .
python -m pytest
```

## Licence
MIT. Made by Math & Myth (mathandmyth.ae): one to one maths mentoring, online, across the UAE.
