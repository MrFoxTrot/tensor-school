#!/usr/bin/env python3
from func import task_1, task_2


if __name__ == "__main__":
    task_number = input("Введите номер задания[1-2]: ")

    if task_number == "1":
        task_1()
    elif task_number == "2":
        task_2()
    else:
        print("Неверно выбран номер задания!")
