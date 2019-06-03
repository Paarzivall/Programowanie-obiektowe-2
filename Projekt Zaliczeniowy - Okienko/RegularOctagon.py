import math
from  ConvexPolygon import ConvexPolygon
import Descryptors as desc


class RegularOctagon(ConvexPolygon):
    fill_colour = desc.ColorValidator()
    outline_colour = desc.ColorValidator()
    lenght_of_side_a = desc.SideValidator()

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)
        self.take_parameters()
        print(f'Pole powierzchni:\t {round(self.area(), 2)}')
        print(f'Obwód:\t {round(self.perimeter(), 2)}')

    def take_parameters(self):
        self.lenght_of_side_a = input("Podaj długość boku ośmiokąta foremnego:\t")

    def area(self):
        a = self.lenght_of_side_a
        return 2 * (1 + math.sqrt(2)) * math.pow(a, 2)

    def perimeter(self):
        return 8 * self.lenght_of_side_a

    def draw(self):
        pass