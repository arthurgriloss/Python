import pygame
import random

class Food(object):
    def __init__(self, grid_size, grid_width, grid_height):
        self.position = (0, 0)
        self.color = (31, 61, 12)
        self.grid_size = grid_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.randomize_position()


    def getPosition(self):
        return self.position


    def randomize_position(self):
        self.position = (random.randint(1, self.grid_width - 2) * self.grid_size, random.randint(1, self.grid_height - 2) *  self.grid_size)
        

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (self.grid_size, self.grid_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)