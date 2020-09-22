import pygame
from shared.config import *



class Path():
    """
    This object crop the floor tiles picture at a certain coordinate, so you can chose
    it's appearance by changing the cropped_pic_coordinates variable.
    Then it reads the map and append the coordinates of each '1' in the lvl file.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tiles_pictures = pygame.image.load('graphics/floor-tiles-20x20.png')
        self.scale = 20
        self.path_coordinates = []
        self.cropped_pic_coordinates = (-20, 0)
        self.path_pic = self.crop(cropped_pic_coordinates)

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
                    if letter == '1':
                        self.path_coordinates.append((x * self.scale, y * self.scale))

    def draw(self):
        for coordinate in self.path_coordinates:
            DISPLAY_SURFACE.blit(self.path_pic, coordinate)
    
    def get_coordinates(self):

        return self.path_coordinates
