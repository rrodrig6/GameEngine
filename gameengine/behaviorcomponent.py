import pygame, yaml

from bounce_box_behavior import *
from bounce_box_behavior2 import *

class BehaviorComponent(yaml.YAMLObject, pygame.sprite.Sprite):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!BehaviorComponent'
    
    @classmethod
    def from_yaml(cls, loader, node):
        behavior = loader.construct_mapping(node)
        behavior_constructor = globals()[behavior['name']]
        return behavior_constructor()