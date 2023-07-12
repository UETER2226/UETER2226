import pygame
from menu import *


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.mouse_clicked = False
        self.DISPLAY_W, self.DISPLAY_H = 720, 640
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        self.background = pygame.image.load(r'D:\python game\how_to_make_a_menu\game bg for Dung-Recovered.png')
        self.background = pygame.transform.scale(self.background, (self.DISPLAY_W, self.DISPLAY_H))

    def game_loop(self):
        while self.curr_menu.run_display:
            self.check_events()
            self.window.blit(self.background, (0, 0))
            self.curr_menu.display_menu()
            pygame.display.update()
            self.reset_keys()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Xử lý sự kiện click chuột trái
                    self.mouse_clicked = True

    def reset_keys(self):
        self.mouse_clicked = False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
     
    



