import pygame

from button import ButtonAutoclick, ButtonPetal


class Bonus:
    def __init__(self):
        self.screen = None
        self.button_autoclick = ButtonAutoclick()
        self.button_petal = ButtonPetal()

    def draw(self):
        self.button_autoclick.draw()
        self.button_petal.draw()

    def update_buttons(self, num_clicks):
        if num_clicks >= self.get_price_autoclick():
            self.button_autoclick.border_colour = pygame.Color((150, 150, 255))
            self.button_autoclick.draw()
        else:
            self.button_autoclick.border_colour = pygame.Color((255, 255, 255))
            self.button_autoclick.draw()

        if num_clicks >= self.get_price_add_petal():
            self.button_petal.border_colour = pygame.Color((150, 150, 255))
            self.button_petal.draw()
        else:
            self.button_petal.border_colour = pygame.Color((255, 255, 255))
            self.button_petal.draw()

    def update_price_autoclicks(self):
        self.button_autoclick.num_clicks_for_buy *= 2

    def update_price_petals(self):
        self.button_petal.num_clicks_for_buy *= 2

    def get_price_autoclick(self):
        return self.button_autoclick.num_clicks_for_buy

    def get_price_add_petal(self):
        return self.button_petal.num_clicks_for_buy

    def update_petals(self):
        self.button_petal.petals.draw()
