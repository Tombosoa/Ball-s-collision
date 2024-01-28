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


balls = [Ball(random.randint(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS),
              random.randint(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS),
              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
         for _ in range(NUM_BALLS)]

main_ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()

    main_ball.dx += (mouse_x - main_ball.x) / 300
    main_ball.dy += (mouse_y - main_ball.y) / 300

    for ball in balls:
        distance_to_main_ball = math.sqrt((main_ball.x - ball.x) ** 2 + (main_ball.y - ball.y) ** 2)

        if distance_to_main_ball < 2 * BALL_RADIUS:
            push_direction = math.atan2(main_ball.y - ball.y, main_ball.x - ball.x)
            push_force = min(10, distance_to_main_ball) / 2

            ball.dx += math.cos(push_direction) * push_force
            ball.dy += math.sin(push_direction) * push_force

        for other_ball in balls:
            if ball != other_ball:
                distance = math.sqrt((ball.x - other_ball.x) ** 2 + (ball.y - other_ball.y) ** 2)
                if distance < 2 * BALL_RADIUS:
                    push_direction = math.atan2(ball.y - other_ball.y, ball.x - other_ball.x)
                    push_force = min(10, distance) / 2

                    ball.dx += math.cos(push_direction) * push_force
                    ball.dy += math.sin(push_direction) * push_force

    main_ball.update()

    for ball in balls:
        ball.update()

    screen.fill(BLACK)

    for ball in balls:
        ball.draw(screen)

    main_ball.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
