import pygame

class BounceBoxBehavior(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        self.parent.rect.move_ip(self.parent.speed)
        self.do_border_collision(kwargs['game'])
        self.handle_collision_events()

    def handle_collision_events(self):
        if(self.parent.collision_events):
            for i in self.parent.collision_events:
                if abs(self.parent.rect.y-i.rect.y) < abs(self.parent.rect.x-i.rect.x):
                    self.parent.speed[0] = -self.parent.speed[0]
                else:
                    self.parent.speed[1] = -self.parent.speed[1]
        self.parent.collision_events = []

    def do_border_collision(self, game):
        if self.parent.rect.left < 0 or self.parent.rect.right > game.screen_width:
           self.parent.speed[0] = -self.parent.speed[0]
        if self.parent.rect.top < 0 or self.parent.rect.bottom > game.screen_height:
           self.parent.speed[1] = -self.parent.speed[1]