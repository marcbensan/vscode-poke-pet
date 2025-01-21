import pygame
import sys
import random

from scripts.pokemon import Pokemon
from scripts.const import *
from scripts.utils import load_img



class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), flags=pygame.RESIZABLE)
        pygame.display.set_caption("Poke Pet")
        self.clock = pygame.time.Clock()
       
        self.bg_surface = load_img(IMG_PATH + 'backgrounds/bg.png')
        self.bg_surface = pygame.transform.scale(self.bg_surface, (GAME_WIDTH, GAME_HEIGHT))


    
    def run(self):
    # Game loop
        while True:
            
            self.screen.blit(self.bg_surface, (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pokemon_instance.current_state == "sleep" and pokemon_instance.rect.collidepoint(event.pos):
                        # Change state to yawn
                        pokemon_instance.current_state = "yawn"    
                        pokemon_instance.idle_time = random.randint(10, 25)
                        pokemon_instance.idle_timer = 0             

                # if event.type == pygame.VIDEORESIZE:
                #     # Update the game width
                #     game_width, game_height = event.w, event.h
                #     screen = pygame.display.set_mode((game_width, game_height), pygame.RESIZABLE)
                #     pokemon_instance.resize_screen(game_width, game_height)
                
            
            self.clock.tick(FPS)
            pygame.display.update()

                

pokemon = pygame.sprite.GroupSingle()
pokemon_instance = Pokemon()
pokemon.add(pokemon_instance)



    
    
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

