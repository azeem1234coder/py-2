import pygame
import random

# Initialize pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Custom event for changing the sprite colors
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Define a simple Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, radius=50):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self, new_color):
        self.color = new_color
        self.image.fill((0, 0, 0, 0))  # Clear previous image
        pygame.draw.circle(self.image, self.color, (self.rect.width // 2, self.rect.height // 2), self.rect.width // 2)

# Create two sprites
sprite1 = Sprite(RED, 200, 300)
sprite2 = Sprite(GREEN, 600, 300)

# Create a sprite group and add the sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            # Change the color of both sprites randomly
            new_color1 = random.choice([RED, GREEN, BLUE])
            new_color2 = random.choice([RED, GREEN, BLUE])
            sprite1.change_color(new_color1)
            sprite2.change_color(new_color2)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Custom event to change color every 3 seconds
    pygame.time.set_timer(CHANGE_COLOR_EVENT, 3000)

    clock.tick(60)  # Maintain 60 frames per second

pygame.quit()
