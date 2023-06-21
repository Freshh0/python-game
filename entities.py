import pygame
from globals import *

# player class
class Player(object):
    def __init__(self, pos_x, pos_y, move_speed, up, down, left, right, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.init_pos_x = pos_x
        self.init_pos_y = pos_y
        self.move_speed = move_speed
        self.rect = pygame.Rect(self.init_pos_x, self.init_pos_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.score = 0
        self.overall_score = 0
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.color = color

    def move_check(self):

        key = pygame.key.get_pressed()

        if key[self.left]:
            self.move(-self.move_speed, 0)
        if key[self.right]:
            self.move(self.move_speed, 0)
        if key[self.up]:
            self.move(0, -self.move_speed)
        if key[self.down]:
            self.move(0, self.move_speed)


    def move(self, x_val, y_val):
        
        # no idea why, but it has to be that way
        if x_val > 0:
            x_val += 0.5
        if y_val > 0:
            y_val += 0.5
        


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

    def reset(self):
        self.rect = pygame.Rect(self.init_pos_x, self.init_pos_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.score = 0
        self.move_speed = PLAYER_MOVE_SPEED
        
# wall class
class Wall(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], WALL_SIZE, WALL_SIZE)

# coin class
class Coin(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        # self.pickup_sound = pygame.mixer.Sound('coin_pickup_sound.mp3')
        # self.pickup_sound.set_volume(0.3)

    def delete(self):
        coins.remove(self)

# powerup class
class PowerUp(object):
    def __init__(self, pos, type):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.type = type
        # if type == 'speed':
        #     self.pickup_sound = pygame.mixer.Sound('speed_pickup_sound.mp3')
        # elif type == 'size':
        #     self.pickup_sound = pygame.mixer.Sound('size_pickup_sound.mp3')
        # self.pickup_sound.set_volume(0.3)

    def delete(self):
        power_ups.remove(self)