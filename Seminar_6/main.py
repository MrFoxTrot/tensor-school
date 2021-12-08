#!/usr/bin/env python3
from typing import List
import re
from math import floor
from itertools import cycle


def task_1():
    """
    Написать функцию преобразующую список строк, в список байт кодов. Написать обратную функцию.
    """
    print("Задание #1")

    def encode(input_list: List[str]) -> List[bytearray]:
        return [x.encode("utf-8") for x in input_list]

    def decode(input_list: List[bytearray]) -> List[str]:
        return [x.decode() for x in input_list]

    print("Введите строки для перевода в байт код (напишите 'стоп' для окончания вводе)")
    input_strings = []
    while True:
        string = input(": ")

        if string.lower() == "стоп":
            break

        input_strings.append(string)

    print("Закодированные строки")
    print(*encode(input_strings), sep="\n")
    print("Раскодированные строки")
    print(*decode(encode(input_strings)), sep="\n")


def task_2():
    """
    Формула молекулы спирта - C2H5(OH). Из неё видно, что молекула состоит из двух атомов углерода (С),
    6 атомов водорода (Н) и одного атома кислорода (О). В Input.txt содержится 3 натуральных числа:
    C, H, O – количество атомов углерода, водорода и кислорода соответственно.
    В файл Output.txt вывести максимально возможное число молекул спирта,
    которые могут получиться из атомов, представленных во входных данных.
    """
    print("Задание #2")

    try:
        with open("./input.txt", 'r') as file_input:
            lines = file_input.read().splitlines()
            # Проверка формата строк
            is_format_valid = len(
                list(filter(lambda v: re.match(r'^(C|H|O)=\d+$', v), lines))) > 0
            if len(lines) != 3 or not is_format_valid:
                return print("Невалидный формат файла input.txt")

            c = [x for x in lines if "C" in x]
            h = [x for x in lines if "H" in x]
            o = [x for x in lines if "O" in x]

            if len(c) != 1 or len(h) != 1 or len(o) != 1:
                return print("Невалидный формат файла input.txt")

            c = int(c[0].split("=")[1])
            h = int(h[0].split("=")[1])
            o = int(o[0].split("=")[1])
            res = [floor(c/2), floor(h/6), o]
            res.sort()
            try:
                with open("./output.txt", "w") as file_output:
                    file_output.write(str(res[0]))
            except IOError:
                return print("Не удалось выполнить запись ответа в файл output.txt. Файл не доступен")

            print(
                f"Максимально возможное кол-во молекул спирта из {c=} {h=} {o=} = {res[0]}")

    except IOError:
        return print("Файл input.txt не найден/недоступен")


def task_3():
    """
    XOR шифрование/расшифрование. На входе файл с текстом и ключ шифрования (строка),
    на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле.
    """
    print("Задание #3")

    def xor(text, secret):
        return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(text, cycle(secret)))

    secret = input("Укажите ключ для шифрования: ")
    try:
        with open("./in_cipher.txt", 'r') as file_input:
            text = ''.join(file_input.readlines())
            try:
                with open("./out_cipher.txt", "w") as file_output:
                    file_output.write(xor(text, secret))
                    print("Зашифрованный текст доступен в файле out_cipher.txt")
            except IOError:
                return print("Не удалось выполнить запись ответа в файл out_cipher.txt. Файл не доступен")
    except IOError:
        return print("Файл in_cipher.txt не найден/недоступен")


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
