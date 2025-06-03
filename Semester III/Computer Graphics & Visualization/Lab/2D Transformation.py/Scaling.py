import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Implementation with DDA || Scaling")

# Colors
WHITE = (255, 255, 255)  # White color for initial line
GREEN = (0, 255, 0)      # Green color for scaled line
BLACK = (0, 0, 0)        # Black background

def draw_2d(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)
    
    x = x1
    y = y1
    
    for _ in range(steps):
        pygame.draw.circle(screen, color, (int(x), int(y)), 1)  # Draw pixel
        x += x_increment
        y += y_increment

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)
        
        # Initial coordinates of the line
        x1, y1 = 100, 100
        x2, y2 = 100, 300  
        
       
        sx, sy = 2, 2  # Scaling factors
        
        # Draw the initial line
        draw_2d(x1, y1, x2, y2, WHITE)  # Initial line in white
        
        # Calculate scaled coordinates
        x3 = x1 * sx
        y3 = y1 * sy
        x4 = x2 * sx
        y4 = y2 * sy
        
        # Draw the scaled line
        draw_2d(x3, y3, x4, y4, GREEN)  # Scaled line in green

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()