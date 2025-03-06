
import pygame.freetype
import random
from Context_Interactive import *
from UI_Context import *

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
        
        self.screen.blit(START_ORIGIN, START_BUTTON)
        draw_button_with_text(self, START_ORIGIN, START_BUTTON, "START")
        
        self.screen.blit(MAP_ORIGIN, MAP_BUTTON)
        draw_button_with_text(self, MAP_ORIGIN, MAP_BUTTON, "MAP OPTIONS")
        
        self.screen.blit(LICENSE_ORIGIN, LICENSE_BUTTON)
        draw_button_with_text(self, LICENSE_ORIGIN, LICENSE_BUTTON, "LICENSE")
        
        self.screen.blit(EXIT_ORIGIN, EXIT_BUTTON)
        draw_button_with_text(self, EXIT_ORIGIN, EXIT_BUTTON, "EXIT")
        
        pygame.display.update()  # Cập nhật màn hình

    def run_game(self):
        
        running = True
        while running:
            
            mouse_pos = pygame.mouse.get_pos()
            
            global START_ORIGIN, START_BUTTON, START_BUTTON_HOVERED
            START_ORIGIN, START_BUTTON, START_BUTTON_HOVERED = button_animation(
                BUTTON_ORIGIN, START_ORIGIN, START_BUTTON, START_BUTTON_HOVERED, START_BUTTON_MASK,mouse_pos
            )
            
            global MAP_ORIGIN, MAP_BUTTON, MAP_BUTTON_HOVERED
            MAP_ORIGIN, MAP_BUTTON, MAP_BUTTON_HOVERED = button_animation(BUTTON_ORIGIN, MAP_ORIGIN, MAP_BUTTON, MAP_BUTTON_HOVERED, MAP_BUTTON_MASK,mouse_pos)
            
            global LICENSE_ORIGIN, LICENSE_BUTTON, LICENSE_BUTTON_HOVERED
            LICENSE_ORIGIN, LICENSE_BUTTON, LICENSE_BUTTON_HOVERED = button_animation(BUTTON_ORIGIN, LICENSE_ORIGIN, LICENSE_BUTTON, LICENSE_BUTTON_HOVERED, LICENSE_BUTTON_MASK, mouse_pos)
            
            global EXIT_ORIGIN, EXIT_BUTTON, EXIT_BUTTON_HOVERED
            EXIT_ORIGIN, EXIT_BUTTON, EXIT_BUTTON_HOVERED = button_animation(BUTTON_ORIGIN, EXIT_ORIGIN, EXIT_BUTTON, EXIT_BUTTON_HOVERED, EXIT_BUTTON_MASK, mouse_pos)
            
            self.Menu_draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Thoát game khi nhấn dấu 'X'
                    running = False

        pygame.quit()
            
