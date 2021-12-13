class Item:
    def __init__(self, emoji, name, weight: float) -> None:
        self.emoji = emoji
        self.name = name
        self.weight = weight

    def get_info(self) -> str:
        """Получить информацию о предмете"""
        return "Название: %s\nВес предмета: %0.2f" % (self.name, self.weight)


class Inventory:
    def __init__(self, weight_limit: int) -> None:
        self.storage = []
        self.weight_limit = weight_limit

    def add(self, item: Item) -> bool:
        """Добавить предмет в инвентарь

        Аргументы:
        item -- предмет для добавления
        """
        if item.weight + self.get_weight() > self.weight_limit:
            raise Exception("weight_limit")
        self.storage.append(item)
        return True

    def remove(self, item_pos) -> Item:
        """Удалить предмет из инвентаря

        Аргументы:
        item_pos -- позиция предмета для удаления
        """
        if not(
                type(item_pos) is int) or len(
                self.storage) < item_pos or item_pos < 1:
            raise Exception("invalid_item_pos")
        item = self.storage[item_pos-1]
        del self.storage[item_pos-1]
        return item

    def get_item(self, item_pos) -> str:
        """Получить информацию о предмете по его позиции

        Аргументы:
        item_pos -- позиция предмета для удаления
        """
        if not(
                type(item_pos) is int) or len(
                self.storage) < item_pos or item_pos < 1:
            raise Exception("invalid_item_pos")
        item = self.storage[item_pos-1]
        return "Предмет[%s]:\n%s" % (item.emoji, item.get_info())

    def get_inventory(self) -> str:
        """Получить информацию об инвентаре"""
        return "%r\nВес: (%0.2f/%0.2f)" % (
            [item.emoji for item in self.storage],
            self.get_weight(),
            self.weight_limit)

    def get_weight(self) -> int:
        """Получить вес инвентаря"""
        return sum([item.weight for item in self.storage])
