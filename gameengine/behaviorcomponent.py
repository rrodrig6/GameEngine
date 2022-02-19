import pygame, yaml

from .behaviors.bounce_box_behavior import *
from .behaviors.bounce_box_behavior2 import *
from .behaviors.player_behavior import *
#from .behaviors import *


class BehaviorComponent(yaml.YAMLObject, pygame.sprite.Sprite):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!BehaviorComponent'
    
    @classmethod
    def from_yaml(cls, loader, node):
        behavior = loader.construct_mapping(node)
        behavior_name = behavior['name']
        behavior_constructor = globals()[behavior_name]
        return behavior_constructor()