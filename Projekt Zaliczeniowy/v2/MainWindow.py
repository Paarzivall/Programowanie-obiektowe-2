import pygame
import pygame.locals
from ResizeClass import Resize


class Window(Resize):

    def __init__(self, background):
        """ Utworzenie 'czystego okienka' z tłem"""
        pygame.init()
        self.background = background
        self.frame = pygame.display.set_mode((960, 540))
        pygame.display.set_caption("Praca Zaliczeniowa - Mateusz Bugaj")

    def draw_window(self, *args):
        """
        Narysowanie okienka na ekranie
        :param args:
        """
        self.frame.blit(self.background, (0, 0))
        for drawable in args:
            drawable.draw_on(self.frame)
        pygame.display.update()

