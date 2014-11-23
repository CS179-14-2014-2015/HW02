import pygame,sys
from pygame.locals import *

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0
pygame.init()
screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('cat.png').convert()
background = pygame.image.load('cat.png').convert()
screen.blit(background, (0, 0))
objects = []
for x in range(10): 		#create 10 objects
    o = GameObject(player, x*40, x)
    objects.append(o)
while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
           sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    pygame.time.delay(100)