import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, asset_manager):
        super().__init__()
        # Motion Setup
        self.rect = pygame.Rect(0,0,64,64)
        self.speed = [4,4]
        
        # Image Setup
        self.frame_sheet = asset_manager.images['sheet']
        self.frame_column_count = 5
        self.frame_count = 5
        self.frame_width = 64
        self.frame_height = 64
        self.frame_rate = 5
        self.image_frames = []
        self.create_frames()
        self.image = self.image_frames[0]
        self.frame_rate_count = 0
        self.current_frame = 0

    def create_frames(self):
        for frame in range (0, self.frame_count):
            self.image_frames.append(self.frame_sheet.subsurface(pygame.Rect( (frame%self.frame_column_count)*self.frame_width, (frame//self.frame_column_count)*self.frame_height, self.frame_width, self.frame_height)))

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
        self.rect.move_ip(self.speed)
        self.do_border_collision(kwargs['game'])
        self.do_sprite_collision(kwargs["collision_group"])

        # Update image frame
        
        self.frame_rate_count = self.frame_rate_count + 1
        if self.frame_rate_count >= self.frame_rate:
            self.frame_rate_count = 0
            self.image = self.image_frames[self.current_frame]
            self.current_frame = self.current_frame + 1
            if self.current_frame >= self.frame_count:
                self.current_frame = 0

        

        
    