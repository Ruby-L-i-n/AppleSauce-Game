import pygame
from sys import exit

pygame.init()

#create a screen
screen = pygame.display.set_mode((800, 400))

#set title
pygame.display.set_caption("Applesauce Run!")

#create a clock object 
clock = pygame.time.Clock()

#test
sky_surface = pygame.image.load('graphics/sky.jpg')
sky_surface = pygame.transform.scale(sky_surface, (800, 400))

road_surface = pygame.image.load('graphics/road.png')
road_surface = pygame.transform.scale(road_surface, (800, 60))


while True: 
    #everything here
    for event in pygame.event.get():

        #account for closing window 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(road_surface, (0,340))

    #update everything
    pygame.display.update()
    #set the ceiling to 60fps
    clock.tick(60)
