import os, pygame, yaml

class AssetManager:

    def __init__(self):
        self.images = {}
        self.load_images()

    def load_images(self):
        
        with open('data\images.yml', 'r') as stream:
            images = yaml.safe_load(stream)
        for image in images:
            image_surface = pygame.image.load(os.path.join('assets', image['path']))
            self.images[image['name']] = pygame.Surface.convert(image_surface)
