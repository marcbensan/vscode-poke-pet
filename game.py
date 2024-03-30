import pygame
import random
from sys import exit
from sprites.cyndaquil_sprites import pkmn_walk, pkmn_walk_flipped, pkmn_idle

def pkmn_animation():
    # walking animation
    global pkmn_surface, pkmn_index, speed
    pkmn_index += 0.1

    if pkmn_surface in pkmn_walk:
        if pkmn_index >= len(pkmn_walk): # reset the array
            pkmn_index = 0
        if speed < 0:
            pkmn_surface = pkmn_walk[int(pkmn_index)]
        else:
            pkmn_surface = pkmn_walk_flipped[int(pkmn_index)]

    if pkmn_surface in pkmn_idle:
        if pkmn_index >= len(pkmn_idle):
            pkmn_index = 0
        if speed < 0:
            pkmn_surface = pkmn_idle[int(pkmn_index)]

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

# variables for animations
pkmn_index = 0
distance_walked = 0
walking_distance = random.randint(0, 50)
speed = 1.5

pkmn_anims = {
    0 : pkmn_walk[pkmn_index],
    1: pkmn_idle[pkmn_index]
}

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface, (0,0))
    screen.blit(platform_surface, (0,100))

    pkmn_surface = pkmn_anims[random.randint(0,1)] # idle or walk
    pkmn_rect = pkmn_surface.get_rect(midbottom = (0, 100))

    # if the sprite is moving right  
    if pkmn_surface in pkmn_walk:
        pkmn_rect.x += speed

    # setting boundaries
    if pkmn_rect.right >= game_width:
        pkmn_rect.x -= 1.5 
        speed = -1.5
    elif pkmn_rect.left <= 0:
        pkmn_rect.x += 1.5 
        speed = 1.4
 
    # animation
    pkmn_animation()

    screen.blit(pkmn_surface, pkmn_rect)

    pygame.display.update()
    clock.tick(80)
