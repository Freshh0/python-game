import pygame
from pygame.locals import *
import sys
import os
import random

from level_gen import generate_level, check_validity
import globals
from entities import Coin, Wall

# function to spawn a coin
def spawn_coin():
    x = y = 0
    while globals.non_player_list[x][y] != False:
        x = random.randint(1, 18)
        y = random.randint(1, 18)
    globals.coins.append(Coin((x*32 + 8, y*32 + 8)))
    globals.non_player_list[x][y] = True


# function to draw text on screen
def draw_text(text, x, y, color):
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)
    

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

# screen setup
screen = pygame.display.set_mode((globals.SCREEN_WIDTH,globals.SCREEN_HEIGHT))
pygame.display.set_caption("Game")

font = pygame.font.Font(pygame.font.get_default_font(), 20)


# game state = play / win
game_state = 'play'

clock = pygame.time.Clock()

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

level_rand = generate_level(level, globals.WALL_GEN_PROB)
level_rand = check_validity(level_rand)

# initialize walls
x = y = 0
for row in level_rand:
    for col in row:
        if col == "W":
            Wall((x, y))
            globals.non_player_list[int(x/32)][int(y/32)] = True
        x += 32
    y += 32
    x = 0

# initialize coins
for i in range(globals.COIN_AMOUNT):
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
        globals.players[0].move_check()
        globals.players[1].move_check()


        for player in globals.players:
            # check for coin collection
            for coin in globals.coins:
                if coin.rect.colliderect(player.rect):
                    globals.coins.remove(coin)
                    player.score += 1
                    if player.score >= globals.WIN_SCORE:
                        game_state = 'win'
                    globals.non_player_list[coin.rect.x//32][coin.rect.y//32] = False
                    # spawn another coin if collected
                    spawn_coin()




    # ----
    # draw
    # ----
    
    # fill background
    screen.fill(globals.BLACK)

    if game_state == 'play':

        # walls
        for wall in globals.walls:
            pygame.draw.rect(screen, (globals.GREY), wall.rect)

        # coins
        for coin in globals.coins:
            pygame.draw.rect(screen, (globals.YELLOW), coin.rect)

        # players
        for player in globals.players:
            pygame.draw.rect(screen, player.color, player.rect)

        # score
        # if len(players) == 2:
        draw_text("Player 1 score: " + str(globals.players[0].score), 10, 5, globals.RED)
        draw_text("Player 2 score: " + str(globals.players[1].score), 460, 5, globals.BLUE)



    if game_state == 'win':
        if globals.players[0].score > globals.players[1].score:
            draw_text("Player 1 wins!", 240, 310, globals.WHITE)
        else:
            draw_text("Player 2 wins!", 240, 310, globals.WHITE)
        

    # update screen
    pygame.display.flip()
