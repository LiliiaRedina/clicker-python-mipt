import pygame


class Statistic:
    def __init__(self):
        pygame.init()

        self.screen = None
        self.num_clicks = 0
        self.num_autoclicks = 0
        self.speed = 0
        self.text_size = 24
        self.x_text_shift = 20
        self.y_text_shift = 20
        self.font = pygame.font.SysFont('Verdana', self.text_size, bold=True)
        self.colour_window = None
        self.colour_text = pygame.Color((150, 150, 255))

    def show(self):
        text_clicks = "NUM CLICKS: {}".format(self.num_clicks)
        render_text_clicks = self.font.render(text_clicks, False, self.colour_text)

        self.screen.fill(rect=pygame.Rect(self.x_text_shift, self.y_text_shift,
                                            self.text_size * len(text_clicks), self.text_size + 1),
                         color=self.colour_window)
        self.screen.blit(render_text_clicks, (self.x_text_shift, self.y_text_shift))

        text_auto = "NUM AUTOCLICKS: {}".format(self.num_autoclicks)
        render_text_auto = self.font.render(text_auto, False, self.colour_text)

        self.screen.fill(rect=pygame.Rect(self.x_text_shift, 2.5 * self.y_text_shift,
                                          self.text_size * len(text_auto), self.text_size + 1),
                         color=self.colour_window)
        self.screen.blit(render_text_auto, (self.x_text_shift, 2.5 * self.y_text_shift))

        text_speed = "SPEED: {}".format(self.speed)
        render_text_speed = self.font.render(text_speed, False, self.colour_text)

        self.screen.fill(rect=pygame.Rect(self.x_text_shift, 4 * self.y_text_shift,
                                          self.text_size * len(text_speed), self.text_size + 1),
                         color=self.colour_window)
        self.screen.blit(render_text_speed, (self.x_text_shift, 4 * self.y_text_shift))

        pygame.display.update()

    def update_clicks(self, count):
        self.num_clicks += count
        self.show()

    def update_autoclicks(self):
        self.num_autoclicks += 1
        self.show()

    def update_speed(self, new_speed):
        self.speed = new_speed
        self.show()
