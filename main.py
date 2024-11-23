import pygame

pygame.init()

display_w = 300
display_h = 400
icon = pygame.image.load("icon.png")
display = pygame.display.set_mode((display_w, display_h))

pygame.display.set_caption("Calculator")
pygame.display.set_icon(icon)


def menu():
    start = True
    
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                        
        display.fill("white")
        pygame.draw.line(display, "#00000000", (0, 150), (300, 150), 3)
    
        pygame.display.update()

    
menu()