import pygame
from MainClass import Game
from FrameClass import Frame


class Button(Game):

    def __init__(self):
        self.board = pygame.display.get_surface()
        self.buttons = {'L': '../images/button_L.png', 'R': '../images/button_R.png', 'O': '../images/button_O.png'}
        self.buttons_light = {'L': '../images/button_L_light.png', 'R': '../images/button_R_light.png', 'O': '../images/button_O_light.png'}
        self.positions = {'L': (280, 165), 'R': (360, 165), 'O': (680, 165)}
        self.positions_light = {'L': (268, 155), 'R': (348, 155), 'O': (672, 155)}
        self.action = {'L': 'Lewy', 'R': 'Prawy', 'O': 'Mieszaj'}
        self.add_buttons()
        self.add_buttons_light()

    def add_buttons(self):
        for i in self.buttons:
            button = pygame.image.load(self.buttons[i])
            button = self.resize(button)
            self.buttons.update({i: button})

    def add_buttons_light(self):
        for i in self.buttons_light:
            button_light = pygame.image.load(self.buttons_light[i])
            button_light = self.resize(button_light)
            self.buttons_light.update({i: button_light})

    def draw_button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for i in self.buttons:
            self.board.blit(self.buttons[i], self.positions[i])
            if click == (1, 0, 0):
                ev = self.board.blit(self.buttons[i], self.positions[i]).collidepoint(mouse)
                if ev:
                    self.board.blit(self.buttons_light[i], self.positions_light[i])
                    print(self.action[i])
                elif not ev:
                    self.board.blit(self.buttons[i], self.positions[i])