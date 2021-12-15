import pygame
import sys

class Being(object):
    def __init__(self, grid_size, width, height):
        self.up = (0, -1)
        self.down = (0, 1)
        self.right = (1, 0)
        self.left = (-1, 0)
        self.grid_size = grid_size
        self.width = width
        self.height = height
        self.position = (grid_size, 0)
        self.color = (255, 255, 255)
        self.direction = (0, -1)
        self.home = (grid_size, 0)
        self.energy = 100
        self.status = "home"
    

    def move(self):
        cur = self.getPosition()
        x, y = self.direction
        new = (((cur[0] + (x * self.grid_size)) % self.width), (cur[1] + (y * self.grid_size)) % self.height)
        if new[0] == self.width:
            pass
        elif new[1] == self.height - self.grid_size:
            if new[0] == self.width - self.grid_size:
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

    def getEnergy(self):
        return energy

    def setDirection(self, direction):
        self.direction = direction


    def go_home(self):
        pass

    def feed(self, target):
        pass

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP8:
                    self.direction = self.up
                    self.move()
                elif event.key == pygame.K_KP2:
                    self.direction = self.down
                    self.move()
                elif event.key == pygame.K_KP4:
                    self.direction = self.left
                    self.move()
                elif event.key == pygame.K_KP6:
                    self.direction = self.right
                    self.move()
                    

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (self.grid_size, self.grid_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
