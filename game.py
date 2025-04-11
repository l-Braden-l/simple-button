# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
def init_game (): 
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events (button, button2):
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       if event.type == pygame.MOUSEBUTTONDOWN:
          # -- Quit -- #
          if button.collidepoint(event.pos):
            pygame.quit()
            sys.exit()
          # -- Play -- #
          if button2.collidepoint(event.pos): 
             button2.y = -100
             button.y = -100
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True


def main():
    screen = init_game()
    clock = pygame.time.Clock()

    # -- Set Position Of Graphic -- #
    background_position = [0,0]


    # -- Load Backgrond -- # 
    background_image = pygame.image.load("C:\move-spaceship-images\saturn_family1.jpg").convert()


    # -- Fonts -- #
    font = pygame.font.SysFont('Ariel', 35, bold=True)
    quit_text = font.render('Quit', True, config.BLACK)
    play_text = font.render('Play', True, config.BLACK)
    welcome_text = font.render('Welcome to My Game!', True, config.BLACK)

    # -- Button Variables -- # 
    button_length = 200
    button_width = 60
    button_x = 280
    button_y = 250

    # -- Quit Button -- #
    button = pygame.Rect(button_x, button_y, button_length, button_width)

    # -- Play Button -- #
    button_y2 = 150
    button2 = pygame.Rect(button_x, button_y2, button_length, button_width)

    # -- Define Surfaces (QUIT & PLAY) -- #
    surf_rect = quit_text.get_rect()
    surf_rect.center = button.center
    surf_rect2 = play_text.get_rect()
    surf_rect2.center = button2.center
    surface_welcome = (300,300)

    running = True
    while running:
        running = handle_events(button, button2)
        screen.fill(config.WHITE)

        # -- Get Mouse Position -- #
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # -- If Collid With Button (QUIT)-- #
        if button.collidepoint(mouse_x, mouse_y):
            button_color = config.RED
        else:
            button_color = (240, 60, 50)

        # -- If Collid With Button (PLAY)-- #
        if button2.collidepoint(mouse_x, mouse_y):
            button_color2 = (36, 202, 219)
        else:
            button_color2 = (39, 160, 216)

        # -- Draw buttons -- #
        pygame.draw.rect(screen, button_color, button)
        pygame.draw.rect(screen, button_color2, button2)

        # -- If Button (0,y) Less Then 0 -- #
        if button2.y >= 0:
            screen.blit(play_text, surf_rect2)
            screen.blit(quit_text, surf_rect)
            
        else: 
           screen.blit(welcome_text, surface_welcome) # If y-cord of Button's are anything other then negative
           screen.blit(background_image, background_position)
        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
   main()