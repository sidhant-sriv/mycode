import pygame
pygame.init()
from math import *
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("FISH v1.0")
x = 50
y = 230
width = 40
height = 40
vel = 5

run = True
picture = pygame.image.load('fish-removebg-preview.png')
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((66, 135, 245))
    win.blit(picture, (x,y))
    win.blit(picture, (x,y+100))
    win.blit(picture, (x,y-100))
    win.blit(picture, (x,y-200))
    win.blit(picture, (x,y+200))
    x = x+ vel
    count = 0
    y  = 250 + 15*sin(0.07*x)
 
    if x==500 or x==0:
        vel *= -1
        picture = pygame.transform.flip(picture, True,False)
    pygame.display.update() 
    
pygame.quit()

