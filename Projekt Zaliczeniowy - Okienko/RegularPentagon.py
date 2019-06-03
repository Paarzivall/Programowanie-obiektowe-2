import math
from  ConvexPolygon import ConvexPolygon
import Descryptors as desc


class RegularPentagon(ConvexPolygon):
    fill_colour = desc.ColorValidator()
    outline_colour = desc.ColorValidator()
    lenght_of_side_a = desc.SideValidator()

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)
        self.take_parameters()
        self.set_skala()
        self.set_wektor()

    def take_parameters(self):
        self.lenght_of_side_a = input("Podaj długość boku pięciokąta foremnego:\t")

    def set_wektor(self):
        a = self.lenght_of_side_a
        if a <= 10:
            self.wektor = 10
        else:
            self.wektor = 5

    def set_skala(self):
        a = self.lenght_of_side_a
        if a <= 10:
            self.skala = 25
        else:
            self.skala = 10

    def get_skala(self):
        return self.skala

    def area(self):
        a = self.lenght_of_side_a
        return (math.pow(a, 2) / 4) * math.sqrt(25 + (10 * math.sqrt(5)))

    def perimeter(self):
        return 5 * self.lenght_of_side_a

    def draw(self):
        a = self.lenght_of_side_a
        A = (self.wektor, self.wektor/2)
        B = (self.wektor + a, self.wektor/2)
        hc = (2 * (a ** 2 * a ** 2 + a ** 2 * a ** 2 + a ** 2 * a ** 2) - (a ** 4 + a ** 4 + a ** 4)) ** 0.5 / (2. * a)
        dx = (a ** 2 - hc ** 2) ** 0.5
        if abs((a - dx) ** 2 + hc ** 2 - a ** 2) > 0.01: dx = -dx
        C = (self.wektor + dx + a, self.wektor/2 + hc)
        D = (self.wektor + dx, self.wektor + 2*a/3)
        E = ((self.wektor + a) / 2, (a * math.sqrt(3)) /2 + a)
        coords = [int((x + 1) * self.skala) for x in A + B + C + D + E]
        return coords