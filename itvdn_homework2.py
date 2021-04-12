# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document.
# Пусть метод edit_document выводит на экран информацию о том,
# что редактирование документов недоступно для бесплатной версии.
# Создайте подкласс ProEditor, в котором данный метод будет переопределён. Введите с клавиатуры лицензионный ключ и,
# если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
# Вызовите методы просмотра и редактирования документов.

# class Editor:
#
#     def edit_document(self):
#         print('Document change is available only for pro`s!')
#
#     def view_document(self):
#         print('You have a regular document')
#
#
# class ProEditor(Editor):
#     l_key = 12345
#
#     def edit_document(self):
#         self.trying = int(input('Enter a licence key: '))
#
#     def view_document(self):
#         print('You have a pro document')
#
#
# quitter = ''
# while quitter != 'pro':
#     doc1 = Editor()
#     doc1.view_document()
#     doc1.edit_document()
#     code = input('Press Enter to buy a pro version:')
#     if code == '':
#         doc2 = ProEditor()
#         doc2.edit_document()
#         if doc2.trying == doc2.l_key:
#             doc2.view_document()
#             quitter = 'pro'
#         else:
#             print('Wrong license key!')

# Задание 2
# Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши.
# Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку.

# class GraphicObj:
#     def mouse_press(self):
#         self.mouse_press()
#         print('The mouse was pressed')
#
#
# class Rectangle(GraphicObj):
#     sides = 4
#
#
# class MousePressObj(GraphicObj):
#     def mouse_is_pressed(self):
#         pass
#
#
# class Button:
#     def button_press(self):
#         print('Button was pressed')
#
#
# obj1 = Button()
# obj2 = Rectangle()
# obj1.button_press()

# Создайте иерархию классов с использованием множественного наследования.
# Выведите на экран порядок разрешения методов для каждого из классов.
# Объясните, почему линеаризации данных классов выглядят именно так.


# class Animal:
#     def eat(self):
#         print('Eating')
#
#
# class Horse(Animal):
#     def run(self):
#         print('Running')
#
#
# class Bird:
#     def fly(self):
#         print('Flying')
#
#     def eat(self):
#         print('Bird is eating')
#
#
# class Unicorn(Horse, Bird):
#     pass
#
#
# u = Unicorn()
# u.fly()
# u.eat()
# u.run()
# print(Unicorn.__mro__)
