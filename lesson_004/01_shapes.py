# -*- coding: utf-8 -*-
import simple_draw as sd

start_point_vector = sd.get_point(300, 300)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
def triangle(length, angle, start):
    t1 = sd.get_vector(start_point=start, angle=angle, length=length)
    t1.draw()
    t2 = sd.get_vector(start_point=t1.end_point, angle=angle + 120, length=length)
    t2.draw()
    t3 = sd.get_vector(start_point=t2.end_point, angle=angle + 240, length=length)
    t3.draw()


# triangle(start=start_point_vector, angle=60, length=200)
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции
length_rectangle = 200


def rectangle(length, start, angle=90):
    t1 = sd.get_vector(start_point=start, angle=angle, length=length)
    t1.draw()
    t2 = sd.get_vector(start_point=t1.end_point, angle=angle + 90, length=length)
    t2.draw()
    t3 = sd.get_vector(start_point=t2.end_point, angle=angle + 180, length=length)
    t3.draw()
    t4 = sd.get_vector(start_point=t3.end_point, angle=angle + 270, length=length)
    t4.draw()


# rectangle(start=start_point_vector, length=length_rectangle)


def pentagon(length, start, angle=0):
    t1 = sd.get_vector(start_point=start, angle=angle, length=length)
    t1.draw()
    t2 = sd.get_vector(start_point=t1.end_point, angle=angle + 70, length=length)
    t2.draw()
    t3 = sd.get_vector(start_point=t2.end_point, angle=angle + 140, length=length)
    t3.draw()
    t4 = sd.get_vector(start_point=t3.end_point, angle=angle + 220, length=length)
    t4.draw()
    t5 = sd.get_vector(start_point=t4.end_point, angle=angle + 285, length=length)
    t5.draw()


#pentagon(start=start_point_vector, length=100)

def six(length, start, angle=60):
    t1 = sd.get_vector(start_point=start, angle=angle, length=length)
    t1.draw()
    t2 = sd.get_vector(start_point=t1.end_point, angle=angle + 60, length=length)
    t2.draw()
    t3 = sd.get_vector(start_point=t2.end_point, angle=angle + 120, length=length)
    t3.draw()
    t4 = sd.get_vector(start_point=t3.end_point, angle=angle + 180, length=length)
    t4.draw()
    t5 = sd.get_vector(start_point=t4.end_point, angle=angle + 240, length=length)
    t5.draw()
    t6 = sd.get_vector(start_point=t5.end_point, angle=angle + 300, length=length)
    t6.draw()


six(start=start_point_vector, length=100)


# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# TODO здесь ваш код

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
