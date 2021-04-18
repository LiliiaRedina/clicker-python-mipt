import pygame


class Petal:
    def __init__(self):
        pygame.init()

        self.screen = None
        self.x_coord = 20
        self.y_coord = 530
        self.radius = 66
        self.num_petals = 0
        self.colour = pygame.Color((255, 255, 255))
        self.coords = []

    def fill_coords(self, coord_centr):
        self.coords.append((coord_centr[0], coord_centr[1] + 100))
        self.coords.append((coord_centr[0] + 71, coord_centr[1] + 71))
        self.coords.append((coord_centr[0] + 100, coord_centr[1]))
        self.coords.append((coord_centr[0] + 71, coord_centr[1] - 71))
        self.coords.append((coord_centr[0], coord_centr[1] - 100))
        self.coords.append((coord_centr[0] - 71, coord_centr[1] - 71))
        self.coords.append((coord_centr[0] - 100, coord_centr[1]))
        self.coords.append((coord_centr[0] - 71, coord_centr[1] + 71))

    def draw(self):
        if self.num_petals < 8:
            pygame.draw.circle(self.screen, self.colour, self.coords[self.num_petals], self.radius)
            pygame.draw.circle(self.screen, pygame.Color('grey'), self.coords[self.num_petals], self.radius, 3)
            self.num_petals += 1

            pygame.display.update()
