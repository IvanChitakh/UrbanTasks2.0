import math


class Figure:
    sides_count = 0
    __sides = []
    __color = []

    def __init__(self, color):
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        if self.__is_valid_color(self.r, self.g, self.b):
            self.__color = [self.r, self.g, self.b]

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (r >= 0 and r <= 255) and (g >= 0 and g <= 255) and (b >= 0 and b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if len(args) == self.__sides:
            for i in args:
                if i < 1 and int(i) != i:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    __radius = 0

    def __init__(self, color, *sides):
        super().__init__(color)
        if len(sides) != self.sides_count:
            Figure._Figure__sides = [1] * self.sides_count
        else:
            Figure._Figure__sides = list(sides * self.sides_count)
            self.side = sides[0]
            self._Circle__radius = self.side / (2 * math.pi)

    def get_square(self):
        return math.pi * (self._Circle__radius ** 2)


class Triangle(Figure):
    sides_count = 3
    triangle_sides = []

    def __init__(self, color, *sides):
        super().__init__(color)
        if len(sides) != self.sides_count:
            Figure._Figure__sides = [1] * self.sides_count
            self.triangle_sides = [1] * self.sides_count
        else:
            Figure._Figure__sides = list(sides)
            self.triangle_sides = list(sides)
        print(Figure._Figure__sides)
        print(self.triangle_sides)

    def get_square(self):
        a = self.triangle_sides[0]
        b = self.triangle_sides[1]
        c = self.triangle_sides[2]
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color)
        if len(sides) != 1:
            Figure._Figure__sides = [1] * self.sides_count
            self.side = 1
        else:
            Figure._Figure__sides = list(sides * self.sides_count)
            self.side = sides[0]

    def get_volume(self):
        return self.side ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print('-----------------\nДля самопроверки')
triangle1 = Triangle((100, 100, 100), 4, 4, 4)
triangle2 = Triangle((-100, 100, 100), 1, 2, 3, 4, 5)

print(triangle1.get_color())
print(triangle2.get_color())

triangle1.set_color(11, 22, 33)
triangle2.set_color(1, 2, -3)

print(triangle1.get_color())
print(triangle2.get_color())

print(triangle1.get_square())
print(triangle2.get_square())

print(circle1.get_square())
