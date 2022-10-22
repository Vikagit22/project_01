# Задача 7
# Есть словарь кодов товаров

titles = {
    'Кроссовки тип 3 - Adidas': '100000110',
    'Мячик тип 2 - Adidas': '100000146',
    'Кепка тип 1 - Adidas': '100000149',
    'Ремень тип 2 - Nike': '100000194',
    'Футболка тип 1 - Adidas': '100000224',
    'Шапка тип 5 - Puma': '100000280',
}

#  Есть словарь списков словарей количества товаров на складе.

sales = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:

# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

# Есть словарь списков количества товаров на складе.

my_art1=titles['Кроссовки тип 3 - Adidas']
sales[my_art1]
quantity = 0
for dict in sales[my_art1]:
    quantity += dict['quantity'] 
    price = 0
for dict in sales[my_art1]:
    price += dict['price']
print(f'Кроссовки тип 3 - Adidas - {quantity} шт, стоимость {price} руб')
my_art1=titles['Мячик тип 2 - Adidas']
sales[my_art1]
quantity = 0
for dict in sales[my_art1]:
    quantity += dict['quantity'] 
    price = 0
for dict in sales[my_art1]:
    price += dict['price']
print(f'Мячик тип 2 - Adidas - {quantity} шт, стоимость {price} руб')
my_art1=titles['Кепка тип 1 - Adidas']
sales[my_art1]
quantity = 0
for dict in sales[my_art1]:
    quantity += dict['quantity'] 
    price = 0
for dict in sales[my_art1]:
    price += dict['price']
print(f'Кепка тип 1 - Adidas - {quantity} шт, стоимость {price} руб')
my_art1=titles['Ремень тип 2 - Nike']
sales[my_art1]
quantity = 0
for dict in sales[my_art1]:
    quantity += dict['quantity'] 
    price = 0
for dict in sales[my_art1]:
    price += dict['price']
print(f'Ремень тип 2 - Nike - {quantity} шт, стоимость {price} руб')
my_art1=titles['Футболка тип 1 - Adidas']
sales[my_art1]
quantity = 0
for dict in sales[my_art1]:
    quantity += dict['quantity'] 
    price = 0
for dict in sales[my_art1]:
    price += dict['price']
print(f'Футболка тип 1 - Adidas - {quantity} шт, стоимость {price} руб')
my_art1=titles['Шапка тип 5 - Puma']
sales[my_art1]
quantity = 0
for dict in sales[my_art1]:
    quantity += dict['quantity'] 
    price = 0
for dict in sales[my_art1]:
    price += dict['price']
print(f'Шапка тип 5 - Puma - {quantity} шт, стоимость {price} руб')