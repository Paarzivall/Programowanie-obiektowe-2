import math
from Rhombus import Rhombus


class Square(Rhombus):
    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def take_parameters(self):
        self.lenght_of_side_a = input("Podaj długość krawędzi podstawy:\t")
        self.lenght_of_side_b = self.lenght_of_side_a
        self.lenght_of_side_c = self.lenght_of_side_a
        self.lenght_of_side_d = self.lenght_of_side_a
        self.angle1 = 90
        self.angle2 = self.angle1
        self.angle3 = self.angle1
        self.angle4 = self.angle1


