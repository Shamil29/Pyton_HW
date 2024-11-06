import math

def square(a):
    return math.ceil(a*a)

side = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(side)}")

