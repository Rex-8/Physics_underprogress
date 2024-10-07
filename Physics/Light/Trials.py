import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Concave Mirror and Light Ray')

def reflect(ray_start, ray_end, mirror_center):
    # Calculate normal at the point of incidence (from mirror center to ray end)
    normal = [ray_end[0] - mirror_center[0], ray_end[1] - mirror_center[1]]
    norm_len = math.sqrt(normal[0]**2 + normal[1]**2)
    normal = [normal[0]/norm_len, normal[1]/norm_len]

    # Calculate the ray direction
    ray_dir = [ray_end[0] - ray_start[0], ray_end[1] - ray_start[1]]
    ray_len = math.sqrt(ray_dir[0]**2 + ray_dir[1]**2)
    ray_dir = [ray_dir[0]/ray_len, ray_dir[1]/ray_len]

    # Calculate the reflection using R = D - 2(D.N)N
    dot = ray_dir[0]*normal[0] + ray_dir[1]*normal[1]
    reflected = [ray_dir[0] - 2*dot*normal[0], ray_dir[1] - 2*dot*normal[1]]

    # Scale the reflected ray for visualization purpose
    scale = 200
    reflected = [reflected[0]*scale, reflected[1]*scale]
    reflected_end = [ray_end[0] + reflected[0], ray_end[1] + reflected[1]]

    return ray_end, reflected_end

mirror_center = (WIDTH // 2, HEIGHT // 2)
mirror_radius = 150
ray_start = [100, HEIGHT // 2]
ray_end = [WIDTH // 2 - 5, HEIGHT // 2]

while True:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if user clicks on start or end of ray
            if abs(event.pos[0] - ray_start[0]) < 10 and abs(event.pos[1] - ray_start[1]) < 10:
                dragging_start = True
            if abs(event.pos[0] - ray_end[0]) < 10 and abs(event.pos[1] - ray_end[1]) < 10:
                dragging_end = True
        if event.type == pygame.MOUSEBUTTONUP:
            dragging_start = False
            dragging_end = False
        if event.type == pygame.MOUSEMOTION:
            if dragging_start:
                ray_start = list(event.pos)
            if dragging_end:
                ray_end = list(event.pos)

    # Draw the concave mirror as a semicircle
    pygame.draw.arc(screen, GRAY, (mirror_center[0] - mirror_radius, mirror_center[1] - mirror_radius, 2*mirror_radius, 2*mirror_radius), math.pi, 2*math.pi, 5)

    # Draw the ray
    pygame.draw.line(screen, RED, ray_start, ray_end, 3)
    pygame.draw.circle(screen, RED, ray_start, 5)
    pygame.draw.circle(screen, RED, ray_end, 5)

    # Draw reflected ray if it intersects with mirror
    reflected_start, reflected_end = reflect(ray_start, ray_end, mirror_center)
    pygame.draw.line(screen, RED, reflected_start, reflected_end, 3)

    pygame.display.flip()
