# Задача 1 
a = int(input("Введите первое число: ")) 
b = int(input("Введите второе число: ")) 
if a > b: 
    maximus = a 
    minimus = b 
else: 
    maximus = b 
    minimus = a 
 
print("Ответ:") 
print("Максимальное число:", maximus) 
print("Минимальное число:", minimus)
#Задача 2
import math
side = float(input("Введите сторону квадрата: "))
radius = float(input("Введите радиус круга: "))
diagonal = math.sqrt(2) * side
if diagonal >= 2 * radius:
    print("Круг впишется в квадрат")
else:
    print("Круг не впишется в квадрат")
x=int(input("Введите первое число: "))
if x<=0:
    y=x**x
else:
    y=1/x*x
    print("Ответ", y)
#Задача 4
import math
side = float(input("Введите сторону квадрата: "))
radius = float(input("Введите радиус круга: "))
diagonal = math.sqrt(2) * side
if diagonal <= 2 * radius:
    print("Квадрат впишется в круг")
else:
    print("Квадрат не впишется в круг")
#Задача 5 
num1 = float(input("Введите первое вещественное число: "))
num2 = float(input("Введите второе вещественное число: "))
if num1 > num2:
    print(f"Большее число: {num1}")
elif num2 > num1:
    print(f"Большее число: {num2}")
else:
    print("Числа равны")