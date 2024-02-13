import pygame
from sys import exit
from random import randint

def display_score():
    curr_time = pygame.time.get_ticks()//100 - start_time
    score_surf = test_font.render(f'{curr_time}', False, 'White')
    score_rect = score_surf.get_rect(midtop = (400, 0))
    screen.blit(score_surf, score_rect)

def obstacle_movement(obs_rect_list):
    if obs_rect_list:
        for obs_rect in obs_rect_list:
            obs_rect.x -= 6
            if obs_rect.bottom == 340: 
                screen.blit(cat_surf, obs_rect)
            else: 
                screen.blit(sqrl_surf, obs_rect)

        obs_rect_list = [obs for obs in obs_rect_list if obs.x > - 10]

    return obs_rect_list


pygame.init()

#create a screen
screen = pygame.display.set_mode((800, 400))

#set title
pygame.display.set_caption("Applesauce Run!")

#font
test_font = pygame.font.Font(None, 40)

#create a clock object 
clock = pygame.time.Clock()

game_active = False

start_time = 0

#test
sky_surf = pygame.image.load('graphics/sky.jpg').convert()
sky_surf = pygame.transform.scale(sky_surf, (800, 400))

road_surf = pygame.image.load('graphics/road.png').convert()
road_surf = pygame.transform.scale(road_surf, (800, 60))


#Obstacles 
cat_surf = pygame.image.load('graphics/Cat.png').convert_alpha()
cat_surf = pygame.transform.scale(cat_surf, (60, 40))
cat_rect = cat_surf.get_rect(midbottom = (800, 340))
sqrl_surf = pygame.image.load('graphics/SQRL_1.png').convert_alpha()
sqrl_surf = pygame.transform.scale_by(sqrl_surf, 2)

obstacle_rect_list = []

player_surf = pygame.image.load('graphics/Jason/no_anim_0.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (60, 80))
player_rect = player_surf.get_rect(midbottom = (100, 340))
player_grav = 0

#Intro Screen 
player_stand = pygame.image.load('graphics/Jason/no_anim_0.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (100, 130))
player_stand_rect = player_stand.get_rect(center = (400, 200))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


while True: 
    #everything here
    for event in pygame.event.get():

        #account for closing window 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active: 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if player_rect.bottom == 340:
                    player_grav = -18

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and player_rect.bottom == 340: 
                    player_grav = -18
        else: 
            if event.type == pygame.KEYDOWN: 
                    start_time = pygame.time.get_ticks()//100
                    game_active = True
        
        if event.type == obstacle_timer and game_active:
            if randint(0, 2): 
                obstacle_rect_list.append(cat_surf.get_rect(midbottom = (randint(800, 1200), 340)))
            else: 
                obstacle_rect_list.append(sqrl_surf.get_rect(midbottom = (randint(800, 1200), 260)))


    if game_active: 
        #background
        screen.blit(sky_surf, (0,0))
        screen.blit(road_surf, (0,340))
        display_score()


        #Cat
        # cat_rect.left -= 6
        # if cat_rect.right < -10: cat_rect.left = 800
        # screen.blit(cat_surf, cat_rect)

        #Player
        player_grav += 0.8
        player_rect.y += player_grav
        if player_rect.bottom >= 340: player_rect.bottom = 340
        screen.blit(player_surf, player_rect)

        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #check collision 
        for obs in obstacle_rect_list: 
            if player_rect.colliderect(obs): 
                obstacle_rect_list = []
                game_active = False
    else: 
        screen.fill((47, 186, 162))
        screen.blit(player_stand, player_stand_rect)

    #update everything
    pygame.display.update()
    #set the ceiling to 60fps
    clock.tick(60)
