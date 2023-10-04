import pygame
import math

pygame.init()

# Constants for character and background
character_speed = 0.45
scroll_speed = 1.0

# Initialize the screen
FPS = 60
screen_width = 900
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shoot or Die")

#loading sounds
startmenu_sound = pygame.mixer.Sound("startmenu_sound.mp3")
startmenu_sound.set_volume(0.3)

# Load asset images
startmenu_background = pygame.image.load("startmenu_background.png").convert()
startmenu_background = pygame.transform.scale(startmenu_background, (screen_width, screen_height))
background = pygame.image.load("natuur.jpeg").convert() 
background = pygame.transform.scale(background, (screen_width * 2, screen_height))
character_image = pygame.image.load("plane.png").convert_alpha()
character_image = pygame.transform.scale(character_image, (93, 93))

# Initial beginning positions
bg_x = 0
plane_x = 6
plane_y = 175

game_state = "start_menu"

#startmenu (stevefinn)
def draw_start_menu():
    screen.blit(startmenu_background, (0, 0))
    font = pygame.font.SysFont('impact', 40)
    title = font.render('Shoot or Die', True, (255, 255, 255))
    start_button = font.render('Press SPACE to start', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
    pygame.display.update()
    startmenu_sound.play()

# Game loop
clock = pygame.time.Clock()
clock.tick (FPS)
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = "game"
            game_over = False
            startmenu_sound.stop()

    elif game_state == "game":
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            plane_y -= character_speed
        if keys[pygame.K_s]:
            plane_y += character_speed

        #test with a&d, makes it too easy
        if keys[pygame.K_a]:
            plane_x -= character_speed
        if keys[pygame.K_d]:
            plane_x += character_speed


        bg_x -= scroll_speed
        if bg_x <= -screen_width:
            bg_x = 0

        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + screen_width, 0))
        screen.blit(character_image, (plane_x, plane_y))
        pygame.display.update()

# Quit pygame
pygame.quit()