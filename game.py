import pygame
import random
from sys import exit
from classes.pokemon import Pokemon

# Initialize pygame
pygame.init()

# Size of the screen
game_width = 600
game_height = 300

# Set up the display
screen = pygame.display.set_mode((game_width, game_height), pygame.RESIZABLE)
pygame.display.set_caption("Poke Pet")
clock = pygame.time.Clock()

# Create background and platform surfaces
bg_surface = pygame.image.load('backgrounds/bg.png')
bg_surface = pygame.transform.scale(bg_surface, (game_width, game_height))
pokemon = pygame.sprite.GroupSingle()
pokemon_instance = Pokemon()
pokemon.add(pokemon_instance)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pokemon_instance.current_state == "sleep" and pokemon_instance.rect.collidepoint(event.pos):
                # Change state to yawn
                pokemon_instance.current_state = "yawn"    
                pokemon_instance.idle_time = random.randint(10, 25)
                pokemon_instance.idle_timer = 0             

        if event.type == pygame.VIDEORESIZE:
            # Update the game width
            game_width, game_height = event.w, event.h
            screen = pygame.display.set_mode((game_width, game_height), pygame.RESIZABLE)
            pokemon_instance.resize_screen(game_width, game_height)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface, (0, 0))
    
    #clock tick
    if pokemon_instance.current_state == "sleep":
        clock.tick(30)
    clock.tick(60)
  
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
