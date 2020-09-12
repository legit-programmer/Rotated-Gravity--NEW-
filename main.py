import pygame
import random
from pygame.locals import *
import sys

pygame.init()

WIDTH = 500
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rotated Gravity By Siddique Khan')

FPS = 65 
clock = pygame.time.Clock()

thrust = False
number_of_walls = 4
wallx = []
wally = []

def getWallStatus():
    global number_of_walls, wally, wallx

    for i in range(number_of_walls):
        randomX = random.randrange(-250, -120)
        randomY = random.randrange(250, HEIGHT)
        wallx.append(randomX)
        wally.append(randomY)

getWallStatus()

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


class Wall:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.vel = 10
        self.offset = 125
        self.width1 = WIDTH-50
        self.height1 = 32
    
    def draw(self):
        wall1 = pygame.draw.rect(WIN, (255, 0, 0), (self.x1, self.y1, self.width1, self.height1))
        wall2 = pygame.draw.rect(WIN, (255, 0, 0), (self.x1+(self.width1+self.offset), self.y1, self.width1, self.height1))

    def move(self):
        pass


p = Player()

# for i in range(number_of_walls):
#     print(wallx, wally)
#     w = Wall(x1=wallx[i], y1=wally[i]+25)
    
    
run = True

def applyAllFuncs():
    global w

    p.draw()
    p.gravity()
    p.thrust()
    # w.draw()
    # w.x1-=w.vel
    

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