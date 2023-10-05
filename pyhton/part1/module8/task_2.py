print('Задача 2. Долги')

# «МирПрогБанк» наконец-то разделил законопослушных граждан и должников и поместил их в разные базы. Но банк не торопится сильно давить на неплательщиков. Операторам банка дали задание позвонить каждому пятому должнику из списка (нумерация начинается с нуля) и уточнить, какую сумму каждый из них задолжал банку.

# Напишите программу, которая получает данные о количестве должников, а затем спрашивает у каждого пятого (начиная с нуля) его долг. В конце выводится общая сумма долгов.

# Пример 1
# Введите количество должников: 13
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Должник с номером 10
# Сколько должны? 2000
# Общая сумма долга: 8000

# Пример 2
# Введите количество должников: 10
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Общая сумма долга: 6000

# Решение
count_of_debtors = int(input('Введите количество должников: '))
total_debt = 0

for debtor_number in range(0, count_of_debtors, 5):
  print(f'Должник с номером {debtor_number}')
  sum_of_debt = int(input('Сколько должны? '))
  total_debt += sum_of_debt
print(f'Общая сумма долга: {total_debt}')