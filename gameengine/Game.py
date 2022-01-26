import sys, pygame

from InputHandler import *
from AssetManager import *
from Level import *

class Game:
    def __init__(self):
        self.clk = pygame.time.Clock()
        pygame.init()
        self.screen_size = self.screen_width, self.screen_height = 640, 480
        self.screen = pygame.display.set_mode(self.screen_size)
        self.asset_manager = AssetManager()
        self.level = Level()
        self.level.load(self.asset_manager)

    def process_events(self):
        InputHandler.get_instance().update()

    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        self.level.draw(screen = self.screen)
        pygame.display.flip()

    def loop(self):
        self.clk.tick(30)
        self.process_events()   
        self.level.update(game = self)
        self.draw()