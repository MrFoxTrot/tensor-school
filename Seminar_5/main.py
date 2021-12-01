#!/usr/bin/env python3
import re


def task_1():
    print("Задание #1")
    settings = {
        "more_than_6": True,
        "one_digit": True,
        "no_digits": True,
        "no_common_word": True,
    }
    while True:
        print("\nВыберите действие:")
        print(" настройка - текущие настройки")
        print(" настройка [номер параметра] - изменить параметр настроек")
        print(" проверка - проверить пароль")
        print(" стоп - выйти")

        i = input(": ")
        if i.lower().startswith("настройка"):
            def params_mapper(param):
                return '✔' if settings[param] else '❌'

            if i.lower().startswith("настройка "):
                param_number = i.lower().split("настройка ")[1]
                try:
                    param_number = int(param_number)
                except ValueError:
                    return print("[❌] Неверно указан номер парметра (не цифра)")

                if len(settings) < param_number:
                    return print("[❌] Данный параметр не найден")

                param = list(settings.keys())[param_number-1]
                settings[param] = not settings[param]
                print("[✔] Вы успешно обновили параметр")

            print("Текущие настройки:")
            print("1) Не менее 6 символов: %s\t\t2) Минимум 1 цифра: %s" % (
                params_mapper("more_than_6"), params_mapper("one_digit")))
            print("3) Отсутсвие цифр: %s\t\t4) Без слово 'password': %s" % (
                params_mapper("no_digits"), params_mapper("no_common_word")))

        elif i.lower() == "проверка":
            passwd = input("Введите пароль: ")
            if settings["more_than_6"] and len(passwd) < 6:
                print("[❌] Слишком малое кол-во символов, минимум 6!")
            elif settings["one_digit"] and re.search(r"\d+", passwd) is None:
                print("[❌] В пароле должно быть минимум 1 цифра!")
            elif settings["no_digits"] and re.search(r"\d+", passwd) is not None:
                print("[❌] В пароле не должно быть цифр!")
            elif settings["no_common_word"] and "password" in passwd:
                print("[❌] В пароле не должно быть слова пароль!")
            else:
                print("[✔] Проверка успешно пройдена!")

        elif i.lower() == "стоп":
            break
        else:
            print("[❌] Неизвестная команда\n")


def task_2():
    print("Задание #2")

    def _sum(*args):
        return sum(args)

    number = input("Укажите ряд чисел для сложения (через пробел): ")
    try:
        if number == "":
            numbers = []
        else:
            numbers = [int(num) for num in number.split(" ")]
    except ValueError:
        return print("[❌] неверно указано целое число!")

    print("[✔] Сумма чисел: %d" % _sum(*numbers))


def task_3():
    print("Задание #3")

    def fib(num):
        if num in [1, 2]:
            return 1
        return fib(num - 1) + fib(num - 2)

    number = input("Укажите номер элемента ряда Фибоначи: ")
    try:
        number = int(number)
    except ValueError:
        return print("[❌] Укажите номер целым числом!")

    print("[✔] Значение этого элемента: %d" % fib(number))


if __name__ == "__main__":
    task_number = input("Введите номер задания[1-3]: ")

    if task_number == "1":
        task_1()
    elif task_number == "2":
        task_2()
    elif task_number == "3":
        task_3()
    else:
        print("Неверно выбран номер задания!")
