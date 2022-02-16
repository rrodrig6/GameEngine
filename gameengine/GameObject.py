import pygame, yaml
from pygame.math import Vector2



class GameObject(yaml.YAMLObject, pygame.sprite.Sprite):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!GameObject'

    @classmethod
    def from_yaml(cls, loader, node):
        return GameObject(**loader.construct_mapping(node))


    def __init__(self, x: int=0, y: int=0, components = {}):
        super().__init__()
        # Motion Setup
        self.position = Vector2(x,y)
        self.image = pygame.Surface((0,0))
        self.components = components
        self.rect = pygame.Rect(self.position.x, self.position.y,0,0)
        self.speed = [4,4]

    def component_setup(self):
        for component in self.components:
            component.parent = self
        
    def attach_component(self, component) -> None:
        self.components[component.name] = component


    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        for component in self.components:
            component.update(*args, **kwargs)
        
        
        