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


def handle_events (button):
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       if event.type == pygame.MOUSEBUTTONDOWN:
          if button.collidepoint(event.pos):
            pygame.quit()
            sys.exit()
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True


def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here


   # -- fonts -- #
   font = pygame.font.SysFont('Ariel', 35, bold=True)
   surf = font.render('Quit', True, config.BLACK)


   # -- Button Variables -- # 
   button_length =200
   button_width = 60
   button_x = 280
   button_y = 250
   button = pygame.Rect(button_x, button_y, button_length, button_width)


   # -- Define Surface -- #
   surf_rect = surf.get_rect()
   surf_rect.center = button.center
   

   running = True
   while running:
      running = handle_events(button)
      screen.fill(config.WHITE) # Use color from config


      # -- Get Mouse Position -- #
      mouse_x, mouse_y = pygame.mouse.get_pos()


      # -- If Collid With Button -- #
      if button.collidepoint(mouse_x, mouse_y):
         button_color = config.RED
      else: 
         button_color = (240, 60, 50)

      pygame.draw.rect(screen, button_color, button)

      screen.blit(surf, surf_rect)


      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate


   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()