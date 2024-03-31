import pygame
import random

# Size of the screen
game_width = 400
game_height = 100

class Pokemon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # walking animation
        pkmn_walk1 = pygame.image.load('cyndaquil/walk1.png').convert_alpha()
        pkmn_walk2 = pygame.image.load('cyndaquil/walkoff2.png').convert_alpha()
        pkmn_walk3 = pygame.image.load('cyndaquil/walk3.png').convert_alpha()
        pkmn_walk4 = pygame.image.load('cyndaquil/walkoff4.png').convert_alpha()
        pkmn_walk5 = pygame.image.load('cyndaquil/walk5.png').convert_alpha()
        pkmn_walk6 = pygame.image.load('cyndaquil/walkoff6.png').convert_alpha()
        self.pkmn_walk = [pkmn_walk1, pkmn_walk2, pkmn_walk3, pkmn_walk4, pkmn_walk5, pkmn_walk6]      

        # flipped animation
        pkmn_walk1_f = pygame.image.load('cyndaquil/walk1-f.png').convert_alpha()
        pkmn_walk2_f = pygame.image.load('cyndaquil/walk2-f.png').convert_alpha()
        pkmn_walk3_f = pygame.image.load('cyndaquil/walk3-f.png').convert_alpha()
        pkmn_walk4_f = pygame.image.load('cyndaquil/walk4-f.png').convert_alpha()
        pkmn_walk5_f = pygame.image.load('cyndaquil/walk5-f.png').convert_alpha()
        pkmn_walk6_f = pygame.image.load('cyndaquil/walk6-f.png').convert_alpha()
        self.pkmn_walk_flipped = [pkmn_walk1_f, pkmn_walk2_f, pkmn_walk3_f, pkmn_walk4_f, pkmn_walk5_f, pkmn_walk6_f]

        # idle animation
        pkmn_idle1 = pygame.image.load('cyndaquil/idle1.png').convert_alpha()
        pkmn_idle2 = pygame.image.load('cyndaquil/idle2.png').convert_alpha()
        pkmn_idle3 = pygame.image.load('cyndaquil/idle3.png').convert_alpha()
        pkmn_idle4 = pygame.image.load('cyndaquil/idle4.png').convert_alpha()
        pkmn_idle5 = pygame.image.load('cyndaquil/idle5.png').convert_alpha()
        pkmn_idle6 = pygame.image.load('cyndaquil/idle6.png').convert_alpha()
        self.pkmn_idle = [pkmn_idle1, pkmn_idle2, pkmn_idle3, pkmn_idle4, pkmn_idle5, pkmn_idle6]

        self.pkmn_index = 0
        self.image = self.pkmn_walk[self.pkmn_index]
        self.rect = self.image.get_rect(midbottom = (0, 100))
        self.speed = random.randint(45, 130)
        self.is_walking = False     
        self.pos = pygame.math.Vector2(self.rect.midbottom)
        self.direction = pygame.math.Vector2(1, 0)

        # Variables for animations and movement
        self.walking_distance = random.randint(20, 120)
        self.distance_walked = 0

    def update(self, dt):
        self.move_sprite(dt)
        self.animation_state()
        # self.idle_sprite()
        # self.is_walking()

    def idle_sprite(self):
        self.pkmn_index += 0.001

        if self.pkmn_index >= len(self.pkmn_idle):
            self.pkmn_index = 0

        self.image = self.pkmn_idle[int(self.pkmn_index)]

    def animation_state(self):
        # Walking animation
        self.pkmn_index += 0.001

        if self.pkmn_index >= len(self.pkmn_walk):
            self.pkmn_index = 0

        if self.direction.x < 0:
            self.image = self.pkmn_walk[int(self.pkmn_index)]  # Convert pkmn_index to an integer
        else:
            self.image = self.pkmn_walk_flipped[int(self.pkmn_index)]  # Convert pkmn_index to an integer

    def move_sprite(self, dt):
        # # Movement logic
        # self.rect += speed
        # distance_walked += 1  # Update distance walked (only magnitude considered)

        # # Boundary check
        if self.rect.right >= game_width:
            self.direction.x = -1
        elif self.rect.left <= 0:
            self.direction.x = 1

        self.pos += self.direction * self.speed * dt
        self.rect.midbottom = self.pos

    def is_walking(self):
        for sprite in self.pkmn_walk:
            if self.image == sprite:
                is_walking = True
                return True
        is_walking = False
        return False
        

    
        