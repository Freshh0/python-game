import pygame
from pygame.locals import *
import sys
import os
import time
import random

# player class
class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(32, 32, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.score = 0

    def move_check(self):

        key = pygame.key.get_pressed()

        if key[K_LEFT]:
            self.move(-PLAYER_MOVE_SPEED, 0)
        if key[K_RIGHT]:
            self.move(PLAYER_MOVE_SPEED, 0)
        if key[K_UP]:
            self.move(0, -PLAYER_MOVE_SPEED)
        if key[K_DOWN]:
            self.move(0, PLAYER_MOVE_SPEED)


    def move(self, xval, yval):

        if xval != 0:
            self.move_single_axis(xval, 0)
        if yval != 0:
            self.move_single_axis(0, yval)

    def move_single_axis(self, xval, yval):

        self.rect.x += xval
        self.rect.y += yval

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if xval > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if xval < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if yval > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if yval < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom



        
# wall class
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], WALL_SIZE, WALL_SIZE)

# coin class
class Coin(object):

    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

    def delete(self):
        coins.remove(self)

# function to spawn a coin
def spawn_coin():
    x = y = 0
    while non_player_list[x][y] != False:
        x = random.randint(1, 18)
        y = random.randint(1, 18)
    coins.append(Coin((x*32 + 8, y*32 + 8)))
    non_player_list[x][y] = True

    




os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()


# preset values and colors
WIN_WIDTH = 640
WIN_HEIGHT = 640

PLAYER_WIDTH = 32
PLAYER_HEIGHT = 32

WALL_SIZE = 32

PLAYER_MOVE_SPEED = 3

COIN_AMOUNT = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)
YELLOW = (255, 225, 0)



# screen setup
screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("Game")

font = pygame.font.Font(pygame.font.get_default_font(), 20)



clock = pygame.time.Clock()
player1 = Player()
walls = []
non_player_list = [[False for _ in range(20)] for _ in range(20)]
coins = []

# basic levels for testing
level = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "WWWWWWWWWWWWWWWWWWWW",
]

level2 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
]

# initialize walls
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
            non_player_list[int(x/32)][int(y/32)] = True
        x += 32
    y += 32
    x = 0

# initialize coins
for i in range(COIN_AMOUNT):
    spawn_coin()


while True:
    # game loop

    clock.tick(60)

    # check for quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()

    # check for player movement
    player1.move_check()

    # check for coin collection
    for coin in coins:
        if coin.rect.colliderect(player1.rect):
            coins.remove(coin)
            player1.score += 1
            non_player_list[coin.rect.x//32][coin.rect.y//32] = False
            # spawn another coin if collected
            spawn_coin()





    # fill background
    screen.fill(BLACK)


    # ----
    # draw
    # ----

    # walls
    for wall in walls:
        pygame.draw.rect(screen, (GREY), wall.rect)

    # coins
    for coin in coins:
        pygame.draw.rect(screen, (YELLOW), coin.rect)

    # players
    pygame.draw.rect(screen, RED, player1.rect)

    # score
    score_text = font.render("Score: " + str(player1.score), True, WHITE, GREY)
    score_rect = score_text.get_rect()
    screen.blit(score_text, score_rect)




    # update screen
    pygame.display.flip()
