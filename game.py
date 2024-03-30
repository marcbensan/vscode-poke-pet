import pygame
import random
from sys import exit
from sprites.cyndaquil_sprites import pkmn_walk, pkmn_walk_flipped, pkmn_idle

def pkmn_animation():
    # Walking animation
    global pkmn_surface, pkmn_index, speed
    pkmn_index += 0.1

    if pkmn_index >= len(pkmn_walk):
        pkmn_index = 0

    if speed < 0:
        pkmn_surface = pkmn_walk[int(pkmn_index)]  # Convert pkmn_index to an integer
    else:
        pkmn_surface = pkmn_walk_flipped[int(pkmn_index)]  # Convert pkmn_index to an integer

def move_sprite():
    global walking_distance, distance_walked, pkmn_rect, speed

    # Movement logic
    pkmn_rect.x += speed
    distance_walked += speed  # Update distance walked (only magnitude considered)

    # Boundary check
    if pkmn_rect.right >= game_width:
        pkmn_rect.x -= 1
        speed = -1
    elif pkmn_rect.left <= 0:
        pkmn_rect.x += 1
        speed = 1

        

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 150))
pygame.display.set_caption("Poke Pet")
clock = pygame.time.Clock()

# Size of the screen
game_width = 400
game_height = 100

# Create background and platform surfaces
bg_surface = pygame.Surface((game_width, game_height)).convert()
bg_surface.fill('white')
platform_surface = pygame.Surface((400, 5)).convert()
platform_surface.fill('Green')

# Variables for animations and movement
pkmn_index = 0
speed = 1
walking_distance = random.randint(20, 120)
distance_walked = 0
is_walking = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface, (0, 0))
    screen.blit(platform_surface, (0, 100))

    pkmn_surface = pkmn_walk[int(pkmn_index)]  # Set default surface to walking animation
    pkmn_rect = pkmn_surface.get_rect(midbottom=(0, 100))

    for sprite in pkmn_walk:
        if pkmn_surface == sprite:
            is_walking = True
            break

    # Run animation
    pkmn_animation()

    # Move the sprite if it's in the walking animation
    if is_walking:
        while distance_walked < walking_distance:
            move_sprite()
        distance_walked = 0
            

    screen.blit(pkmn_surface, pkmn_rect)

    pygame.display.update()
    clock.tick(80)
