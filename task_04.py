# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random 

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
random.randint(1,125)
a = random.choice(my_favorite_songs)
b = random.choice(my_favorite_songs)
c = random.choice(my_favorite_songs)
# сумма минут всех песен c дробной частью
print('Три выбранные песни звучат', a[1]+b[1]+c[1],'минут')
# сумма минут всех песен c округлением до четного, по правилам Python
print('Три выбранные песни звучат', round(a[1]+b[1]+c[1],0) ,'минут')
