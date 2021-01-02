import pygame
import random
import sys
import numpy as np
from time import sleep
import pandas as pd

class Human(object):
    def __init__(self):
        self.position = (grid_size, 0)
        self.color = (255, 255, 255)
        self.direction = up
    

    def move(self):
        cur = self.getPosition()
        x, y = self.direction
        new = (((cur[0] + (x * grid_size)) % width), (cur[1] + (y * grid_size)) % height)
        if new[0] == width - grid_size:
            pass
        elif new[1] == height - grid_size:
            if new[0] == width - 2 * grid_size:
                self.position = new
            else:
                pass
        elif new[0] == 0:
            pass
        elif new[1] == 0:
            pass
        else: 
            self.position = new


    def getPosition(self):
        return self.position


    def getDirection(self):
        return self.direction

    def setDirection(self, direction):
        self.direction = direction


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP8:
                    self.direction = up
                    self.move()
                elif event.key == pygame.K_KP2:
                    self.direction = down
                    self.move()
                elif event.key == pygame.K_KP4:
                    self.direction = left
                    self.move()
                elif event.key == pygame.K_KP6:
                    self.direction = right
                    self.move()
                elif event.key == pygame.K_KP9:
                    self.direction = up_right
                    self.move()
                elif event.key == pygame.K_KP7:
                    self.direction = up_left
                    self.move()
                elif event.key == pygame.K_KP1:
                    self.direction = down_left
                    self.move()
                elif event.key == pygame.K_KP3:
                    self.direction = down_right
                    self.move()
                    

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


    def reset(self):
        self.position = (grid_size, 0)


class Bomb(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (0, 0, 0)
        self.randomize_position()
    

    def randomize_position(self):
        self.position = (random.randint(1, width_grid - 2) * grid_size, random.randint(1, height_grid - 2) * grid_size)


    def getPosition(self):
        return self.position


    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


    def explode(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, (255, 0, 0), r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


def drawGrid(surface):
    for y in range(0, int(height)):
        for x in range(0, int(width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (84, 194, 205), rr)
    for x in range(0, int(width)):
        boarder = pygame.Rect((x * grid_size, width - grid_size), ( grid_size, grid_size))
        pygame.draw.rect(surface, (200, 200, 200), boarder)
        pygame.draw.rect(surface, (125, 125, 125), boarder, 1)
        boarder = pygame.Rect(((x + 2) * grid_size, 0), (grid_size, grid_size))
        pygame.draw.rect(surface, (200, 200, 200), boarder)
        pygame.draw.rect(surface, (125, 125, 125), boarder, 1)
    for y in range(0, int(height)):
        boarder = pygame.Rect((width - grid_size, y * grid_size), ( grid_size, grid_size))
        pygame.draw.rect(surface, (200, 200, 200), boarder)
        pygame.draw.rect(surface, (125, 125, 125), boarder, 1)
        boarder = pygame.Rect((0, y * grid_size), (grid_size, grid_size))
        pygame.draw.rect(surface, (200, 200, 200), boarder)
        pygame.draw.rect(surface, (125, 125, 125), boarder, 1)
    goal = pygame.Rect((width - 2 * grid_size, height - grid_size), (grid_size, grid_size))
    pygame.draw.rect(surface, (255,255,0), goal)
    

# Grid size parameters
height = 480
width = 480
grid_size = 20
height_grid = int(height / grid_size)
width_grid = int(width / grid_size)

# Possible movements
up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)
up_right = (up[0] + right[0], up[1] + right[1]) 
up_left = (up[0] + left[0], up[1] + left[1]) 
down_right = (down[0] + right[0], down[1] + right[1]) 
down_left = (down[0] + left[0], down[1] + left[1]) 


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    human = Human()
    bombs = []

    for b in range(int(min([height_grid, width_grid]) - 1)):
        bombs.append(Bomb())

    while(True):
        clock.tick(30)
        drawGrid(surface)   

        human.handle_keys()

        for bomb in bombs:
            if human.getPosition() == bomb.getPosition():
                bomb.explode(surface)
                screen.blit(surface, (0, 0))
                pygame.display.update()
                done = True
                sleep(1)
                human.reset()

        human.draw(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()

        if human.getPosition() == ( width - 2 * grid_size, height - grid_size):
            print("You win!")
            sleep(1)
            human.reset()   


main()