# Задание
# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение,
# и перехватите это исключение при вызове функции.

# class StopRunningNow(Exception):
#     pass
#
#
# def do_stoprun(user_input):
#     if user_input == 3:
#         raise StopRunningNow('STOP HERE!')
#
#
# while True:
#     user_input = int(input('Enter a number'))
#     do_stoprun(user_input)
#
#
# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение,
# вычитание, умножение, деление и возведение в степень.
# Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных
# данных, делении на ноль и возведении нуля в отрицательную степень.

# def add(first, action, second):
#     if action == '+':
#         print(first + second)
#
#
# def minus(first, action, second):
#     if action == '-':
#         print(first - second)
#
#
# def divide(first, action, second):
#     if action == '/':
#         try:
#             first / second
#         except ZeroDivisionError:
#             print('Can not divide by zero!')
#         else:
#             print(x / y)
#
#
# def power(first, action, second):
#     if action == '**':
#         print(first ** second)
#
#
# def multiply(first, action, second):
#     if action == '*':
#         print(first * second)
#
#
# def checker(first, action, second):
#     try:
#         first, action, second
#     except ValueError:
#         print('Wrong input')
#
#
# while True:
#     try:
#         x = int(input('Enter first number: '))
#         z = str(input('Enter an action(/,+,-,**)'))
#         y = int(input('Enter second number: '))
#         add(x, z, y)
#         minus(x, z, y)
#         divide(x, z, y)
#         power(x, z, y)
#         multiply(x, z, y)
#     except (ValueError, NameError):
#         print('Wrong input!')


# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу.
# Конструктор должен генерировать исключение, если заданы неправильные данные.
# Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты после заданного года.

# class Worker:
#     first_name = None
#     last_name = None
#     job_title = None
#     year = None
#
#     def entering(self):
#         self.first_name = input('Enter the first name of worker: ')
#         if not self.first_name:
#             raise ValueError('Field is empty')
#         self.last_name = input('Enter the last name of worker: ')
#         if not self.last_name:
#             raise ValueError('Field is empty')
#         self.job_title = input('Enter workers job title: ')
#         if not self.job_title:
#             raise ValueError('Field is empty')
#         self.year = input('Enter starting year: ')
#         if not self.year:
#             raise ValueError('Field is empty')
#
#
# w1 = Worker()
# w1.entering()
