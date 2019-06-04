import math
from  ConvexPolygon import ConvexPolygon
import Descryptors as desc


class RegularHexagon(ConvexPolygon):
    fill_colour = desc.ColorValidator()
    outline_colour = desc.ColorValidator()
    lenght_of_side_a = desc.SideValidator()

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)
        self.take_parameters()
        self.set_skala()
        self.set_wektor()

    def set_wektor(self):
        a = self.lenght_of_side_a
        if a <= 10:
            self.wektor = 8
        else:
            self.wektor = 5

    def set_skala(self):
        a = self.lenght_of_side_a
        if a <= 5:
            self.skala = 25
        else:
            self.skala = 10

    def get_skala(self):
        return self.skala

    def take_parameters(self):
        self.lenght_of_side_a = input("Podaj długość boku sześciokąta foremnego:\t")

    def area(self):
        a = self.lenght_of_side_a
        return (3 * math.pow(a, 2) * math.sqrt(3)) / 2

    def perimeter(self):
        return 6 * self.lenght_of_side_a

    def draw(self):
        a = self.lenght_of_side_a
        start_x = self.wektor
        start_y = self.wektor
        coords = []
        angle = 60
        for i in range(6):
            end_x = start_x + a * math.cos(math.radians(angle * i))
            end_y = start_y + a * math.sin(math.radians(angle * i))
            coords.append([self.skala * start_x, self.skala * start_y])
            start_x = end_x
            start_y = end_y
        return coords