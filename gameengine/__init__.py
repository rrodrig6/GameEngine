__version__ = '0.1.0'

import sys, pygame
from Game import *

def main():
    game = Game()
    while 1:
        game.loop()
    

if __name__ == "__main__":
    print (sys.version)
    main()