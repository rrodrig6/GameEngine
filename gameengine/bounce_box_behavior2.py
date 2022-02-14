import pygame

class BounceBoxBehavior2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        self.parent.rect.move_ip(1, 1)
        self.do_border_collision(kwargs['game'])
        self.do_sprite_collision(kwargs["collision_group"])


    def do_border_collision(self, game):

        if self.parent.rect.left < 0 or self.parent.rect.right > game.screen_width:
           self.parent.speed[0] = -self.parent.speed[0]

        if self.parent.rect.top < 0 or self.parent.rect.bottom > game.screen_height:
           self.parent.speed[1] = -self.parent.speed[1]

    def do_sprite_collision(self, collision_group):
        collision_list = pygame.sprite.spritecollide(self.parent, collision_group, False)
        for i in collision_list:
            if i != self:
                if abs(self.parent.rect.y-i.rect.y) < abs(self.parent.rect.x-i.rect.x):
                    self.parent.speed[0] = -self.parent.speed[0]
                else:
                    self.parent.speed[1] = -self.parent.speed[1]