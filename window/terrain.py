import pygame
from shared.entities.wall import Wall
from shared.entities.path import Path
from shared.entities.items import Items
from shared.entities.special_tiles import SpecialTile
from shared.config import * # Enlever

class Terrain():
    """
    This is the terrain construction class. This will assemble every parts of the terrain:
    the path, the walls, the items and the special tiles, and check events on the terrain.
    """
    def __init__(self):

        self.scale = 20
        self.width = 15
        self.height = 15

        self.wall = Wall()
        self.path = Path()
        self.items = Items()
        self.special_tiles = SpecialTile()

        self.num_caught_items = 20

    def draw(self):
        """
        Calling the elements that appears in the window.
        """
        self.path.draw()
        self.wall.draw()
        self.items.draw()
        self.special_tiles.draw()

    def check_events(self, character):
        """
        Checking if items are caught cause those need to appear in the inventory, and checking
        special tiles coordinate.  
        Return a bool and a string that indicates the game is over and the message that needs to appear
        on the end screen.
        """
        for coordinate in self.items.get_coordinates():
            if (character.x, character.y) == coordinate:
                caught_item = self.items.caught((character.x, character.y))
                try:
                    DISPLAY_SURFACE.blit(caught_item, (self.num_caught_items, 280))
                except:
                    pass
                self.items.delete_item((character.x, character.y))
                self.num_caught_items += 20

        if (character.x, character.y) == self.special_tiles.get_coordinates()[1][0]:
            if self.items.get_collected_items() == 4:
                return (True, 'You Win !')
            else:
                return (True, 'You Lose !')

        return (False,)
