print('Задача 5. Вася хочет выигрывать')

# Вася вдохновился фильмом «Двадцать одно» и решил изучить математику игровых автоматов. Для анализа данных ему нужна информация о том, как часто в автомате выпадает три или две одинаковых картинки. Для сбора данных нужна программа, проверяющая это равенство. 

# Даны три целых числа. Определите, сколько среди них совпадающих. 
# Программа должна вывести один из вариантов: 
# 1) 3 (если все совпадают) 
# 2) 2 (если два совпадают)
# 3) 0 (если все числа разные)

# Решение
first_integer = int(input('Введите первое целое число: '))
second_integer = int(input('Введите второе целое число: '))
third_integer = int(input('Введите третье целое число: '))

if first_integer == second_integer == third_integer:
  print ('3')
elif (first_integer == second_integer) or (first_integer == third_integer) or (second_integer == third_integer):
  print ('2')
else:
  print('0')
  