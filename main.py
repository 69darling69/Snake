import pygame
from random import randrange

# Размер квадратов
size = 50

# Ширина и высота поля
width = 16 * size
height = 9 * size 

# Возвращает случайное положение на поле
def RandomPosition():
    return randrange(0, width, size), randrange(0, height, size)

# Положение змейки (сначала случайно)
x, y = RandomPosition()
# Положение яблока (сначала случайно)
apple = RandomPosition()

# Словарь куда можно двигаться
dirs = {'up': True, 'down': True, 'left': True, 'right': True}

# Длина змейки, изначально 1
length = 1
# Список всех мест, где была змейка
snake = [(x, y)]
# Наше движение, dx - лево и право, dy - верх и низ
dx, dy = 0, 0
# Количество кадров в секунду
fps = 5

# Инициализируем pygame для его правильной работы
pygame.init()

# Создаем окно, где и будет происходить игра
window = pygame.display.set_mode([width, height])
# Создаем часы, чтобы ограничить частоту кадров. Если это не сделать, то игра будет работыть слишком быстро
clock = pygame.time.Clock()

# Шрифт для очков
fontScore = pygame.font.SysFont('Arial', 26, bold=True)

# Работаем в бесконечном цикле игры
while True:
    # Заполняем фон черным цветом
    window.fill(pygame.Color('black'))
    # Проходимся по всему списку змейки
    for coordinate in snake:
        # Рисуем прямоугольники по координатам змейки и заданному размеру
        pygame.draw.rect(window, pygame.Color('green'), (coordinate[0], coordinate[1], size, size))
    pygame.draw.rect(window, pygame.Color('red'), (apple[0], apple[1], size, size))

    # Рисуем очки
    renderScore = fontScore.render('Очки: ' + str(length-1), 1, pygame.Color('Orange'))
    window.blit(renderScore, (5, 5))

    # Получаем все нажатые на данный момент кнопки
    keys = pygame.key.get_pressed()
    # Изменяем направление змейки по кнопкам, если в эту сторону можно двигать и меняем разрешенные направления
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

    # Перемещаем нашу змеку на dx и dy
    x += dx * size
    y += dy * size

    # Добавляем эту клетку, чтобы рисовать в ней змейку
    snake.append((x, y))
    snake = snake[-length:]

    # Если голова змейки совпадает с яблоком
    if snake[-1] == apple:
        # То ставим яблоко в другое случайное место
        apple = RandomPosition()
        # Увеличиваем длину
        length += 1
        # И количество кадров в секунду -> скорость игры
        fps += 1

    # Если мы вышли за рамки игрового поля или eсли длина змейки не равна длине множества змейки (т.е. какая-то ячейка змейки повторилась дважды)
    if x < 0 - size or x > width or y < 0 - size or y > height or len(snake) != len(set(snake)):
        # Проигрыш
        # Рендерим надпись
        renderEnd = fontScore.render('ИГРА ОКОНЧЕНА', 1, pygame.Color('orange'))
        # Выводим ее по центру
        window.blit(renderEnd, (width//2-renderEnd.get_size()[0]//2, height//2-renderEnd.get_size()[1]//2))
        # Обновляем экран
        pygame.display.flip()
        # Проходимся в цикле по всем событиям, которые произошли в этот кадр
        for event in pygame.event.get():
        # Если есть событие с типом "выйти"
            if event.type == pygame.QUIT:
                # Выйти из игры
                exit()

    # Обновляем окно
    pygame.display.flip()
    # Устанавливаем количество кадров в секунду
    clock.tick(fps)

    # Проходимся в цикле по всем событиям, которые произошли в этот кадр
    for event in pygame.event.get():
        # Если есть событие с типом "выйти"
        if event.type == pygame.QUIT:
            # Выйти из игры
            exit()
