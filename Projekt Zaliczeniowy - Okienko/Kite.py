import math
from ConvexQuadrilateral import ConvexQuadrilateral


class Kite(ConvexQuadrilateral):
    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def take_parameters(self):
        self.lenght_of_side_a = input("Podaj długość pierwszej krawędzi:\t")
        self.lenght_of_side_b = input("Podaj długość drugiej krawędzi:\t")
        self.lenght_of_side_c = self.lenght_of_side_b
        self.lenght_of_side_d = self.lenght_of_side_a
        self.angle1 = input("Podaj pierwszy kąt:\t")
        self.angle2 = input("Podaj drugi kąt (Jeden z dwóch tych samych):\t")
        self.angle3 = self.angle2
        self.angle4 = 360 - self.angle1 - 2 * self.angle2

    def area(self):
        a = self.lenght_of_side_a
        b = self.lenght_of_side_b

        return ((math.pow(a, 2) * math.sin(math.radians(self.angle1))) / 2) + ((math.pow(b, 2) * math.sin(math.radians(360-(self.angle1 + 2 * self.angle2)))) / 2)

    def draw(self):
        p1 = 2 * self.lenght_of_side_a * math.cos(math.radians((180 - self.angle1) / 2))
        p2 = self.lenght_of_side_a * math.cos(math.radians(self.angle1 / 2)) + self.lenght_of_side_b * math.cos(math.radians((180 - self.angle1) / 2))

        h = math.sqrt(math.pow(self.lenght_of_side_a, 2) - (math.pow(p1, 2)) / 4)

        A = (self.wektor, self.wektor)
        B = (p2 + self.wektor, self.wektor)

        S = (p2 + self.wektor - h, self.wektor)

        C = (S[0], self.wektor - p1 / 2)
        D = (S[0], self.wektor + p1 / 2)

        coords = [int((x + 1) * self.skala) for x in A + C + B + D]
        return coords
