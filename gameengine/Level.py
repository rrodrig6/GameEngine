import pygame, yaml

from .GameObject import *
from .PlayerObject import *
from .ImageComponent import *
from .behaviorcomponent import *
from .collisioncomponent import *

class Level:
    def __init__(self):
        self.game_objects = pygame.sprite.Group()
        self.draw_objects = pygame.sprite.Group()
        self.collision_objects = pygame.sprite.Group()

    def load(self):
        with open('data\objects.yml', 'r') as stream:
            loaded_objects = yaml.load(stream, Loader=yaml.SafeLoader)
        for obj in loaded_objects:
            obj.component_setup()
        self.game_objects.add(loaded_objects)

    def draw(self,*args, **kwargs):
        self.draw_objects.draw(kwargs['screen'])
        
    def update(self, *args, **kwargs):
        self.game_objects.update(collision_group = self.game_objects, **kwargs)