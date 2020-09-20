# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile(x, y):
    point = sd.get_point(x, y)
    sd.circle(point)
    point_eye_x = x - 20
    point_eye_y = y + 10
    next_point = sd.get_point(point_eye_x, point_eye_y)
    sd.circle(next_point, radius=10)
    point_eye_x = x + 20
    next_point = sd.get_point(point_eye_x, point_eye_y)
    sd.circle(next_point, radius=10)
    next_point_mouth = sd.get_point(point_eye_x - 46, point_eye_y - 25)
    v1 = sd.get_vector(next_point_mouth, angle=320, length=20)
    v1.draw()
    next_point_mouth = v1.end_point
    v2 = sd.get_vector(next_point_mouth, angle=0, length=20)
    v2.draw()
    next_point_mouth = v2.end_point
    v3 = sd.get_vector(next_point_mouth, angle=40, length=20)
    v3.draw()


smile(100, 100)
smile(200, 200)
smile(300, 300)
smile(450, 470)
sd.pause()
