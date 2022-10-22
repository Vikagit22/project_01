# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

import random
my_time_list=[]
my_time1 = my_favorite_songs['Waste a Moment']
my_time_list.append(my_time1)
my_time1 = my_favorite_songs['New Salvation']
my_time_list.append(my_time1)
my_time1 = my_favorite_songs['Staying\' Alive']
my_time_list.append(my_time1)
my_time1 = my_favorite_songs['Out of Touch']
my_time_list.append(my_time1)
my_time1 = my_favorite_songs['A Sorta Fairytale']
my_time_list.append(my_time1)
my_time1 = my_favorite_songs['Easy']
my_time_list.append(my_time1)
my_time1 = my_favorite_songs['Beautiful Day']
my_time_list.append(my_time1)
my_time1 = my_favorite_songs['Nowhere to Run']
my_time_list.append(my_time1)
my_time1 = my_favorite_songs['In This World']
my_time_list.append(my_time1)

a = random.choice(my_time_list)
b = random.choice(my_time_list)
c = random.choice(my_time_list)

# сумма минут всех песен c дробной частью
print('Три случайно выбранные песни звучат', a+b+c,'минут')
# сумма минут всех песен c округлением до четного, по правилам Python
print('Три случайно выбранные песни звучат', round(a+b+c,0) ,'минут')

