# Task 1
yourName = input('Enter your name: ')
print('Your name is', yourName)

number = 20
myText = "Hi! It's my first Python program!"
flNumber = 2.8
description = '''PyCharm
is a multifunctional IDE
for coding on Python'''
print(type(myText), type(flNumber))
print(len(description))
print(myText.upper())
print(myText[9:32])

# Task 2, a)
txt = "More results from text..." # Переменной txt присваиваем значение в виде строки
substr = txt[4:12] # Обрезаем кусок текста из строки. На экран выведутся символы с 4 по 11 индекс,
# не включая символ из 12 индекса.
print(substr) # Выводим уже обрезанную часть строки на экран.
print(substr.strip()) # С помощью метода strip() на экран выводится текст без каких-либо
# пробелов в начале либо конце строки, в зависимости, где имеется пробел.

# b)
txt = "More results from text..." # Переменной txt присваиваем значение в виде строки
print(txt.split())  # С помощью метода split() наша строка разделяется на подстроки, если находит
# экземпляры разделителя в строке. В данном случае, экземпляром разделителя является пробел.
# После чего все это в готовом варианте выводится на экран.

# c)
age = 36 # Переменной age задается значение в виде целого числа
txt = "My name is Mary, and I am {}" # Переменной txt присваивается значение в виде строки, вместе
# с заполнителем в конце.
print(txt.format(age)) # С помощью метода format() содержимое из переменной age помещается в
# заполнитель {}, который находится в переменной txt. После чего на экран выводится результат.



