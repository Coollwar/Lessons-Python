# print(1 < 2 or 5 < 3 and 2 < 3) # - документация скрывает файлы от выполнения кода
# print(True or False and True)
# print(False and True)
# print(False)

# Работа со строками

# print("Список необходимых продуктов:\n\t"
#       "\t1. Мясо 'Гнусная гусятина'\n\t"
#       "\t2. Голова обезъяны 'Глаза на выкате'\n\t"
#       "\t3. Свинное рыло 'Хряк' ") # перенос строки срабатывает перед последней табуляцией, если их несколько


# products = ["Молоко", "Сыр", "Мясо"]
# print(*products, sep=', ', end='\n')
# print(*products, sep=' + ', end=' = ')
# print("1500")

# sep= - добавляет символ между объектами в строке
# end= - добваляет символ на конец строки

# name = "John"
# age = 46
#         Отладочная печать
# print("Имя: ", name)
# print("Возраст: ", age)
#
# print(f"{name = }")
# print(f"{age = }")

# print(r"\n Управляющая последовательность \Сырые строки")
# print(r"Q:\Media\ДжобЭ\Фото Инст")
# r  в начале строки позволяет выводить в строке элементы кода в первончальном виде

test_string_1 = "Hello, world!"
test_string_2 = "1234567890"

# print(len(test_string_1))
# print(len(test_string_2))
# Метод Len возвращает количество символов в строке

         # Изменение регистра

# print(test_string_1.upper()) - все с заглавной буквы
# print(test_string_1.lower()) - все с маленькой буквы
# print(test_string_1.capitalize()) - строка с заглавной буквы
# print(test_string_1.title()) - каждое слово с заглавной буквы
# print(test_string_1.startswith("Hello")) - дает булевое значение согласно начала строки (True)
# print(test_string_1.endswith("!")) - дает булевое значение согласно концу строки (True)

