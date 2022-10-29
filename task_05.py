#Задача 5
# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зараплату и составляют expenses руб. в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг, 
# чтобы можно было прожить ближайший год (12 месяцев).
# Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

salary, expenses = 10000, 12000
expens1=12000-10000
expens2=12000*1.03-10000 
_my_credit=expens1+expens2
for i in range(3,13,1):
    expens2 = expens2*1.03
    _my_credit=_my_credit+expens2

print('Необходимо взять в долг', round(_my_credit,2), 'рублей')

# Траты растут ежемесячно по три процента от предыдущей суммы месяца.
# Поэтому реализация выглядит так

salary, expenses = 10000, 12000
i = 0
months_expenses = 0
money_needs = 0

while i < 12:

    if i == 0:
        months_expenses = expenses
    elif i >= 1:
        months_expenses *= 1.03
    i += 1
    difference = round(months_expenses-salary, 2)
    money_needs += difference
    print('Расходы в', i, 'месяце:', difference, ', Итого за', i, 'мес.:', round(money_needs,2))

print('Сотруднику необходимо взять', round(money_needs,2), 'рублей')
