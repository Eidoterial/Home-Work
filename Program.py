import Screen
import pygame
import sys

pygame.init()





class Program:

    def __init__(self):
        self.main_display = pygame.display.set_mode((1200, 700))
        self.main_clock = pygame.time.Clock()
        self.program_fps = 60

        self.click_button = 0

        self.bg = (30, 50, 100)

        self.screen = Screen.Screen(self.main_display)

    def run_program(self):

        while True:

            self.main_display.fill(self.bg)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:

                        if self.screen.button_indes == 1:
                            self.screen.label.fill((30, 50, 80))
                            self.click_button += 1

                            if self.screen.button_status == 0:
                                self.screen.button_status = 1
                            elif self.screen.button_status == 1:
                                self.screen.button_status = 0


                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            if self.screen.button.collidepoint(pygame.mouse.get_pos()):
                self.screen.button_indes = 1

            else:
                self.screen.button_indes = 0

            pygame.display.set_caption(f"Ви натиснули на кнопку {self.click_button} раз")
            self.screen.draw()
            pygame.display.update()

            self.main_clock.tick(self.program_fps)




program = Program()