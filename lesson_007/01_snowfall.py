# -*- coding: utf-8 -*-

import simple_draw as sd
import random


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, cord_x, cord_y, len_snow):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.len_snow = len_snow

    def draw(self):
        point = sd.get_point(self.cord_x, self.cord_y)
        sd.snowflake(center=point, length=self.len_snow)

    def clear_previous_picture(self):
        sd.clear_screen()

    def move(self):
        if self.cord_y > 0:
            self.cord_y -= 10
        else:
            pass

    def can_fall(self):
        if self.cord_y >= 0:
            return True


def get_flakes(count):
    flakes = []
    while count != 0:
        flakes.append(Snowflake(random.randint(0, 500), random.randint(300, 500), 20))
        count -= 1
    return flakes


def get_fallen_flakes():
    fallen_flakes = 0
    for flake in flakes:
        if flake.cord_y <= 0:
            fallen_flakes += 1
    return fallen_flakes


def append_flakes(count):
    while count != 0:
        flakes.append(Snowflake(random.randint(0, 500), random.randint(300, 500), 20))
        count -= 1
        return flakes

# flake = Snowflake(150, 500, 20)

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=10)  # создать список снежинок
print(flakes)
past_count = 0
while True:
    sd.clear_screen()
    for flake in flakes:
        flake.move()
        flake.draw()
        fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
        if fallen_flakes > past_count:
            append_flakes(count=fallen_flakes)
            past_count = fallen_flakes
        sd.sleep(0.03)
    if sd.user_want_exit():
        break

sd.pause()
