print('Задача 2. Поступление')

# Вася работает разработчиком, и его компания создаёт сайт для образовательной компании. Заказчики попросили реализовать калькулятор баллов ЕГЭ в помощь поступающим. Эту задачу отдали Васе.

# Напишите программу, которая запрашивает у пользователя результаты ЕГЭ по трём экзаменам, и проверяет, поступил ли он на бюджет. Проходной балл равняется 270. Выведите соответствующее сообщение.

# Пример 1:
# Введите количество баллов по русскому языку: 90
# Введите количество баллов по математике: 90
# Введите количество баллов по информатике: 90

# Поздравляю, ты поступил на бюджет!

# Пример 2:
# Введите количество баллов по русскому языку: 100
# Введите количество баллов по математике: 50
# Введите количество баллов по информатике: 70

# К сожалению, ты не прошёл на бюджет.

# Решение
russian_language_score = int(
  input('Введите количество баллов по русскому языку: '))
mathematics_score = int(input('Введите количество баллов по математике: '))
informatics_score = int(input('Введите количество баллов по информатике: '))

sum_score = russian_language_score + mathematics_score + informatics_score

if sum_score <= 269:
  print('К сожалению, ты не прошёл на бюджет.')
else:
  print('Поздравляю, ты поступил на бюджет!')
