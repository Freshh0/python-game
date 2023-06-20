import pygame
import utils
from globals import *


class Scene():
    def __init__(self):
        pass
    def on_enter(self):
        pass
    def on_exit(self):
        pass
    def input(self, sm):
        pass
    def update(self, sm):
        pass
    def draw(self, screen):
        pass


class MainMenuScene(Scene):
    def input(self, sm):
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            utils.load_game()
            sm.push(GameScene())
        if key[pygame.K_TAB]:
            sm.pop()
            
    def draw(self, screen):
        screen.fill(BLACK)
        utils.draw_text_center(screen, 'Main menu', SCREEN_WIDTH/2, 100, WHITE)
        utils.draw_text_center(screen, 'First player to 50 points wins!', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30, WHITE)
        utils.draw_text_center(screen, 'ENTER to start the game', SCREEN_WIDTH/2, SCREEN_HEIGHT/2, WHITE)
        utils.draw_text_center(screen, 'TAB to exit the game', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30, WHITE)

# i hope to use this someday \/

# class LevelSelectScene(Scene):
#     def input(self, sm):
#         key = pygame.key.get_pressed()
#         if key[pygame.K_ESCAPE]:
#             sm.pop()
#         if key[pygame.K_1]:
#             sm.push(GameScene())
#         if key[pygame.K_2]:
#             sm.push(GameScene())
#     def update(self, sm):
#         pass
#     def draw(self, sm, screen):
#         screen.fill(BLACK)
#         utils.draw_text(screen, 'Level select. First to', 100, 100, WHITE)
#         utils.draw_text(screen, '1=25 points 2=50 points', 100, 130, WHITE)
#         utils.draw_text(screen, 'ESC=Quit', 100, 160, WHITE)

class GameScene(Scene):
    def input(self, sm):
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            utils.unload_game()
            sm.pop()

    def update(self, sm):
        players[0].move_check()
        players[1].move_check()

        # check if anyone won
        if players[0].score >= WIN_SCORE:
            players[0].overall_score += 1
            sm.push(GameOverScene())
        if players[1].score >= WIN_SCORE:
            players[1].overall_score += 1
            sm.push(GameOverScene())
                
        for player in players:
            # check for coin collection
            for coin in coins:
                if coin.rect.colliderect(player.rect):
                    coins.remove(coin)
                    player.score += 1
                    non_player_list[coin.rect.x//32][coin.rect.y//32] = False
                    # spawn another coin
                    utils.spawn_coin()

    def draw(self, screen):
        screen.fill(BLACK)
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
        utils.draw_text(screen, "Player 1 score: " + str(players[0].score), 10, 5, RED)
        utils.draw_text(screen, "Player 2 score: " + str(players[1].score), 492, 5, BLUE)

class GameOverScene(Scene):
    def input(self, sm):
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            utils.unload_game()
            sm.set(MainMenuScene())

    def draw(self, screen):
        screen.fill(BLACK)
        if players[0].score > players[1].score:
            utils.draw_text_center(screen, "Player 1 wins!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30, WHITE)
            utils.draw_text_center(screen, f"Overall score: {players[0].overall_score} - {players[1].overall_score}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, WHITE)
            utils.draw_text_center(screen, "Press ESC to exit to main menu", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30, WHITE)
        else:
            utils.draw_text_center(screen, "Player 2 wins!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30, WHITE)
            utils.draw_text_center(screen, f"Overall score: {players[0].overall_score} - {players[1].overall_score}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, WHITE)
            utils.draw_text_center(screen, "Press ESC to exit to main menu", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30, WHITE)


class SceneManager:
    def __init__(self):
        self.scenes = []

    def is_empty(self):
        return len(self.scenes) == 0

    def enter_scene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].on_enter()

    def exit_scene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].on_exit()

    def input(self):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self)

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