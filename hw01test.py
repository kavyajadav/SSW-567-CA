import unittest


def classify_triangle(a, b, c):
    """
    Method that Classifies the triangle based on the sides given
    """
    triangle_class = 'Not a Triangle'

    if a <= 0 or b <= 0 or c <= 0:
        return triangle_class

    if (a*a) + (b*b) == (c*c) or (b*b) + (c*c) == (a*a) or (c*c) + (a*a) == (b*b):
        triangle_classification = 'Right Angle Triangle'
    elif (a == b) and (b == c):
        triangle_classification = 'Equilateral Triangle'
    elif (a==b) or(b==c) or (c==a):
        triangle_classification = 'Isosceles Triangle'
    elif (a!=b and b!=c and c!=a):
        triangle_classification = 'Scalene Triangle'

    return triangle_classification


class TriangleClassification(unittest.TestCase):
    """
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    """

    def test_classify_equilateral_triangles(self):
        """
        Testcases for equilateral triangle
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral Triangle')
        self.assertEqual(classify_triangle(10, 10, 10), 'Equilateral Triangle')

    def test_classify_isosceles_triangles(self):
        """
        Testcases classify isosceles triangle
        """
        self.assertEqual(classify_triangle(65, 65, 130), 'Isosceles Triangle')
        self.assertEqual(classify_triangle(2, 3, 3), 'Isosceles Triangle')
        self.assertEqual(classify_triangle(4, 6, 4), 'Isosceles Triangle')

    def test_classify_scalene_triangles(self):
        """
        Testcases scalene triangle
        """
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene Triangle')
        self.assertEqual(classify_triangle(7, 6, 3), 'Scalene Triangle')
        self.assertEqual(classify_triangle(67, 87, 90), 'Scalene Triangle')

    def test_classify_right_triangles(self):
        """
        Testcases classify right triangle
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Angle Triangle')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right Angle Triangle')
        self.assertEqual(classify_triangle(8, 15, 17), 'Right Angle Triangle')

    def test_classify_not_a_triangle(self):
        """
        Testcases classify
        """
        self.assertEqual(classify_triangle(-10, -10, -10), 'Not a Triangle')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
