# Задача 2: Найти максимальное из пяти чисел

a = int(input('Введите число а '))
b = int(input('Введите число b '))
c = int(input('Введите число c '))
d = int(input('Введите число d '))
e = int(input('Введите число e '))

list = [a,b,c,d,e]
max_number = max(list)
print(f'Максимальное число {max_number}')  