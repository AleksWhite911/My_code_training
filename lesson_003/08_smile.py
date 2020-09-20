# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile(x, y, color=COLOR_YELLOW):
    point = sd.get_point(x, y)
    sd.circle(point, color=color)
    point_eye_x = x - 20
    point_eye_y = y + 10
    next_point = sd.get_point(point_eye_x, point_eye_y)
    sd.circle(next_point, radius=10, color=color)
    point_eye_x = x + 20
    next_point = sd.get_point(point_eye_x, point_eye_y)
    sd.circle(next_point, radius=10, color=color)
    next_point_mouth = sd.get_point(point_eye_x - 46, point_eye_y - 25)
    v1 = sd.get_vector(next_point_mouth, angle=320, length=20)
    v1.draw(color)
    next_point_mouth = v1.end_point
    v2 = sd.get_vector(next_point_mouth, angle=0, length=20)
    v2.draw(color)
    next_point_mouth = v2.end_point
    v3 = sd.get_vector(next_point_mouth, angle=40, length=20)
    v3.draw(color)


smile(100, 100, color=COLOR_RED)
smile(200, 200, color=COLOR_PURPLE)
smile(300, 300, color=COLOR_PURPLE)
smile(450, 470, color=COLOR_PURPLE)
sd.pause()
