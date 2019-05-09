import FrameClass as frame


class Actions(object):

    def __init__(self):
        self.frames = frame.Frame()

    def move_frame(self, x, y, action=None):
        """
            metoda pozwalająca na poruszenie ramki na ekranie
        """
        if action == "L":
            print("Akcja L")
            self.frames.draw_frame(x, y)
        elif action == "R":
            print("Akcja R")
            self.frames.draw_frame(x, y)
        elif action == "O":
            print("Akcja O")

    def draw_frame(self, x, y):
        """
            metoda pozwalająca na narysowanie naszej ramki na ekranie
        """
        self.frames.draw_frame(x, y)
