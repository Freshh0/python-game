from pygame.locals import *
from entities import Player

# preset values and colors
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30

WALL_SIZE = 32

PLAYER_MOVE_SPEED = 3

COIN_AMOUNT = 10

WALL_GEN_PROB = 0.45

WIN_SCORE = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)
YELLOW = (255, 225, 0)


players = []
walls = []
coins = []
non_player_list = [[False for _ in range(20)] for _ in range(20)]

players.append(Player(WALL_SIZE, WALL_SIZE, PLAYER_MOVE_SPEED, K_w, K_s, K_a, K_d, RED))
players.append(Player(SCREEN_WIDTH-(2*WALL_SIZE), SCREEN_HEIGHT-(2*WALL_SIZE), PLAYER_MOVE_SPEED, K_UP, K_DOWN, K_LEFT, K_RIGHT, BLUE))
