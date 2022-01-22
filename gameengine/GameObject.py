import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, asset_manager):
        super().__init__()
        self.image = asset_manager.images["square_red_64x"]
        print("GameObject image: "+str(id(self.image)))
        self.speed = [4,4]
        self.rect = self.image.get_rect()

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

        
    