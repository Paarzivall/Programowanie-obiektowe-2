import pygame
from ResizeClass import Resize
import random


class Letter(Resize):

    def __init__(self):
        self.max_letters = 10
        self.letters = {0: '../images/letter_A.png', 1: '../images/letter_B.png',
                        2: '../images/letter_C.png', 3: '../images/letter_D.png',
                        4: '../images/letter_E.png', 5: '../images/letter_F.png',
                        6: '../images/letter_G.png', 7: '../images/letter_H.png',
                        8: '../images/letter_J.png', 9: '../images/letter_K.png',
                        10: '../images/letter_N.png', 11: '../images/letter_O.png',
                        12: '../images/letter_P.png', 13: '../images/letter_R.png',
                        14: '../images/letter_S.png', 15: '../images/letter_X.png',
                        16: '../images/letter_Z.png'}
        self.letters_positions = {0: (268, 91), 1: (318, 91), 2: (368, 91), 3: (418, 91),
                                  4: (468, 91), 5: (518, 91), 6: (568, 91), 7: (618, 91),
                                  8: (668, 91), 9: (718, 91)}
        self.add_letters()
        self.picked_letters = {}
        self.pick_letter()
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

    def pick_letter(self):
        """
            Losuje z wczytanych obiektów 10 liter,
            które będzie widział użytkownik
        """
        for i in range(0, 10):
            x = self.random_letter()
            self.picked_letters[i] = self.letters[x]
            print(x)

    def draw_letters(self):
        """
            Metoda pozwalająca na rysowanie wylosowanych liter
            na ekranie
        """
        for i in self.picked_letters:
            self.board.blit(self.picked_letters[i], self.letters_positions[i])

    def random_letter(self):
        """
            Metoda losująca liczbę z zakresu 0 do 16
        """
        return random.randint(0, 16)
