import pygame
import random
import sys
import numpy as np
from time import sleep
import pandas as pd
from being import Being
from food import Food


def dist_points(x1, x2, y1, y2):
    # Find the distance between two points
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)


def step(being, food):
    if len(food) != 0:
        dist_food = np.zeros(len(food))
        for i in range(len(food)):
            x_being = being.getPosition()[0]
            y_being = being.getPosition()[1]
            x_food = food[i].getPosition()[0]
            y_food = food[i].getPosition()[1]
            dist_food[i] = dist_points(x_being, x_food, y_being, y_food)
        closest_tree = np.min(dist_food)
        n_steps = ((closest_tree / 2) ** 2) * 2
        if being.getEnergy() >= n_steps:
            being.feed(closest_tree)
        else:
            being.go_home()
    else:
        being.go_home()
        

def drawGrid(surface):
    for y in range(0, int(height)):
        for x in range(0, int(width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (89, 60, 31), r)
            else:
                rr = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (100, 70, 36), rr)
    

# Grid size parameters
height = 800
width = 800
grid_size = 20
height_grid = int(height / grid_size)
width_grid = int(width / grid_size)

# Possible movements
up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)

# Q-learning entries
state_space_size = width_grid * height_grid
action_size = 8
q_table = np.zeros((int(state_space_size), action_size))
state_table = np.zeros(height_grid * width_grid).tolist()
k = 0
for j in range(0, height_grid):
    for i in range(0, width_grid):
        state_table[k] = (grid_size * i, grid_size * j)
        k += 1


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    being = Being(grid_size, width, height)
    food = []

    for b in range(int(min([height_grid, width_grid]) - 1)):
        food.append(Food(grid_size, width_grid, height_grid))

    while(True):
        clock.tick(30)
        drawGrid(surface)   

        being.handle_keys()

        for tree in food:
            if being.getPosition() == tree.getPosition():
                food.remove(tree) 
            tree.draw(surface)   

        being.draw(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update() 


main()