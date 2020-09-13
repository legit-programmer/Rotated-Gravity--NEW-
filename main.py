import pygame
import random
from pygame.locals import *
import sys

pygame.init()

# Display Initialization

WIDTH = 500
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rotated Gravity By Siddique Khan')

# Framerate Initialization

FPS = 65 
clock = pygame.time.Clock()

# Font Initialization

main_font = pygame.font.Font('freesansbold.ttf', 32)
# lose_font = main_font.render('You Lose')

# Global Variables

thrust = False
number_of_walls = 4
player = None
wall1 = None
wall2 = None
wallx = []
wally = [HEIGHT, HEIGHT+200, HEIGHT+400, HEIGHT+600]
wally_final = wally.copy()
run = True

def getWallStatus():
    """
    This function handles the (x,y) positions of the wall for the first loop.
    """
    global number_of_walls, wally, wallx

    for i in range(number_of_walls):
        randomX = random.randrange(-350, -150)
        wallx.append(randomX)

getWallStatus()


class Player:
    def __init__(self):
        self.x = WIDTH/2 - 32/2
        self.y = 120
        self.vel_thrust = 10
        self.vel_gravity = 10

    def draw(self):
        global player
        player = pygame.draw.rect(WIN, (0, 0, 255), (self.x, self.y, 32, 32))

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
    def __init__(self):
        self.vel = 2
        self.offset = 200
        self.width1 = WIDTH-50
        self.height1 = 32
    
    def draw(self, x, y):
        global wall1, wall2

        wall1 = pygame.draw.rect(WIN, (255, 0, 0), (x, y, self.width1, self.height1))
        wall2 = pygame.draw.rect(WIN, (255, 0, 0), (x+(self.width1+self.offset), y, self.width1, self.height1))

    def checkCollision(self):
        if player.colliderect(wall1) or player.colliderect(wall2) or p.x <= 0 or p.x >= WIDTH-32:
            print('collision detected')

    def move(self):
        global wallx, wally, wally_final, number_of_walls

        for i in range(number_of_walls):
            w.draw(x=wallx[i], y=wally[i])
            wally[i]-=w.vel

            self.checkCollision() # This function is called as this is the loop where walls are generated,so this function will apply for every walls

            if wally[i] <= -32:
                wally[i] = wally_final[i]
            if i == 3:
                if wally[i] <= -32:
                    wally = wally_final.copy()


p = Player()
w = Wall()
    

def loseScreen():
    global run, FPS, lose_font

    while not run:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    run = False
        
        WIN.blit(lose_font, (HEIGHT/2 - lose_font.get_height()/2, WIDTH/2 - lose_font.get_width()/2))
        pygame.display.update()
        clock.tick(FPS)


    

def applyAllFuncs():
    """
    This function collects all the function and then call them together in the main game loop.
    """
    global w, wallx, wally, wally_final

    p.draw()
    p.gravity()
    p.thrust()
    w.move()


# Main Game Loop

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