import pygame
import random

def load_animation(path, animation_type, num_frames, flip=False):
        frames = []
        for i in range(1, num_frames + 1):
            if flip:
                filename = f'{path}/{animation_type}{i}-f.png'
            else:
                filename = f'{path}/{animation_type}{i}.png'

            image = pygame.image.load(filename).convert_alpha()
            frames.append(image)
        return frames

class Pokemon(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
         # Size of the screen
        self.game_width = 600
        self.game_height = 300

        # LOAD ANIMATIONS #
        # walking animations
        self.pkmn_walk = load_animation("cyndaquil", "walk", 6, False)
        self.pkmn_walk_flipped = load_animation("cyndaquil", "walk", 6, True)

        # idle animation
        self.pkmn_idle = load_animation("cyndaquil", 'idle', 6, False)
        self.pkmn_idle_flipped = load_animation("cyndaquil", 'idle', 6, True)

        # yawn animation
        self.pkmn_yawn = load_animation("cyndaquil", "yawn", 2, False)

        # sleep animation
        self.pkmn_sleep = load_animation("cyndaquil", "sleep", 3, False)
      
        self.pkmn_index = 0
        self.image = self.pkmn_walk[self.pkmn_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(30, 360), 245))
        self.speed = random.uniform(0.3, 0.9)
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
        self.chosen_idle_direction = self.pkmn_idle[int(self.pkmn_index)]

    def update(self):
        self.animation_state(self.current_state)
        if self.current_state == "idle":
            self.idle_sprite()
        elif self.current_state == "walk":
            self.move_sprite()
        elif self.current_state == "yawn":
            self.yawn_sprite()
        elif self.current_state == "sleep":
            self.sleep_sprite()

    def idle_sprite(self):
        self.pkmn_index += 0.1

        if self.pkmn_index >= len(self.pkmn_idle):
            self.pkmn_index = 0

        self.image = self.chosen_idle_direction

        # Increment idle timer
        self.idle_timer += 1

        # Check if idle time is reached
        if self.idle_timer >= self.idle_time:
            sleep_chance = random.randint(1, 2)
            # check sleep
            if sleep_chance == 1:
                self.current_state = "sleep"
                self.idle_time = random.randint(800, 1200)
            
            else:
                self.current_state = "walk"  # Switch back to walking state
                self.idle_timer = 0  # Reset idle timer
                self.walking_distance = random.randint(20, 300)
                self.x_direction = random.choice([-1, 1])
                self.speed = random.uniform(0.3, 0.9)
                if self.x_direction == -1:
                    self.chosen_direction = self.sprite_direction[0]
                else:
                    self.chosen_direction = self.sprite_direction[1]

    def yawn_sprite(self):
        # increment index
        self.pkmn_index += 0.1

        # reset sprite array
        if self.pkmn_index >= len(self.pkmn_yawn):
            self.pkmn_index = 0

        self.image = self.pkmn_yawn[int(self.pkmn_index)]

        # increment timer
        self.idle_timer += 1

        # Check if idle time is reached
        if self.idle_timer >= self.idle_time:
            self.current_state = "walk"  # Switch back to walking state
            self.idle_timer = 0  # Reset idle timer
            self.walking_distance = random.randint(20, 300)
            self.x_direction = random.choice([-1, 1])
            self.speed = random.uniform(0.3, 0.9)
            if self.x_direction == -1:
                self.chosen_direction = self.sprite_direction[0]
            else:
                self.chosen_direction = self.sprite_direction[1]

    def sleep_sprite(self):
        # increment index
        self.pkmn_index += 0.01

        # reset sprite array
        if self.pkmn_index >= len(self.pkmn_sleep):
            self.pkmn_index = 0

        self.image = self.pkmn_sleep[int(self.pkmn_index)]

        # increment timer
        self.idle_timer += 1

        # Check if idle time is reached
        if self.idle_timer >= self.idle_time:
            self.distance_walked = 0
            self.current_state = "idle"  # Switch to idle state
            self.idle_time = random.randint(100, 300)

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

            if self.x_direction == -1:
                self.chosen_idle_direction = self.pkmn_idle[int(self.pkmn_index)]
            else:
                self.chosen_idle_direction = self.pkmn_idle_flipped[int(self.pkmn_index)]
                
    def move_sprite(self):
        # # Boundary check
        if self.current_state == "walk":
            if self.rect.right >= self.game_width:
                self.x_direction = -1
            elif self.rect.left <= 0:
                self.x_direction = 1
            
            # random direction change
            direction_change = random.randint(1, 300)
            if direction_change == 5:
                if self.x_direction == -1:
                    self.x_direction = 1
                else:
                    self.x_direction = -1

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
                
                yawn_anim = random.randint(1, 100)
                if yawn_anim == 1:    
                    self.idle_time = random.randint(30, 55)              
                    self.current_state = "yawn"

    def check_walk(self):
        return self.current_state == "walk"
    
    def resize_screen(self, width, height):
        self.game_width = width
        self.game_height = height

    
        