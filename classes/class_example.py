import math


class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, w, h):
        super().__init__([w, h, w, h])
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, a=10):
        super().__init__(a, a)


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


def default_arguments(a, b, c=10, d=20):
    print(a, b, c)


def dynamic_ars(a, b, c, d):
    print(a, b, c, d)

my_list = [10, 20, 30, 40]
dynamic_ars(*my_list)


default_arguments(20, 30)
default_arguments(20, 30, 40)
default_arguments(20, 30, d=40)
default_arguments(a=20, b=30, d=40)

values = input().split()
print(values)
