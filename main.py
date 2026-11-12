import pygame

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
FPS = 60

pygame.init()

screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)

pygame.display.set_caption("")

clock = pygame.time.Clock()




run = True

while run == True:
    
    clock.tick(FPS)
    
    
    
    
    
    
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()