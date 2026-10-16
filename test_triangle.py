from triangle import is_valid_triangle, classify_triangle
import math
import pytest

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    assert classify_triangle(3, 3, 2) == "Isosceles"
    assert classify_triangle(3, 2, 3) == "Isosceles"
    assert classify_triangle(2, 3, 3) == "Isosceles"

def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 12, 13) == "Right Scalene"
    assert classify_triangle(8, 15, 17) == "Right Scalene"

def test_invalid_triangle():
    assert classify_triangle(0, 0, 0) == "Invalid"
    assert classify_triangle(-1, -1, -1) == "Invalid"
    assert classify_triangle(1, 2, 5) == "Invalid"

def test_degenerate_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(2, 3, 5) == "Invalid"

def test_decimal_right_triangle():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"