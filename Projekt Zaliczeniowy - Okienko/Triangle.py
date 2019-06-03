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
        # print(f'Pole powierzchni:\t {round(self.area(), 2)}')
        # print(f'Obwód:\t {round(self.perimeter(), 2)}')

    def take_parameters(self):
        self.lenght_of_side_a = self.get_length()
        self.lenght_of_side_b = self.get_length()
        self.lenght_of_side_c = self.get_length()

    def get_length(self):
        return input("Podaj długość boku:\t")

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
        pass



