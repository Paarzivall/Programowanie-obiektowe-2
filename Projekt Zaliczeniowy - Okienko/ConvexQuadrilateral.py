import math
from  ConvexPolygon import ConvexPolygon
import Descryptors as desc


class ConvexQuadrilateral(ConvexPolygon):
    fill_colour = desc.ColorValidator()
    outline_colour = desc.ColorValidator()
    lenght_of_side_a = desc.SideValidator()
    lenght_of_side_b = desc.SideValidator()
    lenght_of_side_c = desc.SideValidator()
    lenght_of_side_d = desc.SideValidator()
    angle1 = desc.AngleValidator()
    angle2 = desc.AngleValidator()
    angle3 = desc.AngleValidator()
    angle4 = desc.AngleValidator()

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)
        self.take_parameters()
        self.set_skala()
        self.set_wektor()

    def set_wektor(self):
        a = self.lenght_of_side_a
        b = self.lenght_of_side_b
        c = self.lenght_of_side_c
        d = self.lenght_of_side_d
        if a <= 10 and b <= 10 and c <= 10 and d <= 10:
            self.wektor = 8
        else:
            self.wektor = 10

    def set_skala(self):
        a = self.lenght_of_side_a
        b = self.lenght_of_side_b
        c = self.lenght_of_side_c
        d = self.lenght_of_side_d
        if a <= 5 and b <= 5 and c <= 5 and d <= 5:
            self.skala = 22
        else:
            self.skala = 10

    def get_skala(self):
        return self.skala

    def take_parameters(self):
        self.lenght_of_side_a = input("Podaj długość pierwzego boku:\t")
        self.lenght_of_side_b = input("Podaj długość drugiego boku:\t")
        self.lenght_of_side_c = input("Podaj długość trzeciego boku:\t")
        self.lenght_of_side_d = input("Podaj długość czwartego boku:\t")
        self.angle1 = input("Podaj pierwszy kąt:\t")
        self.angle2 = input("Podaj drugi kąt:\t")
        self.angle3 = input("Podaj trzeci kąt:\t")
        self.angle4 = 360 - (self.angle1 + self.angle2 + self.angle3)

    def area(self):
        h = self.lenght_of_side_b * math.sin(math.radians(self.angle1))
        return self.lenght_of_side_a * h

    def perimeter(self):
        return self.lenght_of_side_a + self.lenght_of_side_b + self.lenght_of_side_c + self.lenght_of_side_d

    def draw(self):
        bok = self.lenght_of_side_a
        bok1 = self.lenght_of_side_b
        bok2 = self.lenght_of_side_c
        bok3 = self.lenght_of_side_d
        a = bok * math.cos(math.radians(self.angle1))
        b = bok1 * math.sin(math.radians(self.angle2))
        c = bok2 * math.cos(math.radians(self.angle3))
        d = bok3 * math.sin(math.radians(self.angle4))

        coords = [
            (self.skala * self.wektor, self.skala * self.wektor),
            (self.skala * (self.wektor + bok), self.skala * self.wektor),
            (self.skala * (self.wektor + bok2 + a), self.skala * (self.wektor + d)),
            (self.skala * (self.wektor + c), self.skala * (self.wektor + d))
        ]

        return coords