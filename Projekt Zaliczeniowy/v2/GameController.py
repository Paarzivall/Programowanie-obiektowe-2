import pygame
from MainWindow import Window


class Controller(Window):

    def __init__(self):
        self.background = (255, 153, 51)
        super().__init__(self.background)
        self.FPS = 10
        self.clock = pygame.time.Clock()

    def draw(self):
        self.draw_window()
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
    cont = Controller()
    cont.run()