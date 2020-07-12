import pygame
import game_config

class Player:
    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        print('player created')
        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.scale(self.image,(game_config.SCALE,game_config.SCALE))
        self.rect = pygame.Rect(self.position[0]*game_config.SCALE,self.position[1]*game_config.SCALE,game_config.SCALE,game_config.SCALE)

    def update(self):
        print('player updated')

    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]


    def render(self,screen,camera):
        self.rect = pygame.Rect(self.position[0]*game_config.SCALE,self.position[1]*game_config.SCALE- (camera[1]*game_config.SCALE),game_config.SCALE,game_config.SCALE)
        screen.blit(self.image, self.rect)

        #pygame.draw.rect(screen, game_config.WHITE,(self.position[0]*game_config.SCALE,self.position[1]*game_config.SCALE,game_config.SCALE,game_config.SCALE),4)
