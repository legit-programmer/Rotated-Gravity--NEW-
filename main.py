import pygame
import random
from pygame.locals import *
import sys

WIDTH = 500
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rotated Gravity By Siddique Khan')

FPS = 65 
clock = pygame.time.Clock()

thrust = False

class Player:
    def __init__(self):
        self.x = WIDTH/2 - 32/2
        self.y = 120
        self.vel_thrust = 10
        self.vel_gravity = 10

    def draw(self):
        pygame.draw.rect(WIN, (0, 0, 255), (self.x, self.y, 32, 32))

    def gravity(self):
        global thrust
        if not thrust:
            if not self.x <= 0:
                self.x-=self.vel_gravity
            

    def thrust(self):
        global thrust
        if thrust:
            if not self.x >= WIDTH-34:
                self.x+=self.vel_thrust
            thrust = False


p = Player()

run = True

def applyAllFuncs():
    p.draw()
    p.gravity()
    p.thrust()

def main():
    global run, thrust
    
    while run:

        WIN.fill((255, 255, 255))
        applyAllFuncs()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()

        if keys[K_SPACE]:
            thrust = True

        pygame.display.update()
        clock.tick(FPS)

main()