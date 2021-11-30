#!/usr/bin/env python3
from random import randint
from inventory import Inventory, Item

def task_1():
    print("Задание #1")
    length = 10
    print("Создаю массив рандомных чисел, длина массива %d" % length)
    array = [randint(0, 200) for _ in range(length)]
    print("Созданный массив: %s " % array)
    for i in range(length -1):
        for j in range(length - i -1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    print("Отсортированный массив: %s " % array) 

def task_2():
    print("Задание #2")
    colors = {
        "aqua": (0, 255, 255),
        "black": (0, 0, 0),
        "blue": (0, 0, 255,),
        "fuchsia": (255, 0, 255),
        "gray": (128, 128, 128),
        "green": (0, 128, 0),
        "lime": (0, 255, 0),
        "maroon": (128, 0, 0),
        "navy": (0, 0, 128),
        "olive": (128, 128, 0),
        "purple": (128, 0, 128),
        "red": (255, 0, 0),
        "silver": (192, 192, 192),
        "teal": (0, 128, 128),
        "white": (255, 255, 255),
        "yellow": (255, 255, 0)
    }
    while True:
        print("\nВыберите действие:")
        print(" цвета - показать достyпные цветовые коды")
        print(" инфо [код] - покажет информацию о цвете")
        print(" стоп - выйти")
        i = input(": ")
        if i.lower() == "цвета":
            print("Информация о доступных цветовых кодах:")
            print(*colors.keys(), sep="\n")
        elif i.lower().startswith("инфо "):
            code = i.lower().split("инфо ")[1]
            if code not in colors.keys():
                print("[❌] Неизвестный код")
            else:
                color = colors[code]
                print("\n[✔] Информация о цвете:\nКод: %s\nКод в 10-чной системе: %s; \t в 16-чной системе: #%02x%02x%02x\n" % (code, color, *color))
        elif i.lower() == "стоп":
            break
        else:
            print("[❌] Неизвестная команда")

def task_3():
    print("Задание #3")
    array1 = [randint(0, 15) for _ in range(10)]
    array2 = [randint(0, 15) for _ in range(10)]
    print("Созданный массив (1): %s " % array1)
    print("Созданный массив (2): %s " % array2)
    print("Список элементов:")
    print(" Входящих в оба множества: %s " % list(set(array1) & set(array2)))
    print(" Входящих только в первое множество: %s " % list(set(array1) - set(array2)))
    print(" Входящих только во второе множество: %s " % list(set(array2) - set(array1)))
    print(" Входящих в первое или во второе, но не в оба из них одновременно: %s " % list(set(array1) ^ set(array2)))

def task_4():
    print("Задание #4")
    inventory = Inventory(100.0)
    items = [
        Item('💎', "Алмаз", 1.0),
        Item('🍕', "Пицца", 5.0),
        Item('🧦', "Носки", 2.5),
        Item('🧱', "Кирпичи", 102.5)
    ]
    while True:
        print("\nВыберите действие:")
        print(" инвентарь - показать инвентарь")
        print(" предметы - список доступных предметов")
        print(" инфо [номер предмета] - информация о предмете")
        print(" добавить [id предмета] - добавить предмет в инвентарь")
        print(" удалить [номер предмета в инвентаре] - удалить предмет из инветаря")
        print(" стоп - выйти")
        i = input(": ")
        if i.lower() == "инвентарь":
            print("Инвентарь:\n%s" % inventory.get_inventory())

        elif i.lower() == "предметы":
            print("Список предметов:\n\tНазвание\tВес\n%s" % '\n'.join(["%d)%s -\t%s\t\t%0.2f" % (i+1, items[i].emoji, items[i].name, items[i].weight) for i in range(len(items))]))

        elif i.lower().startswith("инфо "):
            item_pos = i.lower().split("инфо ")[1]
            try:
                item_pos = int(item_pos)
                print(inventory.get_item(item_pos))
            except ValueError:
                print("[❌] Неверно указан номер предмета (укажите номер числом)")
            except:
                print("[❌] Неверно указан номер предмета (предмета с таким номером нет)")

        elif i.lower().startswith("добавить "):
            item_id = i.lower().split("добавить ")[1]
            try:
                item_id = int(item_id) -1
                if item_id < 0 or len(items) < item_id: 
                    return print("[❌] Неверно указан номер предмета (предмета с таким номером нет)")

                inventory.add(items[item_id])
                print("[✔] Вы успешно добавили предмет %s" % items[item_id].name)
            except ValueError:
                print("[❌] Неверно указан номер предмета (укажите номер числом)")
            except:
                print("[❌] Невожможно добавить предмет (лимит веса инветаря)")

        elif i.lower().startswith("удалить "):
            item_pos = i.lower().split("удалить ")[1]
            try:
                item_pos = int(item_pos)
                print("[✔] Вы успешно удалили предмет %s" % inventory.remove(item_pos).name)
            except ValueError:
                print("[❌] Неверно указан номер предмета (укажите номер числом)")
            except:
                print("[❌] Неверно указан номер предмета (предмета с таким номером нет)")

        elif i.lower() == "стоп":
            break
        else:
            print("[❌] Неизвестная команда\n")

    pass

if __name__ == "__main__":
    task_number = input("Введите номер задания[1-4]: ")

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
