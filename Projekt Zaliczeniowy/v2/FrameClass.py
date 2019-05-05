import pygame
from ResizeClass import Resize


class Frame(Resize):

    def __init__(self):
        """Tworzy ramkę którą będziemy się poruszać po planszy"""
        self.frame = pygame.image.load('../images/frame.png')
        self.frame = self.resize(self.frame)
        self.board = pygame.display.get_surface()
        self.x = 265
        self.y = 90

    def draw_frame(self):
        """Rysuje ramkę na ekranie"""
        self.board.blit(self.frame, (self.x, self.y))

    def move_frame(self):
        """Porusza ramką po ekranie"""
        if self.x <= 618:
            self.x += 50
            print(f"x {self.x}")
            self.draw_frame()
        else:
            self.x = 265
            self.draw_frame()
