import math


class Figure(object):

    def __init__(self):
        self.colour = True
        self.is_filled = False

    def __str__(self):
        return f"Kolor: {self.colour}, Wypełniony: {self.is_filled}"

    def __repr__(self):
        return f"Kolor: {self.colour}, Wypełniony: {self.is_filled}"


class Circle(Figure):

    def __init__(self, radius):
        Figure.__init__(self)
        self.radius = radius
        self.area = (math.pi * math.pow(self.radius, 2))
        self.perimeter = (2 * math.pi * self.radius)
        self.diameter = (2 * self.radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if isinstance(value, float) and value > 0:
            self._radius = value
        else:
            self._radius = 1

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def perimeter(self):
        return self._perimeter

    @perimeter.setter
    def perimeter(self, value):
        self._perimeter = value

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value

    def __str__(self):
        return super(Circle, self).__str__() + f"\nPromień: {self._radius}, Pole: {self._area}, Obwód: {self._perimeter}, Średnica: {self._diameter}"

    def __repr__(self):
        return super(Circle, self).__repr__() + f"\nPromień: {self._radius}, Pole: {self._area}, Obwód: {self._perimeter}, Średnica: {self._diameter}"


class Rectangle(Figure):

    def __init__(self, width, height):
        Figure.__init__(self)
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)
        self.diagonal = math.sqrt(math.pow(self.height, 2) + math.pow(self.height, 2))

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, float) and value > 0:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, float) and value > 0:
            self._height = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def perimeter(self):
        return self._perimeter

    @perimeter.setter
    def perimeter(self, value):
        self._perimeter = value

    @property
    def diagonal(self):
        return self._diagonal

    @diagonal.setter
    def diagonal(self, value):
        self._diagonal = value

    def __str__(self):
        return super(Rectangle, self).__str__() + f"\nPole: {self._area}, Obwód: {self._perimeter}, Wysokość: {self._height}, Szerokość: {self._width}, Przekątna: {self._diagonal}"

    def __repr__(self):
        return super(Rectangle, self).__repr__() + f"\nPole: {self._area}, Obwód: {self._perimeter}, Wysokość: {self._height}, Szerokość: {self._width}, Przekątna: {self._diagonal}"


if __name__ == '__main__':
    circle = Circle(2.0)
    print(circle)

    rectangle = Rectangle(2.0, 2.0)
    print(repr(rectangle))

    # print(Figure.__dict__)
    # print(Circle.__dict__)
    # print(Rectangle.__dict__)
