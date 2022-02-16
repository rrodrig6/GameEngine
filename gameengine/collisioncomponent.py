import pygame, yaml

class CollisionComponent(yaml.YAMLObject, pygame.sprite.Sprite):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!CollisionComponent'
    game = None

    @classmethod
    def from_yaml(cls, loader, node):
        return CollisionComponent(**loader.construct_mapping(node))
    
    def __init__(
            self, 
            parent = None, 
            width: int = 128, 
            height: int = 128, 
            name: str = "CollisionComponent",
            group_list = ['collision']
    ):
        super().__init__()
        self.parent = parent
        self.width = width
        self.height = height
        self.name = name
        self.group_list = group_list

        self.register_groups()
        self.image = pygame.Surface((0,0))
        self.rect = pygame.rect.Rect(0,0,width,height)
        
    def register_groups(self) -> None:
        CollisionComponent.game.level.collision_objects.add(self)

    def update(self, *args, **kwargs) -> None:
        collision_list = pygame.sprite.spritecollide(self, self.game.level.collision_objects, False)
        if(collision_list):
            for i in collision_list:
                if i != self:
                    print("collided")

        if(self.parent):
            self.rect.x = self.parent.rect.x
            self.rect.y = self.parent.rect.y