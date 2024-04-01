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
        self.rect = self.image.get_rect(midbottom = (random.randint(30, 360), 100))
        self.speed = random.randint(1, 5)
        self.is_walking = False     
        self.pos = pygame.math.Vector2(self.rect.midbottom)
        self.direction = pygame.math.Vector2(1, 0)
        self.x_direction = 1

        # Variables for animations and movement
        pkmn_states = ["walk", "idle"]
        self.current_state = random.choice(pkmn_states)
        self.walking_distance = random.randint(20, 600)
        self.distance_walked = 0
        self.idle_timer = 0
        self.idle_time = random.randint(100, 300)
        self.sprite_direction = [self.pkmn_walk, self.pkmn_walk_flipped]
        self.chosen_direction = random.choice(self.sprite_direction)

    def update(self):
        self.animation_state(self.current_state)
        if self.current_state == "idle":
            self.idle_sprite()
        elif self.current_state == "walk":
            self.move_sprite()

        # self.is_walking()

    def idle_sprite(self):
        self.pkmn_index += 0.1

        if self.pkmn_index >= len(self.pkmn_idle):
            self.pkmn_index = 0

        self.image = self.pkmn_idle[int(self.pkmn_index)]

        if self.current_state == "idle":
             # Increment idle timer
            self.idle_timer += 1

            # Check if idle time is reached
            if self.idle_timer >= self.idle_time:
                self.current_state = "walk"  # Switch back to walking state
                self.idle_timer = 0  # Reset idle timer
                self.walking_distance = random.randint(20, 500)
                self.x_direction = random.choice([-1, 1])
                self.speed = random.uniform(0.5, 1.3)
                if self.x_direction == -1:
                    self.chosen_direction = self.sprite_direction[0]
                else:
                    self.chosen_direction = self.sprite_direction[1]

    def animation_state(self, current_state):
        # Walking animation
        self.pkmn_index += 0.1

        if self.current_state == "walk":
            
            if self.pkmn_index >= len(self.pkmn_walk):
                self.pkmn_index = 0

            if self.x_direction == -1:
                self.image = self.sprite_direction[0][int(self.pkmn_index)] # look right
            elif self.x_direction == 1:
                self.image = self.sprite_direction[1][int(self.pkmn_index)] # look left 
            else:
                self.image = self.chosen_direction[int(self.pkmn_index)]

        elif current_state == "idle":
            if self.pkmn_index >= len(self.pkmn_idle):
                self.pkmn_index = 0

            self.image = self.pkmn_idle[int(self.pkmn_index)]

    def move_sprite(self):
        # # Boundary check
        if self.current_state == "walk":
            if self.rect.right >= game_width:
                self.x_direction = -1
            elif self.rect.left <= 0:
                self.x_direction = 1

            # Update direction vector
            self.direction.x = self.x_direction * self.speed
     
            self.pos += self.direction
            self.rect.midbottom = self.pos

              # Update distance walked
            self.distance_walked += 1

            # Check if walking distance reached
            if self.distance_walked >= self.walking_distance:
                self.distance_walked = 0
                self.current_state = "idle"  # Switch to idle state
                self.idle_time = random.randint(100, 300)

    def check_walk(self):
        return self.current_state == "walk"
        

    
        