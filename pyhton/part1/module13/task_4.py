print('Задача 4. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста. В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код согласно следующим условиям: программа получает на вход два числа; в первом числе должно быть не менее трёх цифр, во втором — не менее четырёх, иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.

# И тут вы натыкаетесь на программу, которая была написана предыдущим программистом и которая как раз решает такую задачу. Однако старший программист попросил вас немного переписать этот код, чтобы он не выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.

# Постарайтесь разделить логику кода на три отдельные логические части (функции):
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).

# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.


# Решение
def main():
  first_number = int(input("Введите первое число (не менее 3х цифр): "))
  second_number = int(input("Введите второе число (не менее 4х цифр): "))
  numbers = first_number, second_number
  count, summa_of_reversed_numbers = 0, 0
  for number in numbers:
    count += 1
    check_number = count_digit_in_number(number)

    if (count == 1 and check_number >= 3) or (count == 2
                                              and check_number >= 4):
      summa_of_reversed_numbers += get_reverse_first_and_last_digit_of_number(
        number)
    else:
      return print(f'Введены не правильные числа!\n'
                   f'Число {number} не подходит под условия задачи!')

  print(f'Сумма измененных чисел равна: {summa_of_reversed_numbers}')


def count_digit_in_number(input_number):
  return len(str(input_number))


def get_reverse_first_and_last_digit_of_number(number_for_reverse):
  number_for_reverse = str(number_for_reverse)
  return int(number_for_reverse[-1] + number_for_reverse[1:-1] +
             number_for_reverse[0])


main()