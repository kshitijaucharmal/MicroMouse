import pygame
from wall import Wall

class Cell:
    def __init__(self, i, j, size):
        self.i = i
        self.j = j
        self.size = size

        x = self.i * self.size
        y = self.j * self.size
        w = self.size

        self.top_w = Wall(x, y, x + w, y)
        self.right_w = Wall(x + w, y, x + w, y + w)

        self.visited = False

        self.visitedColor = (51, 51, 51)
        pass

    def draw(self, ds):
        if self.top_w:
            self.top_w.draw(ds)
        if self.right_w:
            self.right_w.draw(ds)
        pass

    def highlight(self, ds):
        x = self.i * self.size
        y = self.j * self.size
        w = self.size
        WHITE = (255, 255, 255)
        pygame.draw.rect(ds, WHITE, (x, y, w, w))

