import pygame

from petal import Petal


class Button:
    def __init__(self):
        pygame.init()

        self.screen = None
        self.x_coord = 300
        self.y_coord = 270
        self.radius = 80
        self.text_colour = pygame.Color((210, 105, 30))
        self.text_size = 40
        self.font = pygame.font.SysFont('Verdana', self.text_size, bold=True)
        self.colour = pygame.Color((210, 105, 30))
        self.colour_fill = pygame.Color((255, 191, 0))

    def draw(self):
        pygame.draw.circle(self.screen, self.colour_fill, (self.x_coord, self.y_coord), self.radius)
        pygame.draw.circle(self.screen, self.colour, (self.x_coord, self.y_coord), self.radius, 4)

        text = "CLICK"
        render_text = self.font.render(text, False, self.text_colour)
        self.screen.blit(render_text, (self.x_coord - len(text) * self.text_size * 0.33,
                                  self.y_coord - self.text_size * 0.6))

        pygame.display.update()


class ButtonAutoclick:
    def __init__(self):
        pygame.init()

        self.screen = None
        self.x_coord = 20
        self.y_coord = 460
        self.num_clicks_for_buy = 2
        self.colour = pygame.Color((255, 255, 255))
        self.border_colour = pygame.Color((255, 255, 255))
        self.text_colour = pygame.Color((150, 150, 150))
        self.text_size = 24
        self.h_coord = self.text_size * 2.3
        self.w_coord = self.text_size * 7
        self.font = pygame.font.SysFont('Verdana', self.text_size, bold=True)
        self.font2 = pygame.font.SysFont('Verdana', int(self.text_size / 2), bold=True)

    def draw(self):
        text_price = "BUY ({})".format(self.num_clicks_for_buy)
        render_text_price = self.font.render(text_price, False, self.text_colour)

        text_name = "AUTOCLICKS"
        render_text_name = self.font2.render(text_name, False, self.text_colour)

        pygame.draw.rect(self.screen, self.colour, (self.x_coord, self.y_coord, self.w_coord, self.h_coord),
                         border_bottom_left_radius=15, border_top_right_radius=15)
        pygame.draw.rect(self.screen, self.border_colour, (self.x_coord, self.y_coord, self.w_coord, self.h_coord), 5,
                         border_bottom_left_radius=15, border_top_right_radius=15)

        self.screen.blit(render_text_price, (self.x_coord + self.text_size * 0.5,
                                  self.y_coord + self.text_size * 0.75))
        self.screen.blit(render_text_name, (self.x_coord + self.text_size * 0.5,
                                  self.y_coord + self.text_size * 0.2))

        pygame.display.update()


class ButtonPetal:
    def __init__(self):
        pygame.init()

        self.petals = Petal()

        self.screen = None
        self.x_coord = 20
        self.y_coord = 530
        self.num_clicks_for_buy = 4
        self.colour = pygame.Color((255, 255, 255))
        self.border_colour = pygame.Color((255, 255, 255))
        self.text_colour = pygame.Color((150, 150, 150))
        self.text_size = 24
        self.h_coord = self.text_size * 2.3
        self.w_coord = self.text_size * 7
        self.font = pygame.font.SysFont('Verdana', self.text_size, bold=True)
        self.font2 = pygame.font.SysFont('Verdana', int(self.text_size / 2), bold=True)

    def draw(self):
        text_price = "ADD ({})".format(self.num_clicks_for_buy)
        render_text_price = self.font.render(text_price, False, self.text_colour)

        text_name = "PETALS"
        render_text_name = self.font2.render(text_name, False, self.text_colour)

        pygame.draw.rect(self.screen, self.colour, (self.x_coord, self.y_coord, self.w_coord, self.h_coord),
                         border_bottom_left_radius=15, border_top_right_radius=15)
        pygame.draw.rect(self.screen, self.border_colour, (self.x_coord, self.y_coord, self.w_coord, self.h_coord), 5,
                         border_bottom_left_radius=15, border_top_right_radius=15)

        self.screen.blit(render_text_price, (self.x_coord + self.text_size * 0.5,
                                  self.y_coord + self.text_size * 0.75))
        self.screen.blit(render_text_name, (self.x_coord + self.text_size * 0.5,
                                   self.y_coord + self.text_size * 0.2))

        pygame.display.update()
