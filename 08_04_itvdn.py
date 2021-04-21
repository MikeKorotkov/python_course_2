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
#     user_input = int(input('Enter a number: '))
#     try:
#         do_stoprun(user_input)
#     except StopRunningNow:
#         print('Choose another number!')

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
#             print(first/ second)
#
#
# def power(first, action, second):
#     if action == '**':
#         if first == 0 and second < 0:
#             try:
#                 first ** second
#             except ZeroDivisionError:
#                 print('Zero can not be raised to a negative power!')
#             else:
#                 print(first**second)
#
#
# def multiply(first, action, second):
#     if action == '*':
#         print(first * second)
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

def output_worker():
    enter_year = str(input('Enter the year you want to see workers from: '))
    if w1.year == enter_year:
        print(w1.first_name, w1.last_name, 'was hired this year')
    if w2.year == enter_year:
        print(w2.first_name, w2.last_name, 'was hired this year')
    if w3.year == enter_year:
        print(w3.first_name, w3.last_name, 'was hired this year')


class Worker:
    first_name = None
    last_name = None
    job_title = None
    year = None

    def entering(self):
        self.first_name = input('Enter the first name of worker: ')
        if not self.first_name:
            raise ValueError('Field is empty')
        self.last_name = input('Enter the last name of worker: ')
        if not self.last_name:
            raise ValueError('Field is empty')
        self.job_title = input('Enter workers job title: ')
        if not self.job_title:
            raise ValueError('Field is empty')
        self.year = input('Enter starting year: ')
        if not self.year:
            raise ValueError('Field is empty')


while True:
    try:
        w1 = Worker()
        w1.entering()
        w2 = Worker()
        w2.entering()
        w3 = Worker()
        w3.entering()
    except (ValueError,NameError):
        print('Field is empty!')
    else:
        output_worker()
        print()
