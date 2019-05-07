import pygame
from MainWindow import Window
import ButtonClass as button
import FrameClass as frame
import LetterClass as letters
from ActionClass import Actions


class Game(Window):

    def __init__(self):
        """zainicjowanie okienka"""
        pygame.init()
        super().__init__()
        self.board = pygame.display.get_surface()
        self.FPS = 10
        self.clock = pygame.time.Clock()
        self.buttons = button.Button()
        self.actions = Actions()
        self.letters = letters.Letter()
        self.frames = frame.Frame()

    def draw(self):
        self.draw_window()
        self.buttons.draw_button()
        self.letters.draw_letters()
        # self.actions.draw_actions()
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
            #else:
            #    self.buttons.draw_button()

    #def move_frame_main(self):
    #    self.frames.move_frame()


if __name__ == '__main__':
    game = Game()
    game.run()