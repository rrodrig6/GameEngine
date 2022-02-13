import os, pygame, yaml

class AssetManager:

    def __init__(self):
        self.images = {}
        self.load_images()

    #Load images, handling alpha conversion for images with alpha layer, no alpha, and colorkey-based transparency
    def load_images(self):
        
        with open('data\images.yml', 'r') as stream:
            images = yaml.safe_load(stream)
        for image in images:
            image_surface = pygame.image.load(os.path.join('assets', image['path']))
            if image['alpha']=='pixel':
                self.images[image['name']] = pygame.Surface.convert_alpha(image_surface)
            elif image['alpha']=='none':
                self.images[image['name']] = pygame.Surface.convert(image_surface)
            else:
                self.images[image['name']] = pygame.Surface.convert(image_surface)
                self.images[image['name']].set_colorkey(pygame.Color(image['alpha']['R'], image['alpha']['G'], image['alpha']['B']))
                self.images[image['name']].get_colorkey()
