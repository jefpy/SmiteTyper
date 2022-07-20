import pygame
import itertools

pygame.init()
print("RGB loaded.")

class Color():
    def __init__(self):
        super().__init__()
        self.colors = itertools.cycle(['green', 'blue', 'purple', 'pink', 'red', 'orange'])
        self.base_color = next(self.colors)
        self.next_color = next(self.colors)
        self.current_color = self.base_color

        self.FPS = 120
        self.change_every_x_seconds = 1.0
        self.number_of_steps = self.change_every_x_seconds * self.FPS
        self.step = 1

        self.clock = pygame.time.Clock()

    def changeColor(self):
        while True:
            self.step += 1
            if self.step < self.number_of_steps:
                self.current_color = [x + (((y-x)/self.number_of_steps)*self.step) for x, y in zip(pygame.color.Color(self.base_color), pygame.color.Color(self.next_color))]
            else:
                self.step = 1
                self.base_color = self.next_color
                self.next_color = next(self.colors)

            self.clock.tick(self.FPS)
            actualColor = [int(self.current_color[0]), int(self.current_color[1]), int(self.current_color[2])]
            return actualColor