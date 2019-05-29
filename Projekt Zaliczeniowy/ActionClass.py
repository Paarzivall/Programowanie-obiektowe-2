import FrameClass as frame
import LetterClass as letter
import GameController as control
from tkinter import *
from tkinter import messagebox


class Actions(object):

    def __init__(self):
        self.frames = frame.Frame()
        self.letters = letter.Letter()
        self.x = 0
        self.compared_letters = {0: (0, 1), 1: (1, 2), 2: (2, 3),
                                 3: (3, 4), 4: (4, 5), 5: (5, 6),
                                 6: (6, 7), 7: (7, 8), 8: (8, 9)}

    def move_frame(self, x, y, action=None):
        """
            metoda pozwalająca na poruszenie ramki na ekranie
        """
        if action == "R":
            # print("Akcja R")
            self.frames.draw_frame(x, y)

    def draw_frame(self, x, y):
        """
            metoda pozwalająca na narysowanie naszej ramki na ekranie
        """
        self.frames.draw_frame(x, y)

    def draw_letters(self):
        self.letters.draw_letters()

    def compare(self, compare_number):
        """Metoda służąca do sprawdzania czy zamiana miejscami liter na żądanie użytkownika jest potrzebne"""
        com = self.compared_letters[compare_number]
        index = 0
        for i in self.letters.picked_letters:
            if index == com[0]:
                tmp = i
            elif index == com[1]:
                tmp2 = i
            index += 1
        if tmp2 <= tmp:
            self.letters.picked_letters[com[0]] = tmp2
            self.letters.picked_letters[com[1]] = tmp
        else:
            Tk().wm_withdraw()  # to hide the main window
            messagebox.showinfo('NIEPOPRAWNY RUCH',
                                'Niepoprawny ruch.\nLitery które chcesz zamienić są już w dobrej kolejności')

    def when_end(self):
        """Metoda kontrolująca koniec gry"""
        if self.letters.picked_letters == self.letters.sorted_picked_letters:
            return True
        else:
            return False

    def recommended_move(self, compare_number):
        """Metoda sprawdzająca czy użytkownik powinien wykonać ruch"""
        com = self.compared_letters[compare_number]
        index = 0
        for i in self.letters.picked_letters:
            if index == com[0]:
                tmp = i
            elif index == com[1]:
                tmp2 = i
            index += 1
        if ord(tmp2) < ord(tmp):
            return True
        elif ord(tmp) == ord(tmp2):
            return False
        else:
            return False

    def end_game(self):
        """Metoda wywołująca ekran zakończenia gry"""
        cont = control.Controller()
        cont.run(2)
        sys.exit()
