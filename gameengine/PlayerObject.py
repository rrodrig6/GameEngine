import pygame

from GameObject import *
from InputHandler import *

class PlayerObject(GameObject):
    def __init__(self, asset_manager):
        super().__init__(asset_manager)
        self.image = asset_manager.images["square_blue_64x"]
        print("PlayerObject image: "+str(id(self.image)))
        self.last_button_state = False

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if not self.last_button_state and InputHandler.get_instance().mouse_state.left:
            self.last_button_state = True
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        if self.last_button_state and not InputHandler.get_instance().mouse_state.left:
            self.last_button_state = False