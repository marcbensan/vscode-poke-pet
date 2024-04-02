import pygame

pygame.init()
screen = pygame.display.set_mode((400, 150))
pygame.display.set_caption("Poke Pet")

# # walking animation
# pkmn_walk1 = pygame.image.load('cyndaquil/walk1.png').convert_alpha()
# pkmn_walk2 = pygame.image.load('cyndaquil/walkoff2.png').convert_alpha()
# pkmn_walk3 = pygame.image.load('cyndaquil/walk3.png').convert_alpha()
# pkmn_walk4 = pygame.image.load('cyndaquil/walkoff4.png').convert_alpha()
# pkmn_walk5 = pygame.image.load('cyndaquil/walk5.png').convert_alpha()
# pkmn_walk6 = pygame.image.load('cyndaquil/walkoff6.png').convert_alpha()
# pkmn_walk = [pkmn_walk1, pkmn_walk2, pkmn_walk3, pkmn_walk4, pkmn_walk5, pkmn_walk6]

# # flipped animation
# pkmn_walk1_f = pygame.image.load('cyndaquil/walk1-f.png').convert_alpha()
# pkmn_walk2_f = pygame.image.load('cyndaquil/walk2-f.png').convert_alpha()
# pkmn_walk3_f = pygame.image.load('cyndaquil/walk3-f.png').convert_alpha()
# pkmn_walk4_f = pygame.image.load('cyndaquil/walk4-f.png').convert_alpha()
# pkmn_walk5_f = pygame.image.load('cyndaquil/walk5-f.png').convert_alpha()
# pkmn_walk6_f = pygame.image.load('cyndaquil/walk6-f.png').convert_alpha()
# pkmn_walk_flipped = [pkmn_walk1_f, pkmn_walk2_f, pkmn_walk3_f, pkmn_walk4_f, pkmn_walk5_f, pkmn_walk6_f]

# # idle animation
# pkmn_idle1 = pygame.image.load('cyndaquil/idle1.png').convert_alpha()
# pkmn_idle2 = pygame.image.load('cyndaquil/idle2.png').convert_alpha()
# pkmn_idle3 = pygame.image.load('cyndaquil/idle3.png').convert_alpha()
# pkmn_idle4 = pygame.image.load('cyndaquil/idle4.png').convert_alpha()
# pkmn_idle5 = pygame.image.load('cyndaquil/idle5.png').convert_alpha()
# pkmn_idle6 = pygame.image.load('cyndaquil/idle6.png').convert_alpha()
# pkmn_idle = [pkmn_idle1, pkmn_idle2, pkmn_idle3, pkmn_idle4, pkmn_idle5, pkmn_idle6]