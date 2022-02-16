import pygame, yaml

class ImageComponent(yaml.YAMLObject, pygame.sprite.Sprite):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!ImageComponent'
    game = None

    @classmethod
    def from_yaml(cls, loader, node):
        return ImageComponent(**loader.construct_mapping(node))
    
    def __init__(
            self, 
            parent = None, 
            image_name: str = None, 
            column_count: int = 1, 
            frame_count: int = 1, 
            width: int = 64, 
            height: int = 64, 
            rate: int = 1, 
            name: str = "ImageComponent",
            group_list = ['render']
    ):
        super().__init__()
        self.parent = parent
        self.sheet = ImageComponent.game.asset_manager.images[image_name]
        self.column_count = column_count
        self.frame_count = frame_count
        self.width = width
        self.height = height
        self.rate = rate
        self.name = name
        self.group_list = group_list
        
        self.frames = []
        self.rate_count = 0
        self.current_frame = 0

        self.create_frames()
        self.register_groups()
        self.image = self.frames[self.current_frame]
        self.rect = pygame.rect.Rect(0,0,0,0)
        
    def create_frames(self) -> None:
        for frame in range (0, self.frame_count):
            self.frames.append(self.sheet.subsurface(pygame.Rect( (frame%self.column_count)*self.width, (frame//self.column_count)*self.height, self.width, self.height)))

    def register_groups(self) -> None:
        ImageComponent.game.level.draw_objects.add(self)

    def update(self, *args, **kwargs) -> None:
        self.rate_count = self.rate_count + 1
        if self.rate_count >= self.rate:
            self.rate_count = 0
            self.current_frame = self.current_frame + 1
            if self.current_frame >= self.frame_count:
                self.current_frame = 0
        self.image = self.frames[self.current_frame]
        if(self.parent):
            self.rect.x = self.parent.rect.x
            self.rect.y = self.parent.rect.y