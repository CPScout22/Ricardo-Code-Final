import pygame 
import random
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.timer = 0 #used for sheep movement
        self.randomdirection = 0
        self.clock = pygame.time.Clock()
        self.player = pygame.sprite.GroupSingle()
    def move(self,player_x,player_y):
        
        if player_x > self.rect.x+32:
            self.direction.x += .02
        elif player_x < self.rect.x:
            self.direction.x -= .02
        elif player_y > self.rect.y+32:
            if player_y != self.rect.y:
                self.direction.y += .02
            else:
                self.direction.y = 0
        elif player_y < self.rect.y:
            if player_y != self.rect.y:
                self.direction.y -= .02
            else:
                self.direction.y = 0
        #if self.randomdirection == 0:
         #   self.direction.x -= .2 #move left
        #elif self.randomdirection == 1:
           # self.direction.x += .2 #move right
        #elif self.randomdirection == 2: 
           #self.direction.y -= .2 #move up
        #elif self.randomdirection == 3:
            #self.direction.y += .2 #move down
        else:
            self.direction.y = 0
            self.direction.x = 0
        #return self.randomdirection

    def update(self,amount,player_x,player_y):
        self.move(player_x,player_y)
