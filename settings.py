import pygame as py
LEVEL_ONE = [
'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ',#1
'x                                                         ',#2
'x                   x                                     ',#3
'x                   x                                     ',#4
'x                   x                                     ',#5
'x    e              x                                     ',#6
'xxxxxxxxxxxxx       x                                     ',#7
'x                x  x                                     ',#8
'xp                 xx                                     ',#9
'xxxxxx   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ']#10
#1234567890123456789012345679
start = False
tile_size = 64
SCREEN_WIDTH = 1280
SCREEN_HIEGHT = len(LEVEL_ONE * tile_size)
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
