import pygame
from ResizeClass import Resize


class Frame(Resize):

    def __init__(self):
        self.frame = pygame.image.load('../images/frame.png')
        self.frame = self.resize(self.frame)
        self.board = pygame.display.get_surface()
        self.x = 265
        self.y = 90

    def draw_frame(self):
        #self.frame.fill((0, 0, 0, 0))
        self.board.blit(self.frame, (self.x, self.y))

    def move_frame(self):
        while self.x <= 618:
            self.x += 50
            self.draw_frame()