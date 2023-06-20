from globals import *
import random
from entities import Coin, Wall, Player
from level_gen import generate_level, check_validity

# function to draw text on screen
def draw_text(screen, text, x, y, color):
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)

# function to draw text on screen
def draw_text_center(screen, text, x, y, color):
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)

# function to spawn a coin
def spawn_coin():
    x = y = 0
    while non_player_list[x][y] != False:
        x = random.randint(1, 19)
        y = random.randint(1, 19)
    coins.append(Coin((x*32 + 8, y*32 + 8)))
    non_player_list[x][y] = True

# function to initialize walls
def init_walls():
    level_rand = generate_level(level_outline, WALL_GEN_PROB)
    level_rand_checked = check_validity(level_rand)
    x = y = 0
    for row in level_rand_checked:
        for col in row:
            if col == "W":
                walls.append(Wall((x, y)))
                non_player_list[int(x/32)][int(y/32)] = True
            x += 32
        y += 32
        x = 0

# function to initialize coins
def init_coins():
    coins.append(Coin((19*32 + 8, 32 + 8)))
    coins.append(Coin((32 + 8, 19*32 + 8)))
    coins.append(Coin((10*32 + 8, 10*32 + 8)))
    coins.append(Coin((32 + 8, 10*32 + 8)))
    coins.append(Coin((10*32 + 8, 32 + 8)))
    coins.append(Coin((19*32 + 8, 10*32 + 8)))
    coins.append(Coin((10*32 + 8, 19*32 + 8)))
    non_player_list[18][1] = True
    non_player_list[1][18] = True
    non_player_list[9][9] = True
    non_player_list[1][9] = True
    non_player_list[9][1] = True
    non_player_list[18][9] = True
    non_player_list[9][18] = True
    while len(coins) < COIN_AMOUNT:
        spawn_coin()

# function to load all entities
def load_game():
    if len(players) == 0:
        players.append(Player(WALL_SIZE, WALL_SIZE, PLAYER_MOVE_SPEED, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, RED))
        players.append(Player(SCREEN_WIDTH-(2*WALL_SIZE), SCREEN_HEIGHT-(2*WALL_SIZE), PLAYER_MOVE_SPEED, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, BLUE))

    init_walls()
    init_coins()

# function to unload all entities
def unload_game():
    for player in players:
        player.reset()

    while len(coins) > 0:
        coins.pop()
    
    while len(walls) > 0:
        walls.pop()

    for row in range(len(non_player_list)):
        for col in non_player_list[row]:
            non_player_list[row][col] = False



