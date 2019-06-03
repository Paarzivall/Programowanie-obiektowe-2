import math
from  ConvexPolygon import ConvexPolygon
import Descryptors as desc


class ConvexQuadrilateral(ConvexPolygon):
    fill_colour = desc.ColorValidator()
    outline_colour = desc.ColorValidator()
    lenght_of_diagonal_ac = desc.SideValidator()
    lenght_of_diagonal_bd = desc.SideValidator()
    angle = desc.AngleValidator()

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)
        self.take_parameters()

    def take_parameters(self):
        self.lenght_of_diagonal_ac = input("Podaj długość przekątnej AC:\t")
        self.lenght_of_diagonal_bd = input("Podaj długość przekątnej BD:\t")
        self.angle = input("Podaj mniejszy kąt między tymi przekątnymi:\t")

    def area(self):
        e = self.lenght_of_diagonal_ac
        f = self.lenght_of_diagonal_bd
        return (e * f * math.sin(self.angle)) / 2

    def perimeter(self):
        pass

    def draw(self):
        pass
