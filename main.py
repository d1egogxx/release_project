import pygame
from settings import *


pygame.init()

screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)

pygame.display.set_caption("")

clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, x,y, w, h):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (w,h) )
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
    def reset(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    pass



run = True

while run == True:
    
    clock.tick(FPS)
    
    
    
    
    
    
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()