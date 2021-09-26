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


if __name__ == '__main__':
    print('\n')
    print (classify_triangle(-1, 5, 4))
    print (classify_triangle(10,10,10))
    print (classify_triangle(5,4,3))
    print (classify_triangle(4,4,3))
    print('\n')
    
