import pygame
import time
from shared.config import DISPLAY_SURFACE
from shared.entities.special_tiles import SpecialTile
from shared.entities.character import Character
from window.terrain import Terrain

class Game:
    """
    This is the main game process.
    The instance of Game is called with the run method first.
    """
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.running = True
        self.replay = None
        self.character = Character()
        self.terrain = Terrain()
        self.text_objects = ''
        self.end_title = True
    
    def check_events(self):
        """
        Checking if the user closed the window
        Returns nothing.
        """
        # Checking events ...
        for event in pygame.event.get():
            # Quit condition
            if event.type == pygame.QUIT:
                self.running = False
                self.end_title = False

    def loop(self):
        
        self.character.move()

        if self.terrain.check_events(self.character)[0]:
            self.running = False
        # I use this function to add delay between the character's moves.
        # Warning : This pauses the game, so it works right now, but won't if ennemies are added, 
        # or other kind of real time events.
        pygame.time.wait(100)

        self.character.update()

    def run(self):
        # Main game loop

        while self.running:
            self.terrain.draw()
            # First we check the events.
            self.check_events()
            # Then let's do the actions.
            self.loop()

            # Update the display
            pygame.display.update()

        # Let's bring the player to the end_title announcing if he wins or loses.
        self.end_screen(self.terrain.check_events(self.character)[1])

    def end_screen(self, text):
        myfont = pygame.font.SysFont('Gameplay.ttf', 60)
        textsurface = myfont.render(text, False, (255, 255, 255))
        # Let's loop over the end_title until the user quit the game.
        while self.end_title:
            DISPLAY_SURFACE.fill((0, 0, 0))
            DISPLAY_SURFACE.blit(textsurface, (50, 120))
            self.check_events()
            pygame.display.update()
        # Clean up before we quit.
        pygame.quit()
