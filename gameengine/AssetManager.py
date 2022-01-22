import os, pygame

class AssetManager:

    def __init__(self):
        self.images = {}
        self.load_images()

    def load_images(self):
        default_image = pygame.Surface((64,64))
        default_image.fill(pygame.Color(255,0,255))
        self.images['default'] = default_image
        
        image_list = ["square_red_64x", "square_blue_64x", "circle_red_64x", "circle_blue_64x"]
        for i in image_list:
            img_surf = pygame.image.load(os.path.join('assets', i+'.png'))
            self.images[i] = pygame.Surface.convert(img_surf)
        