from Triangle import Triangle


class IsoscelesTriangle(Triangle):

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def take_parameters(self):
        self.lenght_of_side_a = self.get_length()
        self.lenght_of_side_b = self.get_length()
        self.lenght_of_side_c = self.lenght_of_side_b

