from triangle import classify_triangle
def test_invalid_triangle():
    assert classify_triangle(1,2,3) == "Invalid"

def test_stained_glass_requirements():
    assert classify_triangle(4,5,6) == "Scalene"
    assert classify_triangle(1,2,3) == "Invalid"
    assert classify_triangle(3,4,5) == "Right Scalene"