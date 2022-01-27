import pygame

from GameObject import *
from InputHandler import *

class PlayerObject(GameObject):
    def __init__(self):
        super().__init__()
        self.last_button_state = False

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if not self.last_button_state and InputHandler.get_instance().mouse_state.left:
            self.last_button_state = True
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        if self.last_button_state and not InputHandler.get_instance().mouse_state.left:
            self.last_button_state = False