import pygame

class PlayerBehavior(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        pushed_keys = pygame.key.get_pressed()
        if pushed_keys[pygame.K_w]:
            self.parent.rect.move_ip(self.parent.speed)