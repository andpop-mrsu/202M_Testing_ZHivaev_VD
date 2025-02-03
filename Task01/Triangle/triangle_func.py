import doctest

class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    """
    Возвращает тип треугольника по длинам его сторон.

    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 3, 4)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(0, 3, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Стороны должны быть положительными
    >>> get_triangle_type(1, 1, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Невозможно построить треугольник с такими сторонами
    """

    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Невозможно построить треугольник с такими сторонами")
    
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"
    
doctest.testmod()

print('Введите через enter a, b и с')

a = int(input())
b = int(input())
c = int(input())

triangleType = get_triangle_type(a, b, c)
print(triangleType)
