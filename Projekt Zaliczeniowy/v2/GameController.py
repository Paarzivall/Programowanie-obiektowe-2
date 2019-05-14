import pygame
import sys
from MainWindow import Window
import ButtonClass as buttons
from MainClass import Game


class Controller(Window):

    def __init__(self):
        self.background = pygame.image.load("../images/chest_controller.png")
        self.background = self.resize(self.background)
        super().__init__(self.background)
        self.rect = pygame.Rect((135, 69), (690, 200))
        self.FPS = 10
        self.clock = pygame.time.Clock()
        self.board = pygame.display.get_surface()
        self.buttons = buttons.Button()
        self.positions = {'Start': (300, 380),
                          'Stop': (500, 380),
                          'Again': (250, 380)}

    def message_start(self):
        """Utworzenie i wypisanie na ekran wiadomości startowej"""
        pygame.draw.rect(self.board, (96, 96, 96), self.rect, 1)
        message = {0: "",
                   1: "Witaj",
                   2: "",
                   3: "",
                   4: "Gra polega na ułożeniu liter",
                   5: "",
                   6: "według kolejności alfabetycznej",
                   7: "",
                   8: "stosując sortowanie bąbelkowe",
                   9: "",
                   10: "Aby rozpocząć naciśnij 'START'"}
        Text_header = pygame.font.SysFont('comicsansms.ttf', 40)
        Text_normal = pygame.font.SysFont('comicsansms.ttf', 25)
        x = 7
        for i in message:
            if i == 1:
                TextSurf, TextRect = self.text_objects(message[i], Text_header)
            else:
                TextSurf, TextRect = self.text_objects(message[i], Text_normal)
            TextRect.center = ((940 / 2), (640 / x))
            self.board.blit(TextSurf, TextRect)
            x -= 0.38

    def text_objects(self, text, font):
        """Przekształcenie tekstu na obiekt pygame"""
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def draw_button_start(self):
        """Narysowanie na ekranie przycisków ekranu startowego"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for i in self.buttons.buttons_controller:
            if i != 'Again':
                self.board.blit(self.buttons.buttons_controller[i], self.positions[i])
                if pygame.MOUSEBUTTONUP:
                    if click == (1, 0, 0):
                        ev = self.board.blit(self.buttons.buttons_controller[i], self.positions[i]).collidepoint(mouse)
                        if ev:
                            self.board.blit(self.buttons.buttons_controller_light[i], self.positions[i])
                            if i == "Start":
                                self.start_game()
                                sys.exit()
                            elif i == "Stop":
                                sys.exit()
                else:
                    self.board.blit(self.buttons.buttons_controller[i], self.positions[i])
                pygame.display.update()

    def start_game(self):
        game = Game()
        game.run()

    def message_end(self):
        """Utworzenie i wypisanie na ekran wiadomości końcowej"""
        pygame.draw.rect(self.board, (96, 96, 96), self.rect, 1)
        message = {0: "",
                   1: "Gratulacje!",
                   2: "",
                   3: "",
                   4: "Udało Ci się ułożyć alfabet",
                   5: "",
                   6: "Jeżeli chcesz zagrać jeszcze raz kliknij 'Jeszcze raz'",
                   7: ""}
        Text_header = pygame.font.SysFont('comicsansms.ttf', 40)
        Text_normal = pygame.font.SysFont('comicsansms.ttf', 25)
        x = 7
        for i in message:
            if i == 1:
                TextSurf, TextRect = self.text_objects(message[i], Text_header)
            else:
                TextSurf, TextRect = self.text_objects(message[i], Text_normal)
            TextRect.center = ((940 / 2), (640 / x))
            self.board.blit(TextSurf, TextRect)
            x -= 0.38

    def draw_button_end(self):
        """Narysowanie na ekranie przycisków ekranu końcowego"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for i in self.buttons.buttons_controller:
            if i != 'Start':
                self.board.blit(self.buttons.buttons_controller[i], self.positions[i])
                if pygame.MOUSEBUTTONUP:
                    if click == (1, 0, 0):
                        ev = self.board.blit(self.buttons.buttons_controller[i], self.positions[i]).collidepoint(mouse)
                        if ev:
                            self.board.blit(self.buttons.buttons_controller_light[i], self.positions[i])
                            if i == "Again":
                                self.start_game()
                                sys.exit()
                            elif i == "Stop":
                                sys.exit()
                else:
                    self.board.blit(self.buttons.buttons_controller[i], self.positions[i])
                pygame.display.update()

    def draw(self, x):
        """główna metoda pozwalająca na rysowanie na ekranie poszczególnych elementów"""
        self.draw_window()
        if x == 1:
            self.draw_button_start()
            self.message_start()
        else:
            self.draw_button_end()
            self.message_end()
        pygame.display.update()

    def run(self, x):
        while not self.handle_events():
            self.draw(x)
            self.clock.tick(self.FPS)

    def handle_events(self):
        """Metoda pozwalająca zamknąć okienko"""
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
            else:
                continue
