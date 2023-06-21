import pygame
import os
from globals import *
import scene_engine
import input_stream
    

pygame.init()

# screen setup
os.environ["SDL_VIDEO_CENTERED"] = "1"
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Race to 50")


clock = pygame.time.Clock()

# setup scene manager
scene_manager = scene_engine.SceneManager()
main_menu = scene_engine.MainMenuScene()
# push first scene to stack
scene_manager.push(main_menu)

# setup input stream
input_str = input_stream.InputStream()

# game loop
running = True
while running:

    # set FPS to 60
    clock.tick(60)

    input_str.process_input()

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # check for inputs, update values and draw sprites
    if scene_manager.is_empty():
        running = False
    scene_manager.input(input_str)
    scene_manager.update()
    scene_manager.draw(screen)


pygame.quit()
