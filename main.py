import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 1600, 900

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jetpack Joyride enemies")

enemy_image = pygame.image.load("missile 22.png")



# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        scaled_enemy_image = pygame.transform.scale(enemy_image, (50, 50))
        self.image = scaled_enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)  # Random horizontal position
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)  # Random vertical position
        self.speed = 7  # Adjust the speed as needed

    def update(self):
        # Move the enemy horizontally (from left to right)
        self.rect.x -= self.speed

        # If the enemy goes off the left edge, reset its position to the left
        if self.rect.right < 0:
            self.rect.x = WIDTH

# Create a sprite group for enemies
all_sprites = pygame.sprite.Group()

# Create and add enemies to the sprite group
for _ in range(14):  # Create 5 enemies
    enemy = Enemy()
    all_sprites.add(enemy)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
