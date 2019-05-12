import FrameClass as frame
from LetterClass import Letter

class Actions(Letter):

    def __init__(self):
        super().__init__()
        self.frames = frame.Frame()
        # self.letters = letters.Letter()
        self.x = 0
        self.compared_letters = {0: (0, 1), 1: (1, 2), 2: (2, 3),
                                 3: (3, 4), 4: (4, 5), 5: (5, 6),
                                 6: (6, 7), 7: (7, 8), 8: (8, 9)}
        # self.picked_letters = letters.picked_letters()

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

    def draw_letter(self):
        self.draw_letter()

    def draw_frame(self, x, y):
        """
            metoda pozwalająca na narysowanie naszej ramki na ekranie
        """
        self.frames.draw_frame(x, y)

    def compare(self, compare_number):
        for i in self.picked_letters:
            if i == compare_number[0]:
                print(self.picked_letters[i])

