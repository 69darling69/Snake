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

# Работаем в бесконечном цикле игры
while True:
    # Заполняем фон черным цветом
    window.fill(pygame.Color('black'))
    # Проходимся по всему списку змейки
    for coordinate in snake:
        # Рисуем прямоугольники по координатам змейки и заданному размеру
        pygame.draw.rect(window, pygame.Color('green'), (coordinate[0], coordinate[1], size, size))
    pygame.draw.rect(window, pygame.Color('red'), (apple[0], apple[1], size, size))

    # Получаем все нажатые на данный момент кнопки
    keys = pygame.key.get_pressed()
    # Изменяем направление змейки по кнопкам
    if keys[pygame.K_UP]:
        dx, dy = 0, -1
    if keys[pygame.K_DOWN]:
        dx, dy = 0, 1
    if keys[pygame.K_LEFT]:
        dx, dy = -1, 0
    if keys[pygame.K_RIGHT]:
        dx, dy = 1, 0

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

    # Если мы вышли за рамки игрового поля
    if x < 0 - size or x > width or y < 0 - size or y > height:
        # Выход
        break
    # Если длина змейки не равна длине множества змейки (т.е. какая-то ячейка змейки повторилась дважды)
    if len(snake) != len(set(snake)):
        # Выход
        break

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
