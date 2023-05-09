import pygame
from settings import *

class Attack():
    def __init__(self,rectx,recty,facing):
        super().__init__()
        self.atkx = rectx
        self.atky = recty
        self.facing = facing


    def attack(self):
        if self.facing == False:
            self.atkx += 30
        else:
            self.atkx -= 30
            
        print("attacking at ",self.atkx," , " ,self.atky )
        pygame.draw.rect(screen,(0,255,255),(self.atkx,self.atky,32,64))
        pygame.display.flip()
