# Задача 10: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
xa = int(input('Введите координату Xa '))
ya = int(input('Введите координату Ya '))
xb = int(input('Введите координату Xb '))
yb = int(input('Введите координату Yb '))

print(((xb - xa)**2 + (yb - ya)**2)**0.5)


