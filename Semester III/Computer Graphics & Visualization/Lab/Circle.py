import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid-point Circle Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_circle_algorithm(x, y, r):
    X = 0
    Y = r
    d = 1 - r

    while X <= Y:
        # Plot all the symmetric points
        screen.set_at((round(X + x), round(Y + y)), WHITE) 
        screen.set_at((round(-X + x), round(Y + y)), WHITE) 
        screen.set_at((round(X + x), round(-Y + y)), WHITE) 
        screen.set_at((round(-X + x), round(-Y + y)), WHITE) 
        screen.set_at((round(Y + x), round(X + y)), WHITE) 
        screen.set_at((round(-Y + x), round(X + y)), WHITE) 
        screen.set_at((round(Y + x), round(-X + y)), WHITE) 
        screen.set_at((round(-Y + x), round(-X + y)), WHITE)

        X = X + 1
        if d < 0:
            d = d + 2 * X + 1
        else:
            d = d + 2 * X - 2 * Y + 1
            Y = Y - 1

# Main function
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)  # Clear the screen
        draw_circle_algorithm(200, 300, 100)  # Draw the circle
        pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()
