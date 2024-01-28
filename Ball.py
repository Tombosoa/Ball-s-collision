import pygame
import sys
import random
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 50
NUM_BALLS = 6

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball")


class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.dx = random.uniform(-5, 5)
        self.dy = random.uniform(-5, 5)
        self.energy = 100

    def update(self):
        self.x += self.dx
        self.y += self.dy

        self.dx *= 0.99
        self.dy *= 0.99

        if self.y - BALL_RADIUS < 0 or self.y + BALL_RADIUS > SCREEN_HEIGHT:
            self.dy = -self.dy

        if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > SCREEN_WIDTH:
            self.dx = -self.dx

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), BALL_RADIUS)

