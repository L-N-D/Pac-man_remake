

def draw_button_text(self):
        button_with_text = self.button_scaled.copy()  # Sao chép ảnh gốc để vẽ chữ lên
        text_surface, _ = self.font.render("START", RED)
        text_rect = text_surface.get_rect(center=button_with_text.get_rect().center)
        button_with_text.blit(text_surface, text_rect)  # Vẽ chữ lên nút
        self.screen.blit(button_with_text, self.button_rect)  # Vẽ nút lên màn hình
        
def button_animation(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.button_rect.collidepoint(mouse_x, mouse_y):
            if not self.button_hovered:
                self.button_hovered = True
                # Phóng to 10% kích thước
                new_size = (int(self.button_original.get_width() * 2), int(self.button_original.get_height() * 1.2))
                self.button_scaled = pygame.transform.smoothscale(self.button_original, new_size)
                self.button_rect = self.button_scaled.get_rect(center=START_BUTTON.center)
        else:
            if self.button_hovered:
                self.button_hovered = False
                self.button_scaled = BUTTON
                self.button_rect = BUTTON.get_rect(center=START_BUTTON.center)