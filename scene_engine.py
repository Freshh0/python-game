import pygame
import utils
from globals import *
import random


class Scene():
    def __init__(self):
        pass
    def on_enter(self):
        pass
    def on_exit(self):
        pass
    def input(self, sm, input_stream):
        pass
    def update(self, sm):
        pass
    def draw(self, screen):
        pass


class MainMenuScene(Scene):

    def input(self, sm, input_stream):
        if input_stream.keyboard.is_key_pressed(pygame.K_RETURN):
            sm.push(LevelSelectScene())
        if input_stream.keyboard.is_key_pressed(pygame.K_ESCAPE):
            sm.pop()
        if input_stream.keyboard.is_key_pressed(pygame.K_LCTRL):
            sm.push(ControlsScene())
        if input_stream.keyboard.is_key_pressed(pygame.K_h):
            sm.push(HelpScene())
            
    def draw(self, screen):
        screen.fill(BLACK)
        utils.draw_text_center(screen, 'Main menu', SCREEN_WIDTH/2, 100, WHITE)
        utils.draw_text_center(screen, 'First player to 50 points wins!', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60, WHITE)
        utils.draw_text_center(screen, 'ENTER to start the game', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 20, WHITE)
        utils.draw_text_center(screen, 'LEFT CONTROL for controls', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 10, WHITE)
        utils.draw_text_center(screen, 'H for help', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40, WHITE)
        utils.draw_text_center(screen, 'ESCAPE to exit the game', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 70, WHITE)

# i hope to use this someday \/

class LevelSelectScene(Scene):
    def input(self, sm, input_stream):
        if input_stream.keyboard.is_key_pressed(pygame.K_ESCAPE):
            sm.pop()
        if input_stream.keyboard.is_key_pressed(pygame.K_1):
            self.load_game(sm, 25)
        if input_stream.keyboard.is_key_pressed(pygame.K_2):
            self.load_game(sm, 50)

    def draw(self, screen):
        screen.fill(BLACK)
        utils.draw_text_center(screen, 'Level select. First to', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30, WHITE)
        utils.draw_text_center(screen, '1=25 points', SCREEN_WIDTH/2, SCREEN_HEIGHT/2, WHITE)
        utils.draw_text_center(screen, '2=50 points', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30, WHITE)
        utils.draw_text_center(screen, 'ESC=Quit', SCREEN_WIDTH/2, SCREEN_HEIGHT - 100, WHITE)

    def load_game(self, sm, win_score):
        utils.load_game()
        last_size_pickup = pygame.time.get_ticks()
        last_speed_pickup = pygame.time.get_ticks()
        last_coin_spawn = pygame.time.get_ticks()
        sm.push(GameScene(win_score, last_speed_pickup, last_size_pickup, last_coin_spawn))

class GameScene(Scene):
    def __init__(self, win_score, last_speed_pickup, last_size_pickup, last_coin_spawn):
        self.win_score = win_score
        self.last_speed_pickup = last_speed_pickup
        self.last_size_pickup = last_size_pickup
        self.last_coin_spawn = last_coin_spawn
    def input(self, sm, input_stream):
        # if input_stream.keyboard.is_key_pressed(pygame.K_ESCAPE):
        #     utils.unload_game()
        #     sm.pop()
        if input_stream.keyboard.is_key_pressed(pygame.K_p):
            sm.push(PauseScene())

    def update(self, sm):
        players[0].move_check()
        players[1].move_check()

        # check if anyone won
        if players[0].score >= self.win_score:
            players[0].overall_score += 1
            sm.push(GameOverScene())
        if players[1].score >= self.win_score:
            players[1].overall_score += 1
            sm.push(GameOverScene())
                
        for player in players:
            # check for coin collection
            for coin in coins:
                if coin.rect.colliderect(player.rect):
                    # coin.pickup_sound.play()
                    coin.delete()
                    player.score += 1
                    non_player_list[coin.rect.x//32][coin.rect.y//32] = False
                    # spawn another coin
                    utils.spawn_coin()
            # check for powerup collection
            for power_up in power_ups:
                if power_up.rect.colliderect(player.rect):
                    # power_up.pickup_sound.play()
                    power_up.delete()
                    non_player_list[power_up.rect.x//32][power_up.rect.y//32] = False
                    if power_up.type == 'speed':
                        self.last_speed_pickup = pygame.time.get_ticks()
                        if player.move_speed <= 4:
                            player.move_speed += 0.5
                    if power_up.type == 'size':
                        self.last_size_pickup = pygame.time.get_ticks()
                        if player.rect.width > 22:
                            player.rect.width -= 5
                            player.rect.height -= 5
        
        # check if any powerups can spawn
        speed = False
        size = False
        for power_up in power_ups:
            if power_up.type == 'speed':
                speed = True
            elif power_up.type == 'size':
                size = True
        
        if not speed and (pygame.time.get_ticks() - self.last_speed_pickup) / 1000 >= 8:
            utils.spawn_power_up('speed')
            
        if not size and (pygame.time.get_ticks() - self.last_size_pickup) / 1000 >= 8:
            utils.spawn_power_up('size')

        # check if enough time passed for a coin/coins to spawn
        if (pygame.time.get_ticks() - self.last_coin_spawn) / 1000 >= 10:
            if random.random() < ANOTHER_COIN_SPAWN_PROB:
                utils.spawn_coin()
            utils.spawn_coin()
            self.last_coin_spawn = pygame.time.get_ticks()




    def draw(self, screen):
        screen.fill(BLACK)
        # walls
        for wall in walls:
            pygame.draw.rect(screen, GREY, wall.rect)
        # coins
        for coin in coins:
            pygame.draw.rect(screen, YELLOW, coin.rect)
        # power ups
        for power_up in power_ups:
            if power_up.type == 'speed':
                pygame.draw.rect(screen, DARK_GREEN, power_up.rect)
            if power_up.type == 'size':
                pygame.draw.rect(screen, PINK, power_up.rect)
        # players
        for player in players:
            pygame.draw.rect(screen, player.color, player.rect)
        # score
        utils.draw_text(screen, "Player 1 score: " + str(players[0].score), 10, 5, RED)
        utils.draw_text(screen, "Player 2 score: " + str(players[1].score), 492, 5, BLUE)

class GameOverScene(Scene):
    def input(self, sm, input_stream):
        if input_stream.keyboard.is_key_pressed(pygame.K_ESCAPE):
            utils.unload_game()
            sm.set(MainMenuScene())

    def draw(self, screen):
        screen.fill(BLACK)
        if players[0].score > players[1].score:
            utils.draw_text_center(screen, "Player 1 wins!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 45, RED)
        else:
            utils.draw_text_center(screen, "Player 2 wins!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 45, BLUE)

        utils.draw_text_center(screen, f"Game score: {players[0].score} - {players[1].score}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 15, WHITE)
        utils.draw_text_center(screen, f"Overall score: {players[0].overall_score} - {players[1].overall_score}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 15, WHITE)
        utils.draw_text_center(screen, "ESC to exit to main menu", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 45, WHITE)

class ControlsScene(Scene):
    def input(self, sm, input_stream):
        if input_stream.keyboard.is_key_pressed(pygame.K_ESCAPE):
            sm.pop()
    def draw(self, screen):
        screen.fill(BLACK)
        utils.draw_text_center(screen, "Controls", SCREEN_WIDTH/2, 100, WHITE)
        utils.draw_text_center(screen, "Player 1:", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60, RED)
        utils.draw_text_center(screen, "WASD to move", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30, RED)
        utils.draw_text_center(screen, "Player 2:", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, BLUE)
        utils.draw_text_center(screen, "Arrow keys to move", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30, BLUE)
        utils.draw_text_center(screen, "ESC to return to main menu", SCREEN_WIDTH/2, SCREEN_HEIGHT - 100, WHITE)

class HelpScene(Scene):
    def input(self, sm, input_stream):
        if input_stream.keyboard.is_key_pressed(pygame.K_ESCAPE):
            sm.pop()
    def draw(self, screen):
        screen.fill(BLACK)
        utils.draw_text_center(screen, "Help", SCREEN_WIDTH/2, 100, WHITE)
        utils.draw_text_center(screen, "Collect coins to gain points, 1 coin = 1 point", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60, YELLOW)
        utils.draw_text_center(screen, "First player to 50 points wins the game", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30, WHITE)
        utils.draw_text_center(screen, "Pink powerup makes you smaller", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PINK)
        utils.draw_text_center(screen, "Green powerup makes you faster", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30, GREEN)
        utils.draw_text_center(screen, "ESC to return to main menu", SCREEN_WIDTH/2, SCREEN_HEIGHT - 100, WHITE)
    
class PauseScene(Scene):
    def input(self, sm, input_stream):
        if input_stream.keyboard.is_key_pressed(pygame.K_p):
            sm.pop()
        if input_stream.keyboard.is_key_pressed(pygame.K_ESCAPE):
            utils.unload_game()
            sm.set(MainMenuScene())
        
    
    def draw(self, screen):
        screen.fill(BLACK)
        utils.draw_text_center(screen, 'Paused', SCREEN_WIDTH/2, 100, WHITE)
        utils.draw_text_center(screen, f'Current score: {players[0].score} - {players[1].score}', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 45, WHITE)
        utils.draw_text_center(screen, 'P to unpause', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 15, WHITE)
        utils.draw_text_center(screen, 'ESC to return to main menu', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 15, WHITE)
        utils.draw_text_center(screen, 'ALT-F4 to exit the game', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 45, WHITE)

class SceneManager:
    def __init__(self):
        self.scenes = []
        # self.background_music = pygame.mixer.Sound('background_music.mp3')
        # self.background_music.set_volume(0.08)
        # self.play_music()

    def is_empty(self):
        return len(self.scenes) == 0

    def enter_scene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].on_enter()

    def exit_scene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].on_exit()

    def input(self, input_stream):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self, input_stream)

    def update(self):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self)

    def draw(self, screen):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(screen)
            
        pygame.display.flip()

    def push(self, scene):
        # exit current scene
        self.exit_scene()
        # enter new scene
        self.scenes.append(scene)
        self.enter_scene()

    def pop(self):
        # exit current scene
        self.exit_scene()
        self.scenes.pop()
        # enter new scene
        self.enter_scene()

    def set(self, scene):
        # pop all scenes
        while len(self.scenes) > 0:
            self.pop()
        # add selected scene
        self.push(scene)

    # def play_music(self):
    #     self.background_music.play(loops=-1)