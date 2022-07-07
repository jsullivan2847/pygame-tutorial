import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#ground and sky
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game', False, 'Green')

#snail
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))


#player
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

#starts a function sort of like update() in unity

while True:
    #allows to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)


    #places images on screen
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300)) 
    screen.blit(text_surface, (300,50)) 
    screen.blit(player_surf, player_rect)
    screen.blit(snail_surf, snail_rect)

    #snail movement
    snail_rect.x -= 4
    if(snail_rect.right <= 0): snail_rect.left = 800

    #collision
    if(player_rect.colliderect(snail_rect)):
        print('collision')
