import pygame
import random
import sys
import numpy as np
from math import exp

class Snake(object):
    def __init__(self):
        self.legth = 1
        self.positions = [((width / 2), (height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        
        
    def get_head_position(self):
        return self.positions[0]

    
    def getPositions(self):
        return self.positions


    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * grid_size)) % width), (cur[1] + (y * grid_size)) % height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        elif new[0] == width - grid_size:
            self.reset()
        elif new[1] == height - grid_size:
            self.reset()
        elif new[0] == 0:
            self.reset()
        elif new[1] == 0:
            self.reset()
        else:                    
            self.positions.insert(0, new)
            if len(self.positions) > self.legth:
                self.positions.pop()
        


    def reset(self):
        self.legth = 1
        self.positions = [((width / 2), (height / 2))]
        self.direction = random.choice([up, down, left, right])


    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_size, grid_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.direction == down:
                        pass
                    else:
                        self.direction = up
                elif event.key == pygame.K_DOWN:
                    if self.direction == up:
                        pass
                    else:
                        self.direction = down
                elif event.key == pygame.K_LEFT:
                    if self.direction == right:
                        pass
                    else:    
                        self.direction = left
                elif event.key == pygame.K_RIGHT:
                    if self.direction == left:
                        pass
                    else:    
                        self.direction = right
    

class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (233, 163, 49)
        self.randomize_position()


    def getPosition(self):
        return self.position


    def randomize_position(self):
        self.position = (random.randint(1, grid_width - 2) * grid_size, random.randint(1, grid_height - 2) *  grid_size)
        

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.color, r)
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
        boarder = pygame.Rect((width - grid_size, x * grid_size), ( grid_size, grid_size))
        pygame.draw.rect(surface, (200, 200, 200), boarder)
        pygame.draw.rect(surface, (125, 125, 125), boarder, 1)
        boarder = pygame.Rect((0, x * grid_size), ( grid_size, grid_size))
        pygame.draw.rect(surface, (200, 200, 200), boarder)
        pygame.draw.rect(surface, (125, 125, 125), boarder, 1)
    for y in range(0, int(height)):
        boarder = pygame.Rect((y * grid_size, width - grid_size), ( grid_size, grid_size))
        pygame.draw.rect(surface, (200, 200, 200), boarder)
        pygame.draw.rect(surface, (125, 125, 125), boarder, 1)
        boarder = pygame.Rect((y * grid_size, 0), ( grid_size, grid_size))
        pygame.draw.rect(surface, (200, 200, 200), boarder)
        pygame.draw.rect(surface, (125, 125, 125), boarder, 1)

# Grid size parameters
width = 480
height = 480
grid_size = 20
grid_width = height / grid_size
grid_height = width / grid_size

# Possible movements
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    while(True):

        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()

        if snake.get_head_position() == food.position:
            snake.legth += 1
            food.randomize_position()
            while food.getPosition() in snake.getPositions():
                food.randomize_position()

        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        # text = myfont.render("Score {0}".format(score), 1, (0))
        # screen.blit(text, (5, 10))
        pygame.display.update()


main()