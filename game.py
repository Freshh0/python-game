import pygame
import os
from globals import *
import scene_engine
    

pygame.init()

# screen setup
os.environ["SDL_VIDEO_CENTERED"] = "1"
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game")


clock = pygame.time.Clock()

# setup scene manager
scene_manager = scene_engine.SceneManager()
main_menu = scene_engine.MainMenuScene()
# push first scene to stack
scene_manager.push(main_menu)


# game loop
running = True
while running:

    # set FPS to 60
    clock.tick(60)

    # check for inputs, update values and draw sprites
    if scene_manager.is_empty():
        running = False
    scene_manager.input()
    scene_manager.update()
    scene_manager.draw(screen)

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
