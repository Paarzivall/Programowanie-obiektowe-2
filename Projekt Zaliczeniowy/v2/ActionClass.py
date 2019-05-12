import FrameClass as frame
import LetterClass as letters


class Actions(object):

    def __init__(self):
        self.frames = frame.Frame()
        self.x = 0

    def move_frame(self, action=None):
        if action == "L":
            print("Akcja L")
        elif action == "R":
            print("Akcja R")
            if self.x <= 8:
                self.frames.draw_frame(self.x)
                self.x += 1
            else:
                self.x = 0
                self.frames.draw_frame(self.x)
        elif action == "O":
            print("Akcja O")
