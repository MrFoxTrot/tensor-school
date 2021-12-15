#!/usr/bin/env python3
import time
from datetime import datetime
import math
import cmath


def global_log(log):
    print(log)
    with open("./log.txt", "a") as f:
        f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+": "+log+"\n")


def wrapper_logger(func):
    def wrapper(*args, **kwargs):
        global_log(f"Функция {func.__name__}")
        func(*args, **kwargs)
    return wrapper


def wrapper_time(func):
    def wrapper(*args, **kwargs):
        global_log(f"Запущен таймер")
        start = time.perf_counter()
        response = func(*args, **kwargs)
        global_log(f"Время выполнения: {time.perf_counter() - start} секунд.")
        return response
    return wrapper


def slow_down(func):
    def wrapper_slow_down(*args, **kwargs):
        global_log(f"Заморозка функции")
        time.sleep(10)
        global_log(f"Разморозка функции")
        func(*args, **kwargs)
    return wrapper_slow_down


@wrapper_logger
@slow_down
@wrapper_time
def task():
    print("Формула квадратного уравнения: ax^2+bx+c=0")

    try:
        a = float(input("Укажите a:"))
        b = float(input("Укажите b:"))
        c = float(input("Укажите c:"))
    except:
        print('Неверно указаны параметры уравнения')
        return
    x1, x2 = math_quadratic_equation(a, b, c)
    print("Корни уравнения")
    print("x1\t:{0}\tx2:\t{1}".format(x1, x2 if x2 else ''))


def math_quadratic_equation(a, b, c):
    x1, x2 = None, None
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
    elif D == 0:
        x1 = -b/(2*a)
    else:
        x1 = (-b + cmath.sqrt(D))/(2*a)
        x2 = (-b - cmath.sqrt(D))/(2*a)
    return x1, x2


if __name__ == "__main__":
    math_quadratic_equation()
