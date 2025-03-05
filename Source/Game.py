
import pygame.freetype
import random
from Context_Interactive import *

import sys
import os

# Lấy đường dẫn thư mục hiện tại (Source/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Lấy đường dẫn thư mục cha (PacManProject/)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))

# Thêm Const_definition vào sys.path
sys.path.append(parent_dir)

# Import Properties.py
from Const_definition.Properties import *




class GAME:
    
    def __init__(self):
        pygame.init()
        
        # set up window properties
        self.font = pygame.freetype.SysFont(None, 24)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.title = pygame.display.set_caption(WINDOW_TITLE)
        
        
        
        self.home_background = pygame.image.load(HOME_BACKGROUND)
        self.home_background = pygame.transform.scale(self.home_background, (HOME_WIDTH, HOME_HEIGHT))
        
        # Sao chép thông tin nút
        self.button_original = BUTTON
        self.button_scaled = BUTTON
        self.button_rect = START_BUTTON.copy()

        # Trạng thái hiệu ứng
        self.button_hovered = False
    
    
    
    def Menu_draw(self):
        """Vẽ màn hình trang chủ"""
        self.screen.fill(BLACK)
        self.screen.blit(self.home_background, (0, 0))
        self.screen.blit(BUTTON, START_BUTTON)
        self.draw_button_text()
        pygame.display.update()  # Cập nhật màn hình
        
    



    def run_game(self):
        """Chạy vòng lặp game"""
        running = True
        while running:
            
            self.button_animation()
            self.Menu_draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Thoát game khi nhấn dấu 'X'
                    running = False

        pygame.quit()
            
