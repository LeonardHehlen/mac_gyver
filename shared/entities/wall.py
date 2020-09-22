import pygame
from shared.config import *

class Wall():
    """
    Wall object works the same as the path object, except it also have a collide box
    object (pygame rectangle) so the character can handle collisions.
    """
    def __init__(self):
        self.x = 0
        self.y = 0        
        self.scale = 20

        self.tiles_pictures = pygame.image.load('graphics/floor-tiles-20x20.png')
        self.collide_box = pygame.Rect(self.x, self.y, self.scale , self.scale)
        self.wall_coordinates = []
        self.wall_pic = self.crop((0, -220))

        self.read_map()

    def crop(self, tile_coordinate):
        # Let's have an empty surface with the size of the scale.
        self.cropped = pygame.Surface((self.scale, self.scale))
        # Then let's paste this surface on the floor-tiles picture with the coordinate of the tile we want to use.
        self.cropped.blit(self.tiles_pictures, tile_coordinate) 
        # That gives us a cropped picture with the right tile at the right scale.
        return self.cropped

    def read_map(self):
        with open('levels/lvl', 'r+') as lvl:

            for y, line in enumerate(lvl.readlines()):
                for x, letter in enumerate(line):
                    if letter == '0':
                        self.wall_coordinates.append((x * self.scale, y * self.scale))

    def draw(self):
        for coordinate in self.wall_coordinates:
            DISPLAY_SURFACE.blit(self.wall_pic, coordinate)

            self.collide_box = pygame.Rect(coordinate[0], coordinate[1], self.scale, self.scale)
            pygame.draw.rect(DISPLAY_SURFACE, (0, 0 ,0), self.collide_box, -1)

    def get_coordinates(self):
        # print(self.wall_coordinates)
        return self.wall_coordinates
