import pygame 
from attack import Attack
from settings import *
from mouse import Mouse
class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8

    def input(self):
        self.atk = Attack(self.rect.x,self.rect.y,self.direction.x)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            self.atk.attack()
        elif keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.y = 0
            self.direction.x = 0

    def update(self, amount):
        self.input()
