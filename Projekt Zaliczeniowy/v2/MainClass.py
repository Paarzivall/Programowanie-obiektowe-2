import pygame
from MainWindow import Window
import ButtonClass as button
import LetterClass as letters
import ActionClass as action


class Game(Window):

    def __init__(self):
        """zainicjowanie okienka"""
        pygame.init()
        super().__init__()
        self.board = pygame.display.get_surface()
        self.FPS = 10
        self.clock = pygame.time.Clock()
        self.buttons = button.Button()
        self.actions = action.Actions()
        self.letters = letters.Letter()

    def draw(self):
        self.draw_window()
        self.buttons.draw_button()
        self.letters.draw_letters()
        self.actions.move_frame()
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


if __name__ == '__main__':
    game = Game()
    game.run()