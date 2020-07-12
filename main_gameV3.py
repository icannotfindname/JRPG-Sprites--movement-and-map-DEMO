import pygame
import game_config
from game import Game
from game_state import GameState

pygame.init()

screen = pygame.display.set_mode((game_config.SCREEN_WIDTH,game_config.SCREEN_HEIGHT))
pygame.display.set_caption('Kirpeos "The Game"')
#framerate
clock = pygame.time.Clock()
game = Game(screen)
game.set_up()

#Game Loop
while game.game_state == GameState.RUNNING:
    clock.tick(50)
    game.update()
    #screen.fill(game_config.BLACK)
    pygame.display.flip()
