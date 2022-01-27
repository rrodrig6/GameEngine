import pygame

from GameObject import *
from AssetManager import *

class ImageComponent():

    def __init__(
            self, 
            parent: GameObject = None, 
            image_name: str = None, 
            column_count: int = 1, 
            frame_count: int = 1, 
            width: int = 64, 
            height: int =64, 
            rate: int = 1, 
            name: str = "ImageComponent"
    ):
        self.parent = parent
        self.sheet = AssetManager.get_instance().images[image_name]
        self.column_count = column_count
        self.frame_count = frame_count
        self.width = width
        self.height = height
        self.rate = rate
        self.name = name
        
        self.frames = []
        self.rate_count = 0
        self.current_frame = 0

        self.create_frames()
        

    def create_frames(self) -> None:
        for frame in range (0, self.frame_count):
            self.frames.append(self.sheet.subsurface(pygame.Rect( (frame%self.column_count)*self.width, (frame//self.column_count)*self.height, self.width, self.height)))

    def update(self) -> None:
        self.rate_count = self.rate_count + 1
        if self.rate_count >= self.rate:
            self.rate_count = 0
            self.current_frame = self.current_frame + 1
            if self.current_frame >= self.frame_count:
                self.current_frame = 0

    def get_current_image(self) -> pygame.Surface:
        return self.frames[self.current_frame]