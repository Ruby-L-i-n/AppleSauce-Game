import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
while True: 
    #everything here

    for event in pygame.event.get():
        #close window 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            

    pygame.display.update()