from game_object import GameObject
import pygame
from pygame.locals import *

class GameObjectGround(GameObject):
    def __init__(self, position, size, kind, id):
        super(GameObjectGround, self).__init__(position, size, kind, id)
        
    def tick(self):
        pass
            
    def clicked(self):
        pass