# random.randint()
# 2. Создать класс "воин". Здоровье в 100 очков. В случайном порядке они
# бьют друг друга. Тот, кто бьет, здоровья не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал,
# и сколько у противника осталось здоровья. Как только у кого-то
# заканчивается ресурс здоровья, программа завершается сообщением о
# том, кто одержал победу.

# from random import randint
#
#
# class Warrior:
#     def __init__(self, health):
#         self.health = health
#
#     def hit(self, target, target1):
#         if target.health > 0:
#             target.health -= 20
#             if target1 == warrior1:
#                 target1 = "Warrior1"
#                 print(target1, " has attacked")
#                 print("Warrior2 has", target.health, "hp left")
#
#             if target1 == warrior2:
#                 target = warrior1
#                 target1 = "Warrior2"
#                 print(target1, " has attacked")
#                 print('Warrior1 has', target.health, "hp left")
#         if target.health == 0:
#             print(target1, " has won!")
#
#
# warrior1 = Warrior(100)
# warrior2 = Warrior(100)
#
# exiter = input('Press "Enter" to start a fight or type "quit" to exit: ')
#
# while exiter != 'quit':
#     if exiter == '':
#         num = randint(1, 2)
#         if num == 1:
#             warrior1.hit(warrior2, warrior1)
#             exiter = input('Press "Enter" to continue or type "quit" if someone has won: ')
#
#         elif num == 2:
#             warrior2.hit(warrior1, warrior2)
#             exiter = input('Press "Enter" to continue or type "quit" if someone has won: ')

# 1. Создать рабочего. У который может ходить на работу.
# Рабочий должен иметь возраст и имя.
# Так же принимать решение идти на работу или нет, в зависимости от того,
# какой ему передали номер дня


# class Worker:
#     name = 'Steven'
#     age = 33
#     day = int(input('Enter weekday number: '))
#
#     def work(self):
#         if self.day == 1 or 2 or 3 or 4 or 5:
#             print(w1.name, 'is working...')
#         else:
#             print(w1.name, 'is not working...')
#
#
# w1 = Worker()
#
#
# w1.work()


# 3. Есть Алфавит, характеристиками которого являются:
# - Язык
# - Список букв
#
# Для Алфавита можно:
# - Напечатать все буквы алфавита
# - Посчитать количество букв

# class Alphabet:
#     language = 'Russian'
#     letters_list = 'А,Б,В,Г,Д,Е,Ё,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я'
#     pure_letter_list = []
#
#     def print_letter_list(self):
#         print(self.letters_list)
#
#     def count_letters(self):
#         for item in self.letters_list:
#             if item != ',':
#                 self.pure_letter_list.append(item)
#         count = len(self.pure_letter_list)
#         print('There are', count, 'letters in this alphabet')
#
#
# rus = Alphabet()
#
# rus.print_letter_list()
# rus.count_letters()
