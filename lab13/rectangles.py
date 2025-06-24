import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Centered Rectangle')

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

rectangle = (400, 300, 200, 150) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    # Draw the rectangle, inside red, outline black
    pygame.draw.rect(screen, red, rectangle)
    pygame.draw.rect(screen, black, rectangle, 20)

    pygame.display.flip()