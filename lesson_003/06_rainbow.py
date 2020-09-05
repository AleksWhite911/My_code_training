# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start = sd.get_point(50, 50)
y = 0
c = 50
d = 350
for x in range(0, 7):
    color = rainbow_colors[y]
    angle = sd.get_point(d, 450)
    start = sd.get_point(c, 50)
    sd.line(start_point=start, end_point=angle, width=3, color=color)
    y += 1
    c += 5
    d += 5
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
