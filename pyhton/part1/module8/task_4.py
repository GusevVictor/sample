print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

# Решение
a = int(input('Введите число "а": '))
b = int(input('Введите число "b": '))
c = int(input('Введите число "c": '))
sum, count_number = 0, 0

for number in range(a, b):
  if number % c == 0:
    sum += number
    count_number += 1

print(
  f'Среднее арифметическое всех чисел из отрезка {a, b} кратное {c}, равно {sum / count_number}'
)
