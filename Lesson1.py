

test_string_1 = "Hello, world, Space, Fuck, Duck"
test_string_2 = "1234567890"

# print(test_string_1.find("u"))
# print(test_string_1.rfind("l"))
# print(test_string_1.index("w"))
# print(test_string_1.rindex("w"))
# print(test_string_1.split(", "))
# print(", ".join(["Hello, world"]))

# print(test_string_1.replace()) !!!!!

# print(test_string_1.isdigit())
# print(test_string_2.isdigit())
# print(test_string_1.isalpha())
# print(test_string_2.isalnum())
# print(test_string_1.islower())
# print(test_string_1.isupper())

products = ["Молоко", "Сыр", "Мясо"]
print(*products, sep=', ', end='\n')
print(*products, sep=' + ', end=' = ')
print("1500")
print(" , ".join(products) + " = 1500")
print(test_string_1.replace("world", "Peace"))