class Animal:
    def __init__(self, age, is_hungry=True) -> None:
        self.is_hungry = is_hungry
        self.is_hungry = age

    def eat(self):
        self.is_hungry = False


class Mammal(Animal):
    def __init__(self, age, is_hungry=False, has_tail=True) -> None:
        super.__init__(age, is_hungry)
        self.has_tail = has_tail

    def move():
        print("Делает вид что двигается, но на самом деле" +
              " просто передвигает ножками")


class Cat(Mammal):
    def __init__(
            self, name, age, skin_color="black", kind="munchkin",
            is_hungry=True, has_tail=True) -> None:
        super.__init__(age, is_hungry, has_tail)
        self.name = name
        self.skin_color = skin_color
        self.kind = kind

    def say(self) -> None:
        print(f"[{self.name}]: Мяууу... {'Хочу есть.' if self.is_hungry else ''}")


class Dog(Mammal):
    def __init__(
            self, name, age, skin_color="orange", kind="corgi",
            is_hungry=False, has_tail=False) -> None:
        super.__init__(age, is_hungry, has_tail)
        self.name = name
        self.skin_color = skin_color
        self.kind = kind

    def say(self) -> None:
        print(f"[{self.name}]: Гав-гав... {'Хочу есть.' if self.is_hungry else ''}")


class Human(Mammal):
    def __init__(
            self, name, age, kind="european",
            is_hungry=False, has_tail=False) -> None:
        super.__init__(age, is_hungry, has_tail)
        self.name = name
        self.kind = kind

    def work(self) -> None:
        print(f"[{self.name}]: *Делает вид что работает*")


class Student(Human):
    def __init__(
            self, name, dz_done, age=18, kind="european",
            is_hungry=False, has_tail=False) -> None:
        super.__init__(name, age, kind, is_hungry, has_tail)
        self.dz_done = dz_done

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Student):
            return self.dz_done == __o.dz_done
        return NotImplemented

    def __ne__(self, __o: object) -> bool:
        if isinstance(__o, Student):
            return self.dz_done != __o.dz_done
        return NotImplemented

    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Student):
            return self.dz_done < __o.dz_done
        return NotImplemented

    def __le__(self, __o: object) -> bool:
        if isinstance(__o, Student):
            return self.dz_done <= __o.dz_done
        return NotImplemented

    def __gt__(self, __o: object) -> bool:
        if isinstance(__o, Student):
            return self.dz_done > __o.dz_done
        return NotImplemented

    def __ge__(self, __o: object) -> bool:
        if isinstance(__o, Student):
            return self.dz_done >= __o.dz_done
        return NotImplemented
