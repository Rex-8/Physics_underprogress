import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
SPRING_COLOR = (0, 0, 0)
PATH_COLOR = (200, 0, 0)
SPRING_START_POS = (WIDTH // 2, HEIGHT // 2)
K = 0  # Spring constant
M = 10  # Mass of the end point
DT = 1/60.0  # Time step
G = 1  # Gravitational acceleration (scaled for our simulation)

# Setup display and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spring System with Dynamics, Gravity and Path')
clock = pygame.time.Clock()

# Variables
dragging = False
pos = [WIDTH // 2 + 10, HEIGHT // 2+10]
dragged_pos = [WIDTH // 2 + 15, HEIGHT // 2 + 15]
velocity = [0, 0]
path_points = []  # List to store the path points

def draw_spring():
    pygame.draw.line(screen, SPRING_COLOR, SPRING_START_POS, dragged_pos, 2)

def draw_path():
    for point in path_points:
        pygame.draw.circle(screen, PATH_COLOR, (int(point[0]), int(point[1])), 2)

def apply_physics():
    global velocity, dragged_pos

    # Calculate displacement from equilibrium
    dx = dragged_pos[0] - pos[0]
    dy = dragged_pos[1] - pos[1]

    # Hooke's Law to determine spring force
    fx = -K * dx
    fy = -K * dy

    # Gravitational force
    fy += M * G

    # Newton's second law to update velocity
    velocity[0] += fx / M * DT
    velocity[1] += fy / M * DT

    # Update dragged position
    dragged_pos[0] += velocity[0]
    dragged_pos[1] += velocity[1]

    # Store the position in path_points
    path_points.append((dragged_pos[0], dragged_pos[1]))

def main():
    global dragging, dragged_pos

    while True:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                distance = ((mx - dragged_pos[0])**2 + (my - dragged_pos[1])**2)**0.5
                if distance < 20:  # If mouse click is close enough to the end of the spring
                    dragging = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False

        if dragging:
            dragged_pos = list(pygame.mouse.get_pos())
            velocity = [0, 0]  # Reset velocity when dragging
            path_points.clear()  # Clear the path when dragging starts
        else:
            apply_physics()

        draw_path()  # Draw the path before the spring for visual clarity
        draw_spring()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
