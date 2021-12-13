#!/usr/bin/env python3
import math
import cmath
x, y = 0, 0


def move(dir, step):
    """Переместить персонажа на n-клеток в m-направлении

    Аргументы:
    dir  -- направление для перемещения
    step -- кол-во клеток для перемещения
    """
    if not step.isdigit():
        return print("Кол-во ходов может быть указано только числом!")

    global x, y
    step = int(step)

    if dir == "влево":
        x -= step
    elif dir == "вправо":
        x += step
    elif dir == "вверх":
        y += step
    elif dir == "вниз":
        y -= step
    else:
        return print("Нельзя ходить в стороны!")


def task_1():
    """Написать скрипт для движения персонажа
    влево, вправо, вверх и вниз по координатам x и y по координатной оси,
    начальная позиция персонажа (0;0)
    """
    print("Задание #1")
    print(f"Позиция персонажа:\t X:{x}\tY:{y}")
    dir = input(
        "Укажите сторону в которую хотите сходить [влево/вправо/вверх/вниз]: ")
    step = input("Укажите кол-во ходов которые вы хотите сделать: ")
    move(dir, step)
    print(f"Позиция персонажа:\t X:{x}\tY:{y}")


def task_2():
    """Написать бесконечный скрипт для движения персонажа
    влево, вправо, вверх и вниз по координатам x и y по координатной оси,
    начальная позиция персонажа (0;0)
    """
    print("Задание #2")
    while True:
        print(f"Позиция персонажа:\t X:{x}\tY:{y}")
        dir = input("Укажите сторону в которую хотите сходить" +
                    "[влево/вправо/вверх/вниз/выйти]: ")
        if dir == "выйти":
            break
        step = input("Укажите кол-во ходов которые вы хотите сделать: ")
        move(dir, step)


def task_3():
    """Написать скрипт решения квадратного уравнения"""
    print("Задание #3")
    print("Формула квадратного уравнения: ax^2+bx+c=0")
    try:
        a = float(input("Укажите a:"))
        b = float(input("Укажите b:"))
        c = float(input("Укажите c:"))
    except:
        print('Неверно указаны параметры уравнения')
        return
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
    elif D == 0:
        x1 = -b/(2*a)
    else:
        return print("Дискриминант этого уравнения меньше 0")

    print("Корни уравнения")
    print("x1\t:{0}\tx2:\t{1}".format(x1, x2 if x2 else ''))


def task_4():
    """Написать скрипт решения квадратного уравнения
    C обработкой отрицательного дискриминанта (с комплексными числами),
    со случаем, если коэффициенты являются комплексными числами.
    """
    print("Задание #4")
    print("Формула квадратного уравнения: ax^2+bx+c=0")
    try:
        a = float(input("Укажите a:"))
        b = float(input("Укажите b:"))
        c = float(input("Укажите c:"))
    except:
        print('Неверно указаны параметры уравнения')
        return
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
    elif D == 0:
        x1 = -b/(2*a)
    else:
        x1 = (-b + cmath.sqrt(D))/(2*a)
        x2 = (-b - cmath.sqrt(D))/(2*a)

    print("Корни уравнения")
    print("x1\t:{0}\tx2:\t{1}".format(x1, x2 if x2 else ''))


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
