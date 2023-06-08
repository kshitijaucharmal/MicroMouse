import pygame

class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.a = pygame.Vector2(x1, y1)
        self.b = pygame.Vector2(x2, y2)
        pass

    def draw(self, ds, color=(255, 255, 255), width=2):
        pygame.draw.line(ds, color, self.a, self.b, width=width)
        pass
