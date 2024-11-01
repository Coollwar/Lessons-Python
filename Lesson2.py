# Программа, которая проверяет и выводит значение переменной word палиндром или нет

# word = input("Введите слово для проверки: ")
#
# word = word.lower()
#
# if word == word[::-1]:
#     print("Это слово Палиндром")
# else:
#     print("Это слово Не Палиндром")

# Запрос ввода для первого и второго числа
# number_1 = input("Введите первое число: ")
# number_2 = input("Введите второе число: ")
#
# # Проверка, содержат ли строки только цифры
# if not number_1.isdigit() or not number_2.isdigit():
#     print("Некорректные данные")
# else:
#     # Преобразование строк в целые числа
#     number_1 = int(number_1)
#     number_2 = int(number_2)
#
#     # Проверка на кратность
#     if number_1 % number_2 == 0:
#         print("Кратно")
#     else:
#         print("Не кратно")

# user_value = input("Введите любое значение: ")
#
# if user_value.isdigit():
#     print("Это цифровое значение")
# elif user_value.isalpha():
#     print("Это текстовое значение")
# elif user_value.isalnum():
#     print("Это цифарки с буковками")
# else:
#     print("Это какая-то херь")

score = int(input("Введите ваш балл по экзамену (от 0 до 100): "))

# Проверяем диапазон балла и выводим соответствующую оценку
if 90 <= score <= 100:
    print("Ваша оценка: A")
elif 80 <= score <= 89:
    print("Ваша оценка: B")
elif 70 <= score <= 79:
    print("Ваша оценка: C")
elif 60 <= score <= 69:
    print("Ваша оценка: D")
elif 0 <= score < 60:
    print("Ваша оценка: F")
else:
    print("Некорректное значение")