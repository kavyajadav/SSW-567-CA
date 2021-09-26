def classify_triangle(a, b, c):
    """
    Method that Classifies the triangle based on the sides given
    """
    intersection = {a, b, c} & {a, b, c}
    is_right_triangle = a ** 2 + b ** 2 == c ** 2
    triangle_class = 'Invalid Triangle'

    if a <= 0 or b <= 0 or c <= 0:
        return triangle_class

    if is_right_triangle:
        triangle_classification = 'Right Angle Triangle'
    elif len(intersection) == 1:
        triangle_classification = 'Equilateral  Triangle'
    elif len(intersection) == 2:
        triangle_classification = 'Isosceles Triangle'
    else:
        triangle_classification = 'Scalene Triangle'

    return triangle_classification



if __name__ == '__main__':
    print('\n')
    print (classify_triangle(-1, 5, 4))
    print (classify_triangle(10,10,10))
    print (classify_triangle(5,4,3))
    print (classify_triangle(4,4,3))
    print('\n')
    