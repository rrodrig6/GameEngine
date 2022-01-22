import pygame

from GameObject import *
from PlayerObject import *

class Level:
    def __init__(self):
        self.background_sprites = pygame.sprite.Group()
        self.game_objects = pygame.sprite.Group()

    def load(self, asset_manager):
        pc = PlayerObject(asset_manager)
        b = GameObject(asset_manager)
        b.rect.x = 128
        b.rect.y = 256
        c = GameObject(asset_manager)
        c.rect.x = 256
        c.rect.y = 128
        self.game_objects.add(pc)
        self.game_objects.add(b)
        self.game_objects.add(c)

    def draw(self,*args, **kwargs):
        self.background_sprites.draw(kwargs['screen'])
        self.game_objects.draw(kwargs['screen'])
        
    def update(self, *args, **kwargs):
        self.game_objects.update(collision_group = self.game_objects, **kwargs)