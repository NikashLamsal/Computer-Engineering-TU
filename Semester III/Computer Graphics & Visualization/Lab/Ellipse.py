import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid-Point Ellipse Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_ellipse_algorithm(xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = (ry**2) - (rx**2 * ry) + (0.25 * (rx**2))
    dx = 2 * (ry**2) * x
    dy = 2 * (rx**2) * y
    
    # First region: 
    while dx <= dy:
        screen.set_at((round(x + xc), round(y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(y + yc)), WHITE)
        screen.set_at((round(x + xc), round(-y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(-y + yc)), WHITE)
        
        if p1 < 0:
            x += 1
            dx = 2 * (ry**2) * x
            p1 += dx + (ry**2)
        else:
            x += 1
            y -= 1
            dx = 2 * (ry**2) * x
            dy = 2 * (rx**2) * y
            p1 += dx - dy + (ry**2)

    p2 = (ry**2) * (x + 0.5)**2 + (rx**2) * (y - 1)**2 - (rx**2) * (ry**2)
    
    # Second region: 
    while y > 0:
        screen.set_at((round(x + xc), round(y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(y + yc)), WHITE)
        screen.set_at((round(x + xc), round(-y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(-y + yc)), WHITE)  
        # Update the decision parameter
        if p2 > 0:
            y -= 1
            dy = 2 * (rx**2) * y
            p2 -= dy + (rx**2)
        else:
            x += 1
            y -= 1
            dx = 2 * (ry**2) * x
            dy = 2 * (rx**2) * y
            p2 += dx - dy + (rx**2)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()       
        screen.fill(BLACK)
        draw_ellipse_algorithm(400, 300, 150, 100)  
        draw_ellipse_algorithm(400,300,350,300)
        pygame.display.flip()

if __name__ == "__main__":
    main()