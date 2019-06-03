import pygame


class Resize(object):

    def __init__(self):
        pass

    def resize(self, img):
        """
        :return: przeskalowany obraz
        """
        size = img.get_size()
        size = int(size[0] / 2), int(size[1] / 2)
        img = pygame.transform.scale(img, size)
        return img