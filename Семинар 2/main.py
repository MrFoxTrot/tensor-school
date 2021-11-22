#!/usr/bin/env python3
import math

def task_1():
    print("Задание #1")
    a = float(input("Укажите первое число: "))
    b = float(input("Укажите второе число: "))
    print("\nРезультаты операции над числами")
    print("Сложение:\t\t\t{0}\t\tУмножение:\t\t{1}".format(a + b, a * b))
    print("Вычитание(a-b):\t\t\t{0}\t\tДеление(a/b):\t\t{1}".format(a - b, a / b if b != 0 else "Невозможно (деление на 0)" ))
    print("Вычитание(b-a):\t\t\t{0}\t\tДеление(b/a):\t\t{1}".format(b - a, b / a if a != 0 else "Невозможно (деление на 0)" ))
    print("Возведение в степень (a^b):\t{0}".format(a**b))
    print("Возведение в степень (b^a):\t{0}".format(b**a))
    print("Деление по модулю (a%b):\t{0}".format(a%b))
    print("Деление по модулю (b%a):\t{0}".format(b%a))
    print("Целочисленного деление (a//b):\t{0}".format(a%b))
    print("Целочисленного деление (b//a):\t{0}".format(a%b))
    
def task_2():
    print("Задание #2")
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}, как дела?")

def task_3():
    print("Задание #3")
    string = input("Введите текст: ")
    print(string[-1:-3:-1])

def task_4():
    print("Задание #4")
    r = int(input("Введите радиус: "))
    print("Площадь окружности %f " % (math.pi * r**2))

    


if __name__ == "__main__":
    task_number = input("Введите номер задания[1-4]:")

    if task_number == "1":
        task_1()
    elif task_number == "2":
        task_2()
    elif task_number == "3":
        task_3()
    elif task_number == "4":
        task_4()
    else:
        print("Неверно выбран номер задания!")
