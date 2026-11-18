import pygame
from settings import *


pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
light = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
light.fill((255, 220, 130))
light.set_alpha(25)

font = pygame.font.SysFont("georgia", 36, bold = True)
hint_font = pygame.font.SysFont("georgia", 23, bold = True)

pygame.display.set_caption("")

clock = pygame.time.Clock()

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

background_2 = pygame.image.load("background_2.jpg")
background_2 = pygame.transform.scale(background_2, (WINDOW_WIDTH, WINDOW_HEIGHT))


key = pygame.image.load("key.png")
key = pygame.transform.scale(key, (200, 200))

code = pygame.image.load("code.png")
code = pygame.transform.scale(code, (200, 200))

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
            "idle": pygame.image.load("player_stand.png"),
            "walking_right" : pygame.image.load("player_walking_right.png"),
            "walking_left" : pygame.image.load("player_walking_left.png")
        }
        
        for state in self.images:
            self.images[state] = pygame.transform.smoothscale(self.images[state], (w,h))
        
        self.state = "idle"
        
    def walking(self, door_open):
        keys = pygame.key.get_pressed()
        
        if door_open:
            left_limit = 70
            right_limit = WINDOW_WIDTH - 70
        else:
            left_limit = 250
            right_limit = WINDOW_WIDTH
        
        if keys[pygame.K_RIGHT] and self.rect.right < right_limit:
            self.rect.x += self.speed
            self.image = self.images["walking_right"]
        
        elif keys[pygame.K_LEFT] and self.rect.left > left_limit:
            self.rect.x -= self.speed
            self.image = self.images["walking_left"]
            
        else:
            self.image = self.images["idle"]


player = Player("player_stand.png", 260, 200, 140, 280, 2.5)
cabinet = pygame.Rect(735, 185, 70, 90)
door = pygame.Rect(860, 190, 138, 160)
table = pygame.Rect(400, 270, 200, 180)


task = "Знайди ключ" 
hint = ""
door_open = False
run = True
key_found = False



while run == True:
    
    clock.tick(FPS)
    
    if door_open == True:
        screen.blit(background_2, (0,0))  
        task = "Знайди вихід" 
        hint = " "
        if touching_table:
            hint = "Натисни Е щоб взаємодіяти"
            if keys[pygame.K_e]:
                screen.blit(code, (300, 150))
        
    else:
        screen.blit(background, (0,0))
        
    screen.blit(light, (0,0))
    
    
    

    
    player.walking(door_open)
    
    keys = pygame.key.get_pressed()
    touching_cabinet = player.rect.colliderect(cabinet)
    touching_door = player.rect.colliderect(door)
    touching_table = player.rect.colliderect(table)
    
    if touching_door and door_open == False:
        if key_found:
            hint = "Натисни Е щоб відкрити двері"
            
            if keys[pygame.K_e]:
                door_open = True
        else: 
            hint = "Спочатку знайди ключ"
    
    if touching_cabinet and key_found == False and door_open == False:
        hint = "Натисни Е щоб взаємодіяти"
        
        if keys[pygame.K_e] and touching_cabinet and key_found == False:
            key_found = True
            task = "Відкрий двері"   
             
    if key_found == True and door_open == False:
        screen.blit(key, (350, 140))
        
        
        
    task_text = font.render(task, True, (150, 0, 0))
    hint_text = hint_font.render(hint, True, (150, 0, 0))
    
    screen.blit(task_text, (310, 30))
    screen.blit(hint_text, (300, 100))
        
    
    player.reset(screen)
    
        
    
    
    
    
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
            
pygame.quit()