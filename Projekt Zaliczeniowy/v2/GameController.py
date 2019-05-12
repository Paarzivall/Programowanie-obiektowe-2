import pygame
import sys
from MainWindow import Window
import ActionClass as actions
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
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def draw_button_start(self):
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
                # pygame.display.update()

    def start_game(self):
        game = Game()
        game.run()

    def message_end(self):
        pass

    def draw(self):
        self.draw_window()
        self.draw_button_start()
        self.message_start()
        pygame.display.update()

    def run(self):
        while not self.handle_events():
            self.draw()
            self.clock.tick(self.FPS)

    def handle_events(self):
        """Metoda pozwalająca zamknąć okienko"""
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
            else:
                continue


if __name__ == '__main__':
    cont = Controller()
    cont.run()