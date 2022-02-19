__version__ = '0.1.0'

from gameengine.Game import *

def main():
    game = Game.get_instance()
    game.start()
    while 1:
        game.loop()
    

if __name__ == "__main__":
    main()