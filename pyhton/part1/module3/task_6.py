print('Задача 6. Проверяем бухгалтера')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

# Решение
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

a1 = (a % 10)
a2 = (a // 10 % 10)
a = str(a2) + str(a1)

b1 = (b % 10)
b2 = (b // 10 % 10)

a = str(a2) + str(a1)
b = str(b2) + str(b1)

print('Сумма:', int(a) + int(b))
