from Triangle import Triangle


class EquilateralTriangle(Triangle):

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def take_parameters(self):
        self.lenght_of_side_a = self.get_length()
        self.lenght_of_side_b = self.lenght_of_side_a
        self.lenght_of_side_c = self.lenght_of_side_a