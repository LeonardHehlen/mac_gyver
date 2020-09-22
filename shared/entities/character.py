import pygame
from shared.entities.wall import Wall
from shared.entities.special_tiles import SpecialTile
from shared.entities.items import Items
from shared.config import *

class Character():
    """
    This object is the character entity.
    The 'move' method check the pygame key pressed function and the collision
    check returns if the character can move or not (if there's a wall or not.)

    It's start position is the coordinate of the special tile 'P'.

    """
    def __init__(self):
        self.picture = pygame.image.load('graphics/MacGyver.png')
        self.picture = pygame.transform.scale(self.picture, (20, 20))
        self.special_tile = SpecialTile()
        self.x = self.special_tile.get_coordinates()[0][0][0]
        self.y = self.special_tile.get_coordinates()[0][0][1]
        self.velocity = 20
        self.width = self.picture.get_width()
        self.height = self.picture.get_height()
        self.wall = Wall()
        self.items = Items()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x = self.x - self.wall.scale
            if self.check_collision(x, self.y):
                self.x -= self.velocity
            else:
                pass

        if keys[pygame.K_RIGHT]:
            x = self.x + self.wall.scale
            if self.check_collision(x, self.y):
                self.x += self.velocity
            else:
                pass

        if keys[pygame.K_UP]:
            y = self.y - self.wall.scale
            if self.check_collision(self.x, y):
                self.y -= self.velocity
            else:
                pass

        if keys[pygame.K_DOWN]:
            y = self.y + self.wall.scale
            if self.check_collision(self.x, y):
                self.y += self.velocity
            else:
                pass
        
    def check_collision(self, x, y):
        for coordinate in self.wall.get_coordinates():
            if (x, self.y) == coordinate:
                return False
        for coordinate in self.wall.get_coordinates():
            if (self.x, y) == coordinate:
                return False
        return True



    def update(self):
        self.collide_box = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(DISPLAY_SURFACE, (0, 0 ,0), self.collide_box, -1)
        DISPLAY_SURFACE.blit(self.picture, (self.x,self.y))
