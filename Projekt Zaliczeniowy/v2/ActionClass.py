import FrameClass as frame


class Actions(object):

    def __init__(self):
        self.frames = frame.Frame()

    def move_frame(self, action):
        if action == "L":
            print("Akcja L")
        elif action == "R":
            print("Akcja R")
            self.frames.move_frame()
        elif action == "O":
            print("Akcja O")

    def draw_actions(self):
        self.frames.draw_frame()