import pygame

from GameObject import *
from PlayerObject import *

class Level:
    def __init__(self):
        self.background_sprites = pygame.sprite.Group()
        self.game_objects = pygame.sprite.Group()

    def load(self):
        pc = PlayerObject()
        b = GameObject()
        b.rect.x = 128
        b.rect.y = 256
        self.game_objects.add(pc)
        self.game_objects.add(b)

    def draw(self,*args, **kwargs):
        self.background_sprites.draw(kwargs['screen'])
        self.game_objects.draw(kwargs['screen'])
        
    def update(self, *args, **kwargs):
        self.game_objects.update(collision_group = self.game_objects, **kwargs)