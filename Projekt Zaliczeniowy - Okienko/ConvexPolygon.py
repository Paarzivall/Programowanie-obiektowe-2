from abc import ABC, abstractmethod


class ConvexPolygon(ABC):

    @abstractmethod
    def __init__(self, fill_colour, outline_colour):
        self.fill_colour = fill_colour
        self.outline_colour = outline_colour

    def area(self):
        pass

    def perimeter(self):
        pass

    def draw(self):
        pass
