import pygame
from sys import exit

def pkmn_animation():
    # walking animation
    global pkmn_surface, pkmn_index, speed
    pkmn_index += 0.1
    if pkmn_index >= len(pkmn_walk):
        pkmn_index = 0
    if speed < 0:
        pkmn_surface = pkmn_walk[int(pkmn_index)]
    else:
        pkmn_surface = pkmn_walk_flipped[int(pkmn_index)]

pygame.init()
screen = pygame.display.set_mode((400, 150))
pygame.display.set_caption("Poke Pet")
clock = pygame.time.Clock()

# size of the screen
game_width = 400
game_height = 100

bg_surface = pygame.Surface((game_width, game_height)).convert()
bg_surface.fill('white')
platform_surface = pygame.Surface((400, 5)).convert()
platform_surface.fill('Green')



# walking animation
pkmn_walk1 = pygame.image.load('cyndaquil/walk1.png').convert_alpha()
pkmn_walk2 = pygame.image.load('cyndaquil/walkoff2.png').convert_alpha()
pkmn_walk3 = pygame.image.load('cyndaquil/walk3.png').convert_alpha()
pkmn_walk4 = pygame.image.load('cyndaquil/walkoff4.png').convert_alpha()
pkmn_walk5 = pygame.image.load('cyndaquil/walk5.png').convert_alpha()
pkmn_walk6 = pygame.image.load('cyndaquil/walkoff6.png').convert_alpha()
pkmn_walk = [pkmn_walk1, pkmn_walk2, pkmn_walk3, pkmn_walk4, pkmn_walk5, pkmn_walk6]

# flipped animation
pkmn_walk1_f = pygame.image.load('cyndaquil/walk1-f.png').convert_alpha()
pkmn_walk2_f = pygame.image.load('cyndaquil/walk2-f.png').convert_alpha()
pkmn_walk3_f = pygame.image.load('cyndaquil/walk3-f.png').convert_alpha()
pkmn_walk4_f = pygame.image.load('cyndaquil/walk4-f.png').convert_alpha()
pkmn_walk5_f = pygame.image.load('cyndaquil/walk5-f.png').convert_alpha()
pkmn_walk6_f = pygame.image.load('cyndaquil/walk6-f.png').convert_alpha()
pkmn_walk_flipped = [pkmn_walk1_f, pkmn_walk2_f, pkmn_walk3_f, pkmn_walk4_f, pkmn_walk5_f, pkmn_walk6_f]


pkmn_index = 0
pkmn_surface = pkmn_walk[pkmn_index]
pkmn_rect = pkmn_surface.get_rect(midbottom = (0, 100))

speed = 1.5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface, (0,0))
    screen.blit(platform_surface, (0,100))

   

    # if the sprite is moving right
    
    pkmn_rect.x += speed
   
    # setting boundaries
    if pkmn_rect.right >= game_width:
        pkmn_rect.x -= 1
        speed = -1.5
    elif pkmn_rect.left <= 0:
        pkmn_rect.x += 1
        speed = 1.4
 
    # run animation
    pkmn_animation()

    screen.blit(pkmn_surface, pkmn_rect)

    pygame.display.update()
    clock.tick(60)
