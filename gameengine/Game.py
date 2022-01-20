import sys, pygame
from GameObject import *
from InputHandler import *

class Game:
    def __init__(self):
        self.clk = pygame.time.Clock()
        pygame.init()
        self.screen_size = self.screen_width, self.screen_height = 640, 480
        self.border_width = 128
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.screen_size)
        self.input_handler = InputHandler()
        pc = GameObject()
        b = GameObject()
        b.rect.x = 128
        b.rect.y = 256
        self.game_objects = pygame.sprite.Group(pc)
        self.game_objects.add(b)

    def process_events(self):
        self.input_handler.update()

    def draw(self):
        self.screen.fill(self.black)
        pygame.draw.rect(self.screen, (128,0,128), pygame.Rect(self.border_width, self.border_width, self.screen_width - (2 * self.border_width), self.screen_height - (2 * self.border_width)))
        self.game_objects.draw(self.screen)
        pygame.display.flip()


    def loop(self):
        self.clk.tick(60)
        self.process_events()   
        self.game_objects.update(self)
        self.draw()