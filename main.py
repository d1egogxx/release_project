import pygame
from settings import *


pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
light = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
light.fill((255, 220, 130))
light.set_alpha(25)

font = pygame.font.SysFont("georgia", 36, bold = True)


pygame.display.set_caption("")

clock = pygame.time.Clock()

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, x,y, w, h):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.smoothscale(self.image, (w,h) )
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
    def reset(self, screen):
        screen.blit(self.image, self.rect,)
        

class Player(GameSprite):
        
    def __init__(self, filename, x, y, w, h, speed):
        super().__init__(filename, x, y, w, h)
        self.speed = speed
        
        self.images = {
            "idle": pygame.image.load("player_stand.png")
        }
        
        self.state = "idle"
        
    def walking(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed
        
        if keys[pygame.K_LEFT] and self.rect.left > 250:
            self.rect.x -= self.speed


player = Player("player_stand.png", 260, 200, 140, 280, 2.5)
cabinet = pygame.Rect(750)

run = True

while run == True:
    
    clock.tick(FPS)
    
    screen.blit(background, (0,0))
    
    player.walking()
    player.reset(screen)
    
    task1 = font.render("Знайди ключ", True, (150, 0, 0))
    screen.blit(task1, (310, 30))
    
    screen.blit(light, (0,0))
    
    
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
            
pygame.quit()