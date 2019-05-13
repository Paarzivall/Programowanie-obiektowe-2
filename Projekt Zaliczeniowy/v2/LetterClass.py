import pygame
from ResizeClass import Resize
import random


class Letter(Resize):

    def __init__(self):
        self.max_letters = 10
        self.letters = {'A': '../images/letter_A.png', 'B': '../images/letter_B.png',
                        'C': '../images/letter_C.png', 'D': '../images/letter_D.png',
                        'E': '../images/letter_E.png', 'F': '../images/letter_F.png',
                        'G': '../images/letter_G.png', 'H': '../images/letter_H.png',
                        'J': '../images/letter_J.png', 'K': '../images/letter_K.png',
                        'N': '../images/letter_N.png', 'O': '../images/letter_O.png',
                        'P': '../images/letter_P.png', 'R': '../images/letter_R.png',
                        'S': '../images/letter_S.png', 'X': '../images/letter_X.png',
                        'Z': '../images/letter_Z.png'}
        self.letters_positions = {0: (268, 91), 1: (318, 91), 2: (368, 91), 3: (418, 91),
                                  4: (468, 91), 5: (518, 91), 6: (568, 91), 7: (618, 91),
                                  8: (668, 91), 9: (718, 91)}
        self.add_letters()
        self.picked_letters = []
        # self.pick_letter()
        self.printuj()
        self.board = pygame.display.get_surface()

    def add_letters(self):
        """
            wczytuje litery do słownika jako obiekty
            z biblioteki pygame
        """
        for i in self.letters:
            letter = pygame.image.load(self.letters[i])
            letter = self.resize(letter)
            self.letters.update({i: letter})

    def printuj(self):
        for i in self.picked_letters:
            print(f"{i}")

    def draw_letters(self):
        """
            Metoda pozwalająca na rysowanie wylosowanych liter
            na ekranie
        """
        pos = 0
        for i in self.picked_letters:
            self.board.blit(self.letters[i], self.letters_positions[pos])
            pos += 1

    def random_letter(self):
        """
            Metoda losująca liczbę z zakresu 0 do 16
        """
        self.picked_letters = random.sample(self.letters.keys(), 10)
