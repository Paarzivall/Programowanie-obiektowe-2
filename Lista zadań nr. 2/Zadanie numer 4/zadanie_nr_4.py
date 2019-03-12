class Rectangle(object):

    def __init__(self):
        self.lenght = float(input("Podaj pierwszy wymiar:\t"))
        self.height = float(input("Podaj drugi wymiar:\t"))

    @property
    def lenght(self):
        return self._lenght

    @lenght.setter
    def lenght(self, value):
        if isinstance(value, float) and value < 0:
            self._lenght = 0
        else:
            self._lenght = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, float) and value < 0:
            self._height = 0
        else:
            self._height = value

    def area(self):
        return self._lenght * self._height

    def return_lenght(self):
        return self._lenght

    def return_height(self):
        return self._height

    def __str__(self):
        return f"Pole prostokąta o wymiarach: {self.lenght} x {self.height} wynosi: {self.area()}"

    def __repr__(self):
        return f"Pole prostokąta o wymiarach: {self.lenght} x {self.height} wynosi: {self.area()}"


class Cuboid(Rectangle):

    def __init__(self):
        Rectangle.__init__(self)
        self.width = float(input("Podaj wysokość bryły:\t"))

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, float) and value < 0:
            self._width = 0
        else:
            self._width = value

    def area(self):
        area = 2 * super(Cuboid, self).area()
        area += 2 * super(Cuboid, self).return_height()
        area += 2 * super(Cuboid, self).return_lenght()
        return area

    def volume(self):
        volume = super(Cuboid, self).area() * self.width
        return volume

    def __str__(self):
        all_info = f"Pierwsza krawędź podstawy: {super(Cuboid, self).return_lenght()}, Druga krawędź podstawy: {super(Cuboid, self).return_height()} "
        all_info += f"Wysokość bryły: {self.width}, \nPole powierzchni tej bryły: {self.area()}, Objętość tej bryły: {self.volume()}"
        return all_info

    def __repr__(self):
        all_info = f"Pierwsza krawędź podstawy: {super(Cuboid, self).return_lenght()}, Druga krawędź podstawy: {super(Cuboid, self).return_height()} "
        all_info += f"Wysokość bryły: {self.width}, \nPole powierzchni tej bryły: {self.area()}, Objętość tej bryły: {self.volume()}"
        return all_info


def menu():
    bryla = Cuboid()
    print(bryla)


if __name__ == '__main__': menu()