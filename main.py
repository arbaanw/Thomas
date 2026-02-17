import pygame
import math
from collections import deque

#initialization
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Thomas")
clock = pygame.time.Clock()
running = True
background_color = pygame.Color(31, 30, 30)
circle_x_position = 0
circle_y_position = 0
path = deque()
path.append(pygame.mouse.get_pos())
tail_length = 5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    
    #math & logic
    mouse_position = pygame.mouse.get_pos()
    circle_x_position,circle_y_position = mouse_position

    if len(path) > tail_length:
        path.popleft()
    path.append(mouse_position)
    print(path)

    #drawing
    pygame.draw.lines(screen, 'blue', False, path, 12)
    pygame.draw.circle(screen, 'red', (circle_x_position, circle_y_position), 30, width = 5)
    pygame.draw.circle(screen, 'white', (circle_x_position, circle_y_position), 12, width = 0)

    pygame.display.flip()


    clock.tick(60)

pygame.quit()
