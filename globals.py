import pygame

# preset values and colors
SCREEN_WIDTH = 672
SCREEN_HEIGHT = 672

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30

WALL_SIZE = 32

PLAYER_MOVE_SPEED = 3

COIN_AMOUNT = 7

WALL_GEN_PROB = 0.5

ANOTHER_COIN_SPAWN_PROB = 0.5

WIN_SCORE = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)
YELLOW = (255, 225, 0)
PINK = (240, 10, 200)
DARK_GREEN = (30, 180, 10)




level_outline = [
    "WWWWWWWWWWWWWWWWWWWWW",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "W                   W",
    "WWWWWWWWWWWWWWWWWWWWW",
]

players = []
walls = []
coins = []
power_ups = []
non_player_list = [[False for _ in range(21)] for _ in range(21)]


pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 20)