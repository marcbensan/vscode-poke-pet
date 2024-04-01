import pygame
import random
from sys import exit
from sprites.cyndaquil_sprites import pkmn_walk, pkmn_walk_flipped, pkmn_idle
from classes.pokemon import Pokemon

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

pokemon = pygame.sprite.GroupSingle()
pokemon_instance = Pokemon()
pokemon.add(pokemon_instance)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface, (0, 0))
    screen.blit(platform_surface, (0, 100))
    
    #clock tick
    dt = clock.tick(60)
  
    # Run animation
    # Pokemon.animation_state(pokemon_instance)

    # Move the sprite if it's in the walking animation
    if pokemon_instance.check_walk():
        if pokemon_instance.distance_walked < pokemon_instance.walking_distance:
            pokemon_instance.animation_state("walk")
            pokemon_instance.move_sprite()
        else:
            distance_walked = 0

    screen.blit(pokemon_instance.image, pokemon_instance.rect)
    pokemon.draw(screen)
    pokemon.update()

    pygame.display.update()
