import pygame

pygame.init()

screen_h = 400
screen_w = 500
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Calculator")

def display():
    start = True
    
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
    pygame.display.update()
    
display()