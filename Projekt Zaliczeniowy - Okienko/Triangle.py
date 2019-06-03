from ConvexPolygon import ConvexPolygon
import Descryptors as desc
import math


class Triangle(ConvexPolygon):
    fill_colour = desc.ColorValidator()
    outline_colour = desc.ColorValidator()
    lenght_of_side_a = desc.SideValidator()
    lenght_of_side_b = desc.SideValidator()
    lenght_of_side_c = desc.SideValidator()

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)
        self.take_parameters()
        self.set_skala()

    def take_parameters(self):
        self.lenght_of_side_a = self.get_length()
        self.lenght_of_side_b = self.get_length()
        self.lenght_of_side_c = self.get_length()

    def get_length(self):
        return input("Podaj długość boku:\t")

    def set_skala(self):
        a = self.lenght_of_side_a
        b = self.lenght_of_side_b
        c = self.lenght_of_side_c
        if a <= 10 and b <= 10 and c <= 10:
            self.skala = 50
        else:
            self.skala = 20

    def get_skala(self):
        return self.skala

    def area(self):
        """
            obliczanie pola trójkąta wg wzoru Herona
        """
        a = self.lenght_of_side_a
        b = self.lenght_of_side_b
        c = self.lenght_of_side_c
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def perimeter(self):
        return self.lenght_of_side_a + self.lenght_of_side_b + self.lenght_of_side_c

    def draw(self):
        a = self.lenght_of_side_a
        b = self.lenght_of_side_b
        c = self.lenght_of_side_c

        A = (0, 0)
        B = (c, 0)
        hc = (2 * (a ** 2 * b ** 2 + b ** 2 * c ** 2 + c ** 2 * a ** 2) - (a ** 4 + b ** 4 + c ** 4)) ** 0.5 / (2. * c)
        dx = (b ** 2 - hc ** 2) ** 0.5
        if abs((c - dx) ** 2 + hc ** 2 - a ** 2) > 0.01: dx = -dx
        C = (dx, hc)

        coords = [int((x + 1) * self.skala) for x in A + B + C]
        return coords
