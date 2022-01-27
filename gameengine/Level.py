import pygame, os, yaml

from GameObject import *
from PlayerObject import *
from ImageComponent import *

class Level:
    def __init__(self):
        self.background_sprites = pygame.sprite.Group()
        self.game_objects = pygame.sprite.Group()

    def load(self):

        with open('data\levels.yml', 'r') as stream:
            level = yaml.safe_load(stream)
        for object in level['level1']['objects']:
            object_constructor = globals()[object['class']]
            new_object = object_constructor()
            for component in object['components']:
                component_constructor = globals()[component['class']]
                new_component = component_constructor(**component['arguments'])
                new_object.attach_component(new_component)
            new_object.rect.x = object['x']
            new_object.rect.y = object['y']
            self.game_objects.add(new_object)

    def draw(self,*args, **kwargs):
        self.background_sprites.draw(kwargs['screen'])
        self.game_objects.draw(kwargs['screen'])
        
    def update(self, *args, **kwargs):
        self.game_objects.update(collision_group = self.game_objects, **kwargs)