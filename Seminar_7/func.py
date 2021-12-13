import os
import platform
import numpy
from random import randint


def task_1():
    """Вывести информацию о системе"""
    print("Задание #1")

    print(f"Тип системы: {os.name}")
    print(f"Название системы: {platform.system()} {platform.release()}")
    print(f"Текущий пользователь: {os.getlogin()}")
    print(f"Список файлов и папок:")
    print(*os.listdir(os.getcwd()), sep="\n ")


def task_2():
    """Вывести матрицу рандомных чисел и транспонировать ее"""
    print("Задание #2")
    array = numpy.array([randint(0, 200) for _ in range(9)]).reshape(3, 3)
    print("Сгенерированная матрица:")
    print(array)
    print("Транспонированная матрица:")
    print(array.transpose())
