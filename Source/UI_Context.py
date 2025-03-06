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

# START BUTTON INFO
START_ORIGIN = BUTTON_ORIGIN.copy()
START_BUTTON = START_ORIGIN.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100))
START_BUTTON_RECT = pygame.Rect(START_BUTTON)
START_BUTTON_MASK = pygame.mask.from_surface(START_ORIGIN)
START_BUTTON_HOVERED = False

# MAP BUTTON
MAP_ORIGIN = BUTTON_ORIGIN.copy()
MAP_BUTTON = MAP_ORIGIN.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
MAP_BUTTON_RECT = pygame.Rect(MAP_BUTTON)
MAP_BUTTON_MASK = pygame.mask.from_surface(MAP_ORIGIN)
MAP_BUTTON_HOVERED = False

LICENSE_ORIGIN = BUTTON_ORIGIN.copy()
LICENSE_BUTTON = LICENSE_ORIGIN.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
LICENSE_BUTTON_RECT = pygame.Rect(LICENSE_BUTTON)
LICENSE_BUTTON_MASK = pygame.mask.from_surface(LICENSE_ORIGIN)
LICENSE_BUTTON_HOVERED = False

EXIT_ORIGIN = BUTTON_ORIGIN.copy()
EXIT_BUTTON = EXIT_ORIGIN.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 200))
EXIT_BUTTON_RECT = pygame.Rect(EXIT_BUTTON)
EXIT_BUTTON_MASK = pygame.mask.from_surface(EXIT_ORIGIN)
EXIT_BUTTON_HOVERED = False