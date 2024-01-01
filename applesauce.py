import pygame
from sys import exit

pygame.init()

#create a screen
screen = pygame.display.set_mode((800, 400))

#set title
pygame.display.set_caption("Applesauce Run!")

#font
test_font = pygame.font.Font('fonts/SadMorningDemoRegular.ttf', 50)

#create a clock object 
clock = pygame.time.Clock()

#test
sky_surface = pygame.image.load('graphics/sky.jpg').convert()
sky_surface = pygame.transform.scale(sky_surface, (800, 400))

road_surface = pygame.image.load('graphics/road.png').convert()
road_surface = pygame.transform.scale(road_surface, (800, 60))

text_surface = test_font.render('Applesauce Run', False, 'White')

cat_surface = pygame.image.load('graphics/Cat.png').convert_alpha()
cat_surface = pygame.transform.scale(cat_surface, (80, 60))
cat_rect = cat_surface.get_rect(midbottom = (800, 340))

player_surface = pygame.image.load('graphics/Jason/no_anim_0.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (60, 80))
player_rect = player_surface.get_rect(midbottom = (100, 340))

while True: 
    #everything here
    for event in pygame.event.get():

        #account for closing window 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(road_surface, (0,340))
    screen.blit(text_surface, (250,50))

    cat_rect.left -= 4
    if cat_rect.right < -10: cat_rect.left = 800
    screen.blit(cat_surface, cat_rect)
    screen.blit(player_surface, player_rect)

    if player_rect.colliderect(cat_rect) : 
        print("ahh")
        cat_rect.left = 800

    #update everything
    pygame.display.update()
    #set the ceiling to 60fps
    clock.tick(60)