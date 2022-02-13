import pygame, yaml
from pygame.math import Vector2

class GameObject(yaml.YAMLObject, pygame.sprite.Sprite):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!GameObject'

    @classmethod
    def from_yaml(cls, loader, node):
        return GameObject(**loader.construct_mapping(node))


    def __init__(self, x: int=0, y: int=0, components = {} ):
        super().__init__()
        print('GameObject __init__()')
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

    def do_border_collision(self, game):

        if self.rect.left < 0 or self.rect.right > game.screen_width:
           self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > game.screen_height:
           self.speed[1] = -self.speed[1]

    def do_sprite_collision(self, collision_group):
        collision_list = pygame.sprite.spritecollide(self, collision_group, False)
        for i in collision_list:
            if i != self:
                if abs(self.rect.y-i.rect.y) < abs(self.rect.x-i.rect.x):
                    self.speed[0] = -self.speed[0]
                else:
                    self.speed[1] = -self.speed[1]

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        for component in self.components:
            component.update()
            #component.rect.x = self.rect.x
            #component.rect.y = self.rect.y
        
        self.rect.move_ip(self.speed)
        self.do_border_collision(kwargs['game'])
        self.do_sprite_collision(kwargs["collision_group"])
        