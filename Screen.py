import pygame

pygame.init()


def center(size_text, size_surface):

    x = (size_surface[0] // 2) - (size_text[0] // 2)
    y = (size_surface[1] // 2) - (size_text[1] // 2)

    return [x, y]


class Screen:

    def __init__(self, main_display):

        self.main_display = main_display

        self.label = pygame.Surface((300, 100))
        self.label.fill((30, 50, 80))
        self.main_font = pygame.font.SysFont("Arial", 20)

        self.button_label = pygame.Surface((100, 50))
        self.button = pygame.Rect(550, 400, 100, 50)

        self.button_normal = (120, 50, 100)
        self.button_active = (100, 130, 50)

        self.button_select_banc = (self.button_normal,
                                   self.button_active)

        self.text_label_1 = self.main_font.render("Не нажимай на кнопку", False, (0, 0, 0))
        self.text_label_2 = self.main_font.render("Нажми на кнопку", False, (0, 0, 0))
        self.text_select_bank = (self.text_label_1,
                                 self.text_label_2)

        self.text_button = self.main_font.render("КНОПКА", False, (0, 0, 0))

        self.button_indes = 0
        self.button_status = 0




    def draw(self):

        self.main_display.blit(self.label, (450, 300))
        self.label.blit(self.text_select_bank[self.button_status],
                        center(self.text_select_bank[self.button_status].get_size(), self.label.get_size()))

        pygame.draw.rect(self.main_display, (0, 0, 0), self.button)

        self.main_display.blit(self.button_label, (self.button[0], self.button[1]))
        self.button_label.fill(self.button_select_banc[self.button_indes])
        self.button_label.blit(self.text_button, center(self.text_button.get_size(), self.button_label.get_size()))








