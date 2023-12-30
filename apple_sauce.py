import pygame
from sys import exit

pygame.init()

#create a screen
screen = pygame.display.set_mode((800, 400))

#set title
pygame.display.set_caption("Applesauce Run!")

#create a clock object 
clock = pygame.time.Clock()

while True: 
    #everything here
    for event in pygame.event.get():

        #account for closing window 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    #update everything
    pygame.display.update()
    #set the ceiling to 60fps
    clock.tick(60)
