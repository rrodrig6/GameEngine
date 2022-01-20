import sys, pygame

class InputHandler:
    def __init__(self):
        self.mouse_state = MouseState()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                self.mouse_state.update()

class MouseState:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.left = False
        self.middle = False
        self.right = False

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.left, self.middle, self.right = pygame.mouse.get_pressed()

    def __str__(self):
        state_string = "("+str(self.x)+","+str(self.y)+")"
        if self.left: state_string = state_string + " L"
        if self.middle: state_string = state_string + " M"
        if self.right: state_string = state_string + " R"
        return state_string