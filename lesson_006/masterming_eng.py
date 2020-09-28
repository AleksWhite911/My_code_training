from random import randint

num = ''


# number = '1234'


def make_a_guess_number():
    global num
    num1 = []
    while len(num1) != 4:
        if not num1:
            elem = randint(1, 9)
        else:
            elem = randint(0, 9)
        if elem not in num1:
            num1.append(elem)
        num = ''.join(map(str, num1))
    return num


def check_number(number, num=num):
    slov = {}
    bik = 0
    cows = 0
    for position, elem in enumerate(number):
        if elem == num[position]:
            bik += 1
    for elem1 in number:
        for elem2 in num:
            if elem1 == elem2 and num.index(elem2) != number.index(elem1):
                cows += 1
    slov = {'Коровы': cows, 'Быки': bik}
    return slov


make_a_guess_number()
# check_number(number, num)
