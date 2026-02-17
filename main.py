import pygame
import math

#initialization
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Thomas")
clock = pygame.time.Clock()
running = True
background_color = pygame.Color(31, 30, 30)
circle_x_position = 0
circle_y_position = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    
    #math & logic
    theta = math.atan2(circle_y_position - pygame.mouse.get_pos()[1], circle_x_position - pygame.mouse.get_pos()[0] )
    deg = math.degrees(theta)
    print(deg)
    mouse_position = pygame.mouse.get_pos()
    circle_x_position,circle_y_position = mouse_position

    #drawing
    pygame.draw.polygon(screen, 'blue', ((circle_x_position + 100*math.cos(theta), circle_y_position + 100*math.sin(theta)), (circle_x_position + 12*math.cos(theta+1.5708), circle_y_position + 12*math.sin(theta+1.5708)), (circle_x_position + 12*math.cos(theta+4.71239), circle_y_position + 12*math.sin(theta+4.71239))), width = 0)
    pygame.draw.circle(screen, 'red', (circle_x_position, circle_y_position), 30, width = 5)
    pygame.draw.circle(screen, 'white', (circle_x_position, circle_y_position), 12, width = 0)

    pygame.display.flip()


    clock.tick(48)

pygame.quit()
