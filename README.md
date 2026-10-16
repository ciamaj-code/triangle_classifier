Triangle Classifier

Project Description - This project is a Python program that determines whether three side lengths form a valid triangle and classifies the triangle as Equilateral, Isosceles, or Scalene. It also identifies right triangles using the Pythagorean theory.

How to Run - 
Install the required package: python -m pip install -r requirements.txt

Run all the tests: python -m pytest -v

Equivalence Classes and Boundaries - 
The program tests follow these rules of equivalence
Equilateral: All 3 sides are equal
Isosceles: 2 of 3 sides are equal
Scalene: All 3 sides are different
Right Triangle: Sides lengths satisfy the Pythagorean theorem
Invalid Triangle: Side lengths are zero, negative, or violate the triangle inequality.

Boundary cases include zero-length sides, negative sides, and degenerate triangles where two sides add up to exactly the third.

The program also tests a right triangle with decimal side lengths to verify floating-point tolerance

Reminder: Equilateral triangles cannot be right triangles because a right triangle requires at least 1 90-degree angle, so it just doesnt work.

Acceptance Criteria:
1: Given three positive side lengths that form a valid triangle, the program returns the correct classification

2: Given invalid side lengths, the program returns "invalid" without raising an exception.

3: Given side lengths forming a right triangle, the classification begins with "Right" to identify pieces requiring reinforced corners.

| Test                        | Copilot-suggested?    | Decision | Why                                               |
|-----------------------------|-----------------------|----------|---------------------------------------------------|
| test_equilateral_triangle   | Yes                   | Kept     | Checked that three equal sides return Equilateral |
| test_scalene_triangle       | Yes                   | Edited   | Changed (3, 4, 5) because it is Right Scalene     |
| test_invalid_triangle       | Yes                   | Edited   | Corrected the expected output to Invalid          |
| test_decimal_right_triangle | Yes                   | Kept     | Verified that decimal side lengths work with math.isclose        |

AI-Use Disclosure:
I used GitHub Copilot with assistance of information provided to me by my groupmates for reference in part 1 and generating unit tests in part 2. I reviewed the suggestions, corrected mistakes, and ran the tests using pytest to verify the results.

I did not use GitHub Copilot for part 3. I still had reference material and I did use ChatGPT to better understand the assignment & git interactions, troubleshoot my code when I got it wrong, and review my work part 3 however, I mostly relied on google.