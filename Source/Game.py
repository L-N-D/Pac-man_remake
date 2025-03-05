
import pygame.freetype
import random
from Context_Interactive import *

class GAME:
    
    def __init__(self):
        pygame.init()
        
        # set up window properties
        self.font = pygame.freetype.SysFont(None, 24)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.title = pygame.display.set_caption(WINDOW_TITLE)
        
        self.home_background = pygame.image.load(HOME_BACKGROUND)
        self.home_background = pygame.transform.scale(self.home_background, (HOME_WIDTH, HOME_HEIGHT))   
    
    # DISPLAY HOME SCREEN
    def Menu_draw(self):
        
        self.screen.fill(BLACK)
        self.screen.blit(self.home_background, (0, 0))
        
        self.screen.blit(BUTTON, START_BUTTON)
        draw_button_with_text(self, BUTTON, START_BUTTON, "START")
        
        pygame.display.update()  # Cập nhật màn hình
        
    



    def run_game(self):
        
        running = True
        while running:
            
            mouse_pos = pygame.mouse.get_pos()
            
            global BUTTON, START_BUTTON, START_BUTTON_HOVERED
            BUTTON, START_BUTTON, START_BUTTON_HOVERED = button_animation(
                BUTTON_ORIGIN, BUTTON, START_BUTTON, START_BUTTON_HOVERED, mouse_pos
            )
            self.Menu_draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Thoát game khi nhấn dấu 'X'
                    running = False

        pygame.quit()
            
