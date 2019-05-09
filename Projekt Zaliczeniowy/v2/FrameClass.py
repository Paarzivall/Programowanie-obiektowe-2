import pygame
from ResizeClass import Resize


class Frame(Resize):

    def __init__(self):
        """Tworzy ramkę którą będziemy się poruszać po planszy"""
        self.frame = pygame.image.load('../images/frame.png')
        self.frame_positions = {0: (265, 90), 1: (315, 90), 2: (365, 90),
                                3: (415, 90), 4: (465, 90), 5: (515, 90),
                                6: (565, 90), 7: (615, 90), 8: (665, 90)}
        self.frame = self.resize(self.frame)
        self.board = pygame.display.get_surface()
        self.x = 265
        self.y = 90

    def draw_frame(self, x, y):
        """Rysuje ramkę na ekranie"""
        self.board.blit(self.frame, (x, y))
