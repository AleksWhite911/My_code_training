# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
x = 0
y = 1
c = 0
for _ in range(100):
    point = sd.get_point(x, y)
    v1 = sd.get_vector(point, 0, 100)
    v1.draw()
    next_point = v1.end_point
    v2 = sd.get_vector(next_point, 90, 50)
    v2.draw()
    next_point = v2.end_point
    v3 = sd.get_vector(next_point, 180, 100)
    v3.draw()
    next_point = v3.end_point
    v4 = sd.get_vector(next_point, 270, 50)
    v4.draw()
    x += 100
    if x > 600:
        y += 50
        x = 0
sd.pause()
