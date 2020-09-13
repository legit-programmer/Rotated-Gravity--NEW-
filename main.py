import pygame
import random
from pygame.locals import *
import sys
import os

pygame.init()

# Display Initialization

WIDTH = 500
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rotated Gravity By Siddique Khan')
pygame.display.set_icon(pygame.image.load(os.path.join('assets', 'logo.png')))

# Framerate Initialization

FPS = 65 
clock = pygame.time.Clock()

# Font Initialization

main_font = pygame.font.Font('freesansbold.ttf', 75)
enter_font = pygame.font.Font('freesansbold.ttf', 32)
lose_font = main_font.render('You Lose', True, (200, 0, 0))
continue_font = enter_font.render('Press Enter To Continue', True, (97, 204, 142))

# Global Variables

thrust = False
number_of_walls = 4
player = None
wall1 = None
wall2 = None
wallx = []
wally = [HEIGHT, HEIGHT+200, HEIGHT+400, HEIGHT+600]
wally_final = wally.copy()
playerx_final = WIDTH/2 - 32/2
run = True
lose = False

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
        self.x = playerx_final
        self.y = 120
        self.vel_thrust = 10
        self.vel_gravity = 10
        self.color = (97, 114, 204)

    def draw(self):
        global player
        player = pygame.draw.rect(WIN, self.color, (self.x, self.y, 32, 32))

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
        self.color = (204, 46, 90)
    
    def draw(self, x, y):
        global wall1, wall2

        wall1 = pygame.draw.rect(WIN, self.color, (x, y, self.width1, self.height1))
        wall2 = pygame.draw.rect(WIN, self.color, (x+(self.width1+self.offset), y, self.width1, self.height1))

    def checkCollision(self):
        global lose
        if player.colliderect(wall1) or player.colliderect(wall2) or p.x <= 0 or p.x >= WIDTH-32:
            lose = True

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
    global run, FPS, lose_font, continue_font, lose, wally

    if lose:
        while lose:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        lose = False
                        wally = wally_final.copy()
                        p.x = playerx_final
            
            WIN.blit(lose_font, (WIDTH/2-lose_font.get_width()/2, 175))
            WIN.blit(continue_font, (WIDTH/2-continue_font.get_width()/2, 200+lose_font.get_height()+75))

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
    loseScreen()


# Main Game Loop

def main():
    global run, thrust
    
    while run:

        WIN.fill((255, 255, 255))
        applyAllFuncs()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                run = False
        
        keys = pygame.key.get_pressed()

        if keys[K_SPACE]:
            thrust = True

        pygame.display.update()
        clock.tick(FPS)

main()