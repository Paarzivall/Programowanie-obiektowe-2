from ConvexQuadrilateral import ConvexQuadrilateral


class Parallelogram(ConvexQuadrilateral):

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def take_parameters(self):
        self.lenght_of_side_a = input("Podaj długość pierwszego boku:\t")
        self.lenght_of_side_b = input("Podaj długość drugiego boku:\t")
        self.lenght_of_side_c = self.lenght_of_side_a
        self.lenght_of_side_d = self.lenght_of_side_b
        self.angle1 = input("Podaj wielkość pierwszego kąta:\t")
        self.angle2 = 180 - self.angle1
        self.angle3 = self.angle1
        self.angle4 = self.angle2


