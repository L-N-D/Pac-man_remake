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

def draw_button_with_text(self, button_surface, rect, text):
        """Vẽ nút với nội dung chữ"""
        button_with_text = button_surface.copy()  # Sao chép ảnh gốc để vẽ chữ lên
        text_surface, _ = self.font.render(text, RED)
        text_rect = text_surface.get_rect(center=button_with_text.get_rect().center)
        button_with_text.blit(text_surface, text_rect)  # Vẽ chữ lên nút
        self.screen.blit(button_with_text, rect)  # Vẽ nút lên màn hình
        
def button_animation(button_original, button_scaled, button_rect, hovered, mouse_pos):
    """Xử lý hiệu ứng hover cho nút"""
    if button_rect.collidepoint(mouse_pos):
        if not hovered:
            hovered = True
            # Phóng to kích thước nút
            new_size = (int(button_original.get_width() * 1.2), int(button_original.get_height() * 1.2))
            button_scaled = pygame.transform.smoothscale(button_original, new_size)
            button_rect = button_scaled.get_rect(center=button_rect.center)
    else:
        if hovered:
            hovered = False
            button_scaled = button_original.copy()
            button_rect = button_scaled.get_rect(center=button_rect.center)

    return button_scaled, button_rect, hovered