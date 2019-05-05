import FrameClass as frame
import LetterClass as letters


class Actions(object):

    def __init__(self):
        self.frames = frame.Frame()
        # self.letters = letters.Letter()

    def move_frame(self, action):
        if action == "L":
            print("Akcja L")
        elif action == "R":
            print("Akcja R")
            self.frames.move_frame()
        elif action == "O":
            print("Akcja O")

    # def draw_actions(self):
    #    self.letters.draw_letters()
    #    self.frames.draw_frame()
