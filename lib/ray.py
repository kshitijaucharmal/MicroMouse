import math
import pygame

class Ray:
    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = self.from_angle(math.radians(angle))
        pass

    def from_angle(self, angle):
        a = pygame.Vector2(math.cos(angle), math.sin(angle))
        print(a)
        return a

    def set(self, new_pos):
        self.pos = new_pos
        pass

    def look_at(self, x, y):
        self.dir = pygame.Vector2(x, y) - self.pos
        self.dir = self.dir.normalize()
        pass

    def draw(self, ds):
        pygame.draw.circle(ds, (255, 255, 0), self.pos, 4)
        # pygame.draw.line(ds, (255, 255, 255), self.pos, self.pos + self.dir * 100)
        pass

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        if t > 0 and t < 1 and u > 0:
            pt = pygame.Vector2()
            pt.x = x1 + t * (x2 - x1)
            pt.y = y1 + t * (y2 - y1)
            return pygame.Vector2(pt)
        else:
            return None

    def get_closest_wall(self, walls):
        min_dist = 1000
        closest = None
        for b in walls:
            p = self.cast(b)
            if p:
                dist = self.pos.distance_to(p)
                if dist < min_dist:
                    min_dist = dist
                    closest = p
        return closest

