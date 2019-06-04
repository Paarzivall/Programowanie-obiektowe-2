import math
from ConvexQuadrilateral import ConvexQuadrilateral


class Kite(ConvexQuadrilateral):
    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def take_parameters(self):
        self.lenght_of_side_a = input("Podaj długość pierwszej krawędzi:\t")
        self.lenght_of_side_b = input("Podaj długość drugiej krawędzi:\t")
        self.lenght_of_side_c = self.lenght_of_side_a
        self.lenght_of_side_d = self.lenght_of_side_b
        self.angle1 = input("Podaj pierwszy kąt:\t")
        self.angle2 = input("Podaj drugi kąt (Jeden z dwóch tych samych):\t")
        self.angle3 = self.angle2
        self.angle4 = 360 - self.angle1 - 2 * self.angle2

    def area(self):
        a = self.lenght_of_side_a
        b = self.lenght_of_side_b

        return (math.pow(a, 2) * math.sin(math.radians(self.angle1))) / 2 + (math.pow(b, 2) *math.sin(math.radians(self.angle1))) / 2

    def draw(self):
        a = self.lenght_of_side_a
        b = self.lenght_of_side_b

        start_x = self.wektor
        start_y = self.wektor
        coords = []
        angle1 = self.angle1
        angle2 = self.angle2
        angle3 = self.angle4
        for i in range(4):
            if i == 1:
                end_x = start_x + a * math.cos(math.radians(angle1 * i))
                end_y = start_y + a * math.sin(math.radians(angle1 * i))
            elif i == 2:
                end_x = start_x + b * math.cos(math.radians(angle2 * i))
                end_y = start_y + b * math.sin(math.radians(angle2 * i))
            elif i == 3:
                end_x = start_x + b * math.cos(math.radians(angle3 * i))
                end_y = start_y + b * math.sin(math.radians(angle3 * i))
            else:
                end_x = start_x + a * math.cos(math.radians(angle2 * i))
                end_y = start_y + a * math.sin(math.radians(angle2 * i))
            coords.append([self.skala * start_x, self.skala * start_y])
            start_x = end_x
            start_y = end_y
        return coords

