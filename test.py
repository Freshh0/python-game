import pygame
from pygame.locals import *
import sys
import os
import random

# player class
class Player(object):
    def __init__(self, pos_x, pos_y, up, down, left, right, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.Rect(self.pos_x, self.pos_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.score = 0
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.color = color

    def move_check(self):

        key = pygame.key.get_pressed()

        if key[self.left]:
            self.move(-PLAYER_MOVE_SPEED, 0)
        if key[self.right]:
            self.move(PLAYER_MOVE_SPEED, 0)
        if key[self.up]:
            self.move(0, -PLAYER_MOVE_SPEED)
        if key[self.down]:
            self.move(0, PLAYER_MOVE_SPEED)


    def move(self, x_val, y_val):

        if x_val != 0:
            self.move_single_axis(x_val, 0)
        if y_val != 0:
            self.move_single_axis(0, y_val)

    def move_single_axis(self, x_val, y_val):

        self.rect.x += x_val
        self.rect.y += y_val

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if x_val > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if x_val < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if y_val > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if y_val < 0: # Moving up; Hit the bottom side of the wall
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


# function to draw text on screen
def draw_text(text, x, y, color):
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)
    

    

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




pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

# screen setup
screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("Game")

font = pygame.font.Font(pygame.font.get_default_font(), 20)


# game state = play / win
game_state = 'play'

clock = pygame.time.Clock()
players = []
players.append(Player(32, 32, K_w, K_s, K_a, K_d, RED))
players.append(Player(WIN_WIDTH-(2*PLAYER_WIDTH), WIN_HEIGHT-(2*PLAYER_HEIGHT), K_UP, K_DOWN, K_LEFT, K_RIGHT, BLUE))
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

    # ------
    # update
    # ------


    # check for quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()

    if game_state == 'play':


        # check for player movement
        players[0].move_check()
        players[1].move_check()


        for player in players:
            # check for coin collection
            for coin in coins:
                if coin.rect.colliderect(player.rect):
                    coins.remove(coin)
                    player.score += 1
                    if player.score >= 5:
                        game_state = 'win'
                    non_player_list[coin.rect.x//32][coin.rect.y//32] = False
                    # spawn another coin if collected
                    spawn_coin()




    # ----
    # draw
    # ----
    
    # fill background
    screen.fill(BLACK)

    if game_state == 'play':

        # walls
        for wall in walls:
            pygame.draw.rect(screen, (GREY), wall.rect)

        # coins
        for coin in coins:
            pygame.draw.rect(screen, (YELLOW), coin.rect)

        # players
        for player in players:
            pygame.draw.rect(screen, player.color, player.rect)

        # score
        # if len(players) == 2:
        draw_text("Player 1 score: " + str(players[0].score), 10, 5, RED)
        draw_text("Player 2 score: " + str(players[1].score), 470, 5, BLUE)



    if game_state == 'win':
        if players[0].score > players[1].score:
            draw_text("Player 1 wins!", 240, 310, WHITE)
        else:
            draw_text("Player 2 wins!", 240, 310, WHITE)
        




    # update screen
    pygame.display.flip()
