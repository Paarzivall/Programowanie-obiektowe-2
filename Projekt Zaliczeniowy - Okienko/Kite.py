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

