import sys, pygame

from InputHandler import *
from AssetManager import *
from Level import *
from ImageComponent import *

class Game:

    __instance = None

    @staticmethod
    def get_instance():
        if Game.__instance == None:
            Game()
        return Game.__instance

    def __init__(self):
        if Game.__instance != None:
            raise Exception("Game Singleton Error")
        else:
            Game.__instance = self

    
    def start(self):
        self.clk = pygame.time.Clock()
        pygame.init()
        self.screen_size = self.screen_width, self.screen_height = 640, 480
        self.screen = pygame.display.set_mode(self.screen_size)
        self.asset_manager = AssetManager()

        ImageComponent.game = Game.get_instance()

        self.level = Level()
        self.level.load()

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