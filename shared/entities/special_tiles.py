import pygame
from shared.config import *

class SpecialTile():
    """
    This object load the special effect tiles, that is the ending and starting
    points.
    """
    def __init__(self):

        self.scale = 20

        self.end_x = 0
        self.end_y = 0

        self.start_x = 0
        self.start_y = 0

        self.start_coordinates = []
        self.end_coordinates = []

        self.end_picture = pygame.image.load('graphics/Gardien.png')
        self.end_picture = pygame.transform.scale(self.end_picture, (20, 20))

        self.read_map()

    def read_map(self):
        with open('levels/lvl', 'r+') as lvl:

            for y, line in enumerate(lvl.readlines()):
                for x, letter in enumerate(line):
                    if letter == 'P':
                        self.start_coordinates.append((x * self.scale, y * self.scale))
                    if letter == 'E':
                        self.end_coordinates.append((x * self.scale, y * self.scale))
                    

    def draw(self):
        for coordinate in self.start_coordinates:
            startpoint = pygame.Rect(coordinate[0], coordinate[1], self.scale, self.scale)
            pygame.draw.rect(DISPLAY_SURFACE, (255,255,255), startpoint, 0)

        for coordinate in self.end_coordinates:
            DISPLAY_SURFACE.blit(self.end_picture, coordinate)

    def get_coordinates(self):
        return self.start_coordinates, self.end_coordinates
