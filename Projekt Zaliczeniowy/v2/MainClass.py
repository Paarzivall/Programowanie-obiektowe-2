import pygame
from MainWindow import Window
import ButtonClass as button
import LetterClass as letters
import ActionClass as action


class Game(Window):

    def __init__(self):
        """zainicjowanie okienka"""
        pygame.init()
        self.background = pygame.image.load("../images/chest.png")
        self.background = self.resize(self.background)
        super().__init__(self.background)
        self.board = pygame.display.get_surface()
        self.FPS = 10
        self.clock = pygame.time.Clock()
        self.buttons = button.Button()
        self.letters = letters.Letter()
        self.letters.pick_letter()

    def draw(self):
        """
            metoda pozwalająca rysować na ekranie,
            wywołuje metody z innych klas odpowiedzialne
            za poszczególne elementy
        """
        self.draw_window()
        self.letters.draw_letters()
        self.buttons.draw_button()
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

