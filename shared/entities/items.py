import pygame
from shared.config import *
from shared.entities.path import Path
import random

class Items():
    """
    Unlinke walls or path which are one item with a list of instances, the Items
    object is working for a list of different items.
    Each item in the list has a unique position (that is random), and a unique picture
    (that was setup at init.).
    
    The caught method returns the pygame image object of the item that's the same position
    as the character, so it can be displayed in the inventory, that is for now, some empty blocks
    on the terrain.


    """
    def __init__(self):
        self.path = Path()

        self.load_pics = [(pygame.image.load('graphics/aiguille.png')), (pygame.image.load('graphics/seringue.png')), (pygame.image.load('graphics/ether.png')), (pygame.image.load('graphics/tube_plastique.png'))]
        self.pictures = []
        self.items_coordinates = []

        for picture in self.load_pics:
            self.pos = self.x, self.y = self.path.get_coordinates()[random.randint(0, self.path.get_coordinates().__len__() - 1)]
            picture = pygame.transform.scale(picture, (20, 20))
            self.pictures.append((picture, self.pos))

        self.collected_items = 0
        
    
    def draw(self):

        for picture in self.pictures:
            self.items_coordinates.append(picture[1])
            DISPLAY_SURFACE.blit(picture[0], picture[1])

    def get_coordinates(self):

        return self.items_coordinates

    def caught(self, character_coordinate):

        for picture_and_coordinate in self.pictures:
            if picture_and_coordinate[1] == character_coordinate:
                self.collected_items +=1
                return picture_and_coordinate[0]

    def delete_item(self, character_coordinate):

        for i, picture_and_coordinate in enumerate(self.pictures):
            if picture_and_coordinate[1] == character_coordinate:
                for j, item_coordinate in enumerate(self.items_coordinates):
                    if item_coordinate == picture_and_coordinate[1]:
                        self.items_coordinates.pop(j)
                self.pictures.pop(i)

    def get_collected_items(self):
        return self.collected_items
