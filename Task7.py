# Задача 7: Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x = int(input('Введите число а '))
y = int(input('Введите число b '))
z = int(input('Введите число c '))

a = not (x or y or z)
b = not x and not y and not z

if a == b:
    print('Equal')
else:
    print('Not equal')    