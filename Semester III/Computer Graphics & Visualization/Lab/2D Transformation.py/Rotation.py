import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Implementation with DDA || Rotation")

# Colors
WHITE = (255, 255, 255)  # White color for initial line
GREEN = (0, 255, 0)      # Green color for rotated line
BLACK = (0, 0, 0)        # Black background

# Function to draw a line using DDA algorithm
def draw_2d(x1, y1, x2, y2, colour):
    x = x1
    y = y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steps = max(dx, dy)
    x_inc = (x2 - x1) / steps
    y_inc = (y2 - y1) / steps

    for _ in range(steps + 1):
        screen.set_at((round(x), round(y)), colour)
        x += x_inc
        y += y_inc


# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        x1, y1 = 350, 350
        x2, y2 = 400, 450
        angle = 60  

        draw_2d(x1, y1, x2, y2, WHITE)  

        t = angle * (math.pi / 180)

        x3 = round(x1 * math.cos(t) - y1 * math.sin(t))
        y3 = round(x1 * math.sin(t) + y1 * math.cos(t))
        x4 = round(x2 * math.cos(t) - y2 * math.sin(t))
        y4 = round(x2 * math.sin(t) + y2 * math.cos(t))

        draw_2d(x3, y3, x4, y4, GREEN)  

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
