import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            self.random_angle = random.uniform(20, 50)
            self.new_vector1 = self.velocity.rotate(self.random_angle)
            self.new_vector2 = self.velocity.rotate(-self.random_angle)
            self.new_radius = self.radius / 2
            self.new_asteroid1 = Asteroid(self.position.x, self.position.y, self.new_radius)
            self.new_asteroid2 = Asteroid(self.position.x, self.position.y, self.new_radius)
            self.new_asteroid1.velocity = self.new_vector1 * 1.2
            self.new_asteroid2.velocity = self.new_vector2 * 1.2
