import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset_x = -70
        self.offset_y = -10

    def draw_cursor(self):
        self.cursor_rect.x = self.cursor_rect.x + self.offset_x
        self.cursor_rect.y = self.cursor_rect.y + self.offset_y
        pygame.draw.circle(self.game.display, self.game.WHITE, self.cursor_rect.center, 10)



    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset_x, self.starty)
        self.start_rect = pygame.Rect(0, 0, 140, 40)  # Vùng bao quanh tùy chọn "Start Game"
        self.options_rect = pygame.Rect(0, 0, 140, 40)  # Vùng bao quanh tùy chọn "Options"
        self.credits_rect = pygame.Rect(0, 0, 140, 40)  # Vùng bao quanh tùy chọn "Credits"
        self.subject_selected = False  # Thêm thuộc tính subject_selected

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_mouse_hover()  # Thêm phần kiểm tra di chuột qua các tùy chọn
            if self.game.mouse_clicked:
                if self.state == 'Start'and not self.subject_selected:
                    self.subject_selected = True
                elif self.state == 'Options':
                    self.game.curr_menu = self.game.options
                    self.run_display = False
                elif self.state == 'Credits':
                    self.game.curr_menu = self.game.credits
                    self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()
            
            # Hiển thị menu "Subject" khi tùy chọn "Start Game" được chọn
            if self.subject_selected:
                subject_menu = SubjectMenu(self.game)
                subject_menu.display_menu()
                self.subject_selected = False  # Đặt lại subject_selected để có thể hiển thị menu "Subject" lần tiếp theo

    def check_mouse_hover(self):
        self.start_rect.topleft = (self.startx - 70, self.starty - 20)
        self.options_rect.topleft = (self.optionsx - 70, self.optionsy - 20)
        self.credits_rect.topleft = (self.creditsx - 70, self.creditsy - 20)
        if self.start_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.startx + self.offset_x, self.starty)
            self.state = 'Start'
        elif self.options_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.optionsx + self.offset_x, self.optionsy)
            self.state = 'Options'
        elif self.credits_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.creditsx + self.offset_x, self.creditsy)
            self.state = 'Credits'

    

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset_x, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_mouse_click()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_mouse_click(self):
        if self.game.mouse_clicked:
            if self.state == 'Volume':
                # Xử lý khi click vào tùy chọn Volume
                pass
            elif self.state == 'Controls':
                # Xử lý khi click vào tùy chọn Controls
                pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.mouse_clicked:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by Quang Dung and Huy Long', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()

class SubjectMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'History'
        self.historyx, self.historyy = self.mid_w, self.mid_h + 20
        self.geographyx, self.geographyy = self.mid_w, self.mid_h + 40
        self.mathx, self.mathy = self.mid_w, self.mid_h + 60
        self.physicsx, self.physicsy = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.historyx + self.offset_x, self.historyy)
        self.history_rect = pygame.Rect(0, 0, 140, 40)  
        self.geography_rect = pygame.Rect(0, 0, 140, 40)  
        self.math_rect = pygame.Rect(0, 0, 140, 40)  
        self.physics_rect = pygame.Rect(0, 0, 140, 40) 
        self.modegame_selected = False  # Thêm thuộc tính subject_selected

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_mouse_hoverr()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Subject', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("History", 20, self.historyx, self.historyy)
            self.game.draw_text("Geography", 20, self.geographyx, self.geographyy)
            self.game.draw_text("Math", 20, self.mathx, self.mathy)
            self.game.draw_text("Physics", 20, self.physicsx, self.physicsy)
            self.draw_cursor()  # Vẽ con trỏ chuột
            self.check_input()
            self.blit_screen()


    def check_mouse_hoverr(self):
        self.history_rect.topleft = (self.historyx - 70, self.historyy - 20)
        self.geography_rect.topleft = (self.geographyx - 70, self.geographyy - 20)
        self.math_rect.topleft = (self.mathx - 70, self.mathy - 20)
        self.physics_rect.topleft = (self.physicsx - 70, self.physicsy - 20)
        if self.history_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.historyx + self.offset_x, self.historyy)
            self.state = 'History'
        elif self.geography_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.geographyx + self.offset_x, self.geographyy)
            self.state = 'Geography'
        elif self.math_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.mathx + self.offset_x, self.mathy)
            self.state = 'Math'
        elif self.physics_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.physicsx + self.offset_x, self.physicsy)
            self.state = 'Physics'    

    def check_input(self):
        if self.game.mouse_clicked:
            if self.state == 'History':
                mode_game = GameModeMenu(self.game)
                mode_game.display_menu()
            elif self.state == 'Geography':
                mode_game = GameModeMenu(self.game)
                mode_game.display_menu()
            elif self.state == 'Math':
                mode_game = GameModeMenu(self.game)
                mode_game.display_menu()
            elif self.state == 'Physics':
                mode_game = GameModeMenu(self.game)
                mode_game.display_menu()

class GameModeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Classic'
        self.classicx, self.classicy = self.mid_w, self.mid_h + 20
        self.racex, self.racey = self.mid_w, self.mid_h + 40
        self.monsterx, self.monstery = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.classicx + self.offset_x, self.classicy)
        self.classic_rect = pygame.Rect(0, 0, 140, 40)
        self.race_rect = pygame.Rect(0, 0, 140, 40)
        self.monster_rect = pygame.Rect(0, 0, 140, 40)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.check_mouse_hover()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Mode Game', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Classic", 20, self.classicx, self.classicy)
            self.game.draw_text("Race", 20, self.racex, self.racey)
            self.game.draw_text("Monster Fighting", 20, self.monsterx, self.monstery)
            self.draw_cursor()
            self.blit_screen()

    def check_mouse_hover(self):
        self.classic_rect.topleft = (self.classicx - 70, self.classicy - 20)
        self.race_rect.topleft = (self.racex - 70, self.racey - 20)
        self.monster_rect.topleft = (self.monsterx - 70, self.monstery - 20)
        if self.classic_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.classicx + self.offset_x -50, self.classicy)
            self.state = 'Classic'
        elif self.race_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.racex + self.offset_x - 50, self.racey)
            self.state = 'Race'
        elif self.monster_rect.collidepoint(pygame.mouse.get_pos()):
            self.cursor_rect.midtop = (self.monsterx + self.offset_x - 50, self.monstery)
            self.state = 'Monster Fighting'

    def check_input(self):
        if self.game.mouse_clicked:
            if self.state == 'Classic':
                # Xử lý khi chọn mode Classic
                pass
            elif self.state == 'Race':
                # Xử lý khi chọn mode Race
                pass
            elif self.state == 'Monster Fighting':
                # Xử lý khi chọn mode Monster Fighting
                pass





