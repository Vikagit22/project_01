# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек

# решение задания №2  предложены три варианта ответа на первый из вопросов залания
my_cities=['МОСКВА', 'КАЗАНЬ', 'УФА']
my_popul= [['МОСКВА',12000000], ['КАЗАНЬ', 1400000], ['УФА',1100000]]

# вариант с явным написанием города с изменеием падежа, как указано в задании 
print('Население Казани','-', my_popul[1][1], 'человек')
# мой вариант ответа №1
print('Население города',my_cities[1], '-', my_popul[1][1], 'человек')
# мой вариант ответа №2
print('Население города',my_popul[1][0], '-', my_popul[1][1], 'человек')
# итоговый вывод суммы
print('Итого размер населения','-', my_popul[0][1]+my_popul[1][1]+my_popul[2][1], 'человек')
