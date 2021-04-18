import sys
import pygame

from bonus import Bonus
from button import Button
from statistic import Statistic


class Game:
    def __init__(self):
        self.button = Button()
        self.statistic = Statistic()
        self.bonus = Bonus()
        self.h_window = 600
        self.w_window = 600
        self.colour_window = pygame.Color((200, 200, 255))

        pygame.init()

        self.screen = pygame.display.set_mode((self.h_window, self.w_window))
        self.construct_game()

        self.screen.fill(self.colour_window)

        self.statistic.show()
        self.bonus.draw()
        self.button.draw()

        pygame.display.update()

    def construct_game(self):
        self.button.screen = self.screen
        self.statistic.screen = self.screen
        self.bonus.screen = self.screen
        self.bonus.button_autoclick.screen = self.screen
        self.bonus.button_petal.screen = self.screen
        self.bonus.button_petal.petals.screen = self.screen
        self.bonus.button_petal.petals.fill_coords([self.button.x_coord, self.button.y_coord])
        self.statistic.colour_window = self.colour_window

    def play(self):
        time = 0
        last_num_clicks = 0

        while True:
            pygame.time.delay(100)

            time += 1
            if time == 10:
                self.statistic.update_speed(self.statistic.num_clicks - last_num_clicks)
                last_num_clicks = self.statistic.num_clicks

                self.statistic.update_clicks(self.statistic.num_autoclicks)
                time = 0

            self.bonus.update_buttons(self.statistic.num_clicks)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONUP:
                    click = pygame.mouse.get_pos()

                    if self.check_press_to_obj_circle(click, self.button):

                        self.statistic.update_clicks(1)

                    elif self.check_press_to_obj_rect(click, self.bonus.button_autoclick) and \
                            self.statistic.num_clicks >= self.bonus.button_autoclick.num_clicks_for_buy:

                        self.statistic.update_autoclicks()
                        self.statistic.update_clicks(-self.bonus.get_price_autoclick())
                        self.bonus.update_price_autoclicks()

                    elif self.check_press_to_obj_rect(click, self.bonus.button_petal) and \
                            self.statistic.num_clicks >= self.bonus.button_petal.num_clicks_for_buy:

                        self.bonus.update_petals()
                        self.button.draw()
                        self.statistic.update_clicks(-self.bonus.get_price_add_petal())
                        self.bonus.update_price_petals()

                elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:

                    self.statistic.update_clicks(1)

    def check_press_to_obj_circle(self, click, obj):
        coord_obj = (click[0] - obj.x_coord) ** 2 + (click[1] - obj.y_coord) ** 2
        return coord_obj <= self.button.radius ** 2

    def check_press_to_obj_rect(self, click, obj):
        return obj.x_coord < click[0] < obj.x_coord + obj.w_coord and \
               obj.y_coord < click[1] < obj.y_coord + obj.h_coord
