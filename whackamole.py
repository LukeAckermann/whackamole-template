import pygame
import random

pygame.init()

width, height = 640, 512
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Whack-a-Mole')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mole_image = pygame.image.load('mole.png')
mole_image = pygame.transform.scale(mole_image, (32, 32))

mole_x, mole_y = 0, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(mole_x, mole_x + 32) and event.pos[1] in range(mole_y, mole_y + 32):
                mole_x = random.randrange(0, width, 32)
                mole_y = random.randrange(0, height, 32)

    screen.fill(WHITE)

    for x in range(0, width, 32):
        pygame.draw.line(screen, BLACK, (x, 0), (x, height))
    for y in range(0, height, 32):
        pygame.draw.line(screen, BLACK, (0, y), (width, y))

    screen.blit(mole_image, (mole_x, mole_y))

    pygame.display.flip()

pygame.quit()
