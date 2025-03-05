# declare default setting
import pygame

# color definition
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
CYAN    = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY    = (128, 128, 128)
ORANGE  = (255, 165, 0)
PURPLE  = (128, 0, 128)
BROWN   = (165, 42, 42)
PINK    = (255, 192, 203)

# window setting
WINDOW_WIDTH, WINDOW_HEIGHT = 1024, 768
WINDOW_TITLE = r'PAC-MAN'
FPS = 60

# Map pool
MAP_POOL = [r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/maps/map_1.png",
           r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/maps/map_2.png",
           r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/maps/map_3.png",
           r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/maps/map_4.png",
           r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/maps/map_5.png"]

MAP_INPUT_TXT = [[r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_1/map_1.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_1/map_2.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_1/map_3.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_1/map_4.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_1/map_5.txt"],
                 [r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_2/map_1.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_2/map_2.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_2/map_3.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_2/map_4.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_2/map_5.txt"],
                 [r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_3/map_1.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_3/map_2.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_3/map_3.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_3/map_4.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_3/map_5.txt"],
                 [r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_4/map_1.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_4/map_2.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_4/map_3.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_4/map_4.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_4/map_5.txt"],
                 [r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_5/map_1.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_5/map_2.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_5/map_3.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_5/map_4.txt", r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/levels/level_5/map_5.txt"]]

MAP_NUM = len(MAP_POOL)

# Background
HOME_BACKGROUND = r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/bg/home_background.jpg"
ABOUT_BACKGROUND = r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/bg/about_bg.png"
GAMEOVER_BACKGROUND = r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/bg/gameover_bg.png"
VICTORY_BACKGROUND = r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/bg/victory_bg.jpg"

# Screen state
STATE_HOME = "home"
STATE_PLAYING = "playing"
STATE_ABOUT = "about"
STATE_LEVEL = "level"
STATE_SETTING = "setting"
STATE_GAMEOVER = "gameover"
STATE_VICTORY = 'victory'

# Home UI layout

BUTTON_SOURCE = r"D:/HCMUS_2023-2024/Artificial_Inteligent/Pac_Man_Clone/Assets/UI_Context/button.png"
BUTTON = pygame.image.load(BUTTON_SOURCE)   


HOME_WIDTH, HOME_HEIGHT = WINDOW_WIDTH, WINDOW_HEIGHT
START_BUTTON = BUTTON.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100))
