import pygame
from random import randrange

size = 50

width = 16 * size
height = 9 * size 

def RandomPosition():
    return randrange(0, width, size), randrange(0, height, size)

x, y = RandomPosition()
apple = RandomPosition()

dirs = {'up': True, 'down': True, 'left': True, 'right': True}

length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5

pygame.init()

window = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

fontScore = pygame.font.SysFont('Arial', 26, bold=True)

while True:
    window.fill(pygame.Color('black'))
    for coordinate in snake:
        pygame.draw.rect(window, pygame.Color('green'), (coordinate[0], coordinate[1], size-1, size-1))
    pygame.draw.rect(window, pygame.Color('red'), (apple[0], apple[1], size, size))

    renderScore = fontScore.render('Очки: ' + str(length-1), 1, pygame.Color('Orange'))
    window.blit(renderScore, (5, 5))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dirs['up']:
        dx, dy = 0, -1
        dirs = {'up': True, 'down': False, 'left': True, 'right': True}
    if keys[pygame.K_DOWN] and dirs['down']:
        dx, dy = 0, 1
        dirs = {'up': False, 'down': True, 'left': True, 'right': True}
    if keys[pygame.K_LEFT] and dirs['left']:
        dx, dy = -1, 0
        dirs = {'up': True, 'down': True, 'left': True, 'right': False}
    if keys[pygame.K_RIGHT] and dirs['right']:
        dx, dy = 1, 0
        dirs = {'up': True, 'down': True, 'left': False, 'right': True}

    x += dx * size
    y += dy * size

    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = RandomPosition()
        length += 1
        fps += 1
    print(x, y)
    if x < 0 or x > width-size or y < 0 or y > height-size or len(snake) != len(set(snake)):
        x, y = RandomPosition()
        apple = RandomPosition()
        dirs = {'up': True, 'down': True, 'left': True, 'right': True}
        length = 1
        snake = [(x, y)]
        dx, dy = 0, 0
        fps = 5

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
