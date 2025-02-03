import math

def findRoots(a, b, c):
    if (a == 0 and b == 0 and c == 0):
        print("Infinite solutions")

    if (a == 0 and b == 0):
        print("No solution")
    if a != 0:
        D = b ** 2 - 4 * a * c
        if b == 0 and c == 0:
            print(0)
        elif b == 0:
            if c > 0:
                print(0)
            else:
                x1 = (-c / a) ** 0.5
                x2 = -((-c / a) ** 0.5)
                mas = [round(x1, 2), round(x2, 2)]
                print(*sorted(mas))
        elif D < 0:
            print("No solution")
        elif D == 0:
            x = -b / 2 * a
            print(round(x, 2))
        elif D > 0:
            x1 = (-1 * b + D ** 0.5) / (2 * a)
            x2 = (-1 * b - D ** 0.5) / (2 * a)
            mas = [round(x1, 2), round(x2, 2)]
            print(*sorted(mas))
            
    if a == 0 and b != 0:
        if c == 0:
            print(0)
        else:
            print(round(-c / b, 2))

print('Введите через enter значения a, b и с')

a = float(input())
b = float(input())
c = float(input())

findRoots(a, b, c)