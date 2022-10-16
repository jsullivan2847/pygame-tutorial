import pygame
from sys import exit

# just changing file for github push
# once again...
# and again....

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def display_game_over():
    snail_rect.left = 800
    screen.fill((94,129,162))
    restart_text = test_font.render('Press the space bar to restart', False, (64,64,64))
    restart_rect = restart_text.get_rect(center = (400,360))

    score_text = test_font.render(f'your score: {score}', False, (64,64,64))
    score_rect = score_text.get_rect(center = (400, 50))

    screen.blit(player_stand,player_stand_rect)
    screen.blit(restart_text, restart_rect)
    screen.blit(score_text, score_rect)
    


# renders game window
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

#ground and sky
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score
# score_surf = test_font.render('My Game', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

# snail
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

fly_surf = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly_rect = fly_surf.get_rect(bottomright=(600,200))


# player
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
gravity = 0
player_gravity = 0

#static player image for game over 
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (200, 200))
player_stand_rect = player_stand.get_rect(center=(400,200))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

# starts a function sort of like update() in unity
while True: 
    # allows to quit
    for event in pygame.event.get():
        # allows user to quit

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and isGrounded:
                    player_gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)
        if event.type == obstacle_timer and game_active:
            print('test')

    pygame.display.update()
    # keeps it at 60 frames per second
    clock.tick(60)

    # renders images in game window
    if game_active:

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        # snail movement
        snail_rect.x -= 4
        if(snail_rect.right <= 0):
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        if player_rect.bottom < 300:
            isGrounded = False
        else:
            isGrounded = True
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        display_game_over(); 

