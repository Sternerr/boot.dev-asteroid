import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid"
        else: 
            random_angle = random.uniform(20, 50)

            direction1 = self.velocity.rotate(random_angle) * 1.2
            direction2 = self.velocity.rotate(-random_angle) * 1.2

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = direction1

            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = direction2
