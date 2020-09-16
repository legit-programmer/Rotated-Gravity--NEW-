"""
ROTATED GRAVITY NY SIDDIQUE KHAN

WEBSITE:- https://hellocodersweb.herokuapp.com
COVID-19 TRACKER BY ME:- https://tracks-covid.herokuapp.com
FOLLOW ON INSTAGRAM:- https://www.instagram.com/programmer_py.sid
FOLLOW ON TWITTER:- https://www.twitter.com/programmerpysid
GITHUB:- https://www.github.com/programmer-py-sid

Thank You :)
"""


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

# Images

welc_img = pygame.image.load(os.path.join('assets','welcome.png'))

# Font Initialization

main_font = pygame.font.Font('freesansbold.ttf', 75)
enter_font = pygame.font.Font('freesansbold.ttf', 32)
lose_font = main_font.render('You Lose', True, (214, 72, 29))
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
score = 0
welcome = True

def getWallStatus():
    """
    This function handles the (x,y) positions of the wall for the first loop.
    """
    global number_of_walls, wally, wallx

    for i in range(number_of_walls):
        randomX = random.randrange(-350, -150)
        wallx.append(randomX)

getWallStatus()

def blitScore():
    score_font = enter_font.render(f'SCORE: {score}', True, (32, 198, 214))
    WIN.blit(score_font, (10, 10)) 

def blitHighscore():
    
    hscore = int(open(os.path.join('data', 'HighScore.txt'), 'r').read())
    
    if score > hscore:
        # File Handling Below:-
        hscore = open(os.path.join('data', 'HighScore.txt'), 'w')
        hscore.write(str(score))
        hscore.close()
        hscore = int(open(os.path.join('data', 'HighScore.txt'), 'r').read())
    
    hfont = enter_font.render(f'HIGH SCORE: {hscore}', True, (64, 101, 204))
    WIN.blit(hfont, (WIDTH/2-hfont.get_width()/2, 200+lose_font.get_height()+75))
        

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
        self.x = None
        self.y = None
    
    def draw(self):
        global wall1, wall2

        wall1 = pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width1, self.height1))
        wall2 = pygame.draw.rect(WIN, self.color, (self.x+(self.width1+self.offset), self.y, self.width1, self.height1))

    def checkCollision(self):
        global lose, score

        if player.colliderect(wall1) or player.colliderect(wall2) or p.x <= 0 or p.x >= WIDTH-32:
            lose = True
        else:
            if p.y == self.y:
                score+=1
                blitScore()
                

    def move(self):
        global wallx, wally, wally_final, number_of_walls

        for i in range(number_of_walls):

            self.x, self.y = wallx[i], wally[i]
            w.draw()
            wally[i]-=w.vel

            self.checkCollision() # This function is called as this is the loop where walls are generated,so this function will apply for every walls

            if wally[i] <= -32:
                wally[i] = wally_final[i]
            if i == 3:
                if wally[i] <= -32:
                    wally = wally_final.copy()


p = Player()
w = Wall()

def welcScreen():
    global welcome

    if welcome:
        while welcome:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        welcome = False
            
            WIN.blit(welc_img, (0, 0))

            pygame.display.update()
            clock.tick(FPS)


# Lose Screen

def loseScreen():
    global run, FPS, lose_font, continue_font, lose, wally, score

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
            
            score_font = main_font.render(str(score), True, (255, 255, 255))

            WIN.blit(lose_font, (WIDTH/2-lose_font.get_width()/2, 100))
            pygame.draw.rect(WIN, (229, 207, 86), (WIDTH/2-80/2,143+lose_font.get_height(), 80, 80))
            WIN.blit(score_font, (WIDTH/2 - score_font.get_width()/2, 150+lose_font.get_height()))
            blitHighscore()
            WIN.blit(continue_font, (WIDTH/2-continue_font.get_width()/2, 250+lose_font.get_height()+75))
            
            pygame.display.update()
            clock.tick(FPS)

        score = 0


def applyAllFuncs():
    """
    This function collects all the function and then call them together in the main game loop.
    """

    p.draw()
    p.gravity()
    p.thrust()
    w.move()
    loseScreen()
    blitScore()
    welcScreen()


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
