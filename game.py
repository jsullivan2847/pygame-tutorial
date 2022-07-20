import pygame
from sys import exit


#renders game window
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#ground and sky
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score
score_surf = test_font.render('My Game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

#snail
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))


#player
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
gravity = 0
player_gravity = 0 

#starts a function sort of like update() in unity
while True:
    #allows to quit
    for event in pygame.event.get():
        #allows user to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

        if event.type == pygame.KEYUP:
            print('keyup')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

        #checks for mouse collision with player object
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')
    pygame.display.update()
    #keeps it at 60 frames per second
    clock.tick(60)
    #renders images in game window
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300)) 
    screen.blit(score_surf,score_rect) 
 

    #snail movement
    snail_rect.x -= 4
    if(snail_rect.right <= 0): snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)

    # player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surf, player_rect)

    #keyboardinput
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')


    
    
