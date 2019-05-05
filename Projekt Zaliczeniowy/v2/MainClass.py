import pygame
from MainWindow import Window
import ButtonClass as button


class Game(Window):

    def __init__(self):
        """zainicjowanie okienka"""
        pygame.init()
        super().__init__()
        self.board = pygame.display.get_surface()
        self.FPS = 200
        self.fps_clock = pygame.time.Clock()
        self.buttons = button.Button()

    def draw(self):
        self.draw_window()
        self.buttons.draw_button()
        pygame.display.flip()

    def run(self):
        while not self.handle_events():
            self.draw()
            self.fps_clock.tick(self.FPS)

    def handle_events(self):
        """Metoda pozwalająca zamknąć okienko"""
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
            #elif event.type == pygame.MOUSEBUTTONDOWN:
            #    self.buttons.button_actions(pygame.mouse.get_pos())


if __name__ == '__main__':
   game = Game()
   game.run()