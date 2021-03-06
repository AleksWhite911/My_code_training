#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42
print (3.1415926 * 42 ** 2)
# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()


# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у
check = (((23 ** 2) + (34 ** 2)) ** 0.5)
print (check < 42)
# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

# Аналогично для другой точки
point_2 = (30, 30)
check1 = (((30 ** 2) + (30 ** 2)) ** 0.5)
print (check1 < 42)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


