# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month = 10
money = 0
summ = 0
percent = 0
while month > 0:
    if month == 10:
        money = expenses - educational_grant
        summ += money
        month -= 1
    elif month <= 9:
        percent = (expenses / 100) * 3
        expenses = expenses + percent
        money = expenses - educational_grant
        summ += money
        month -= 1
print(summ)
