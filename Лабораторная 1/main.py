import doctest


class Wardrobe:
    def __init__(self, shelves_count: int, drawers_count: int):
        """
        Создание и подготовка к работе объекта "Шкаф"
        :param shelves_count: Число полок
        :param drawers_count: Число ящиков

        Примеры:
        >>> wardrobe = Wardrobe(4, 3)
        """
        if not isinstance(shelves_count, int):
            raise TypeError("Число полок должно быть типа int")
        if shelves_count <= 0:
            raise ValueError("Число полок должно быть положительным числом")
        self.shelves_count = shelves_count

        if not isinstance(drawers_count, int):
            raise TypeError("Число ящиков должно быть int")
        if drawers_count <= 0:
            raise ValueError("Число ящиков должно быть положительным числом")
        self.drawers_count = drawers_count

    def is_empty_wardrobe(self) -> bool:
        """
        Функция проверяет является ли шкаф пустым
        :return: Является ли шкаф пустым

        Примеры:
        >>> wardrobe = Wardrobe(5, 2)
        >>> wardrobe.is_empty_wardrobe()
        """

    def open_wardrobe(self) -> None:
        """
        Функция окрывает шкаф

        Примеры:
        >>> wardrobe = Wardrobe(7, 1)
        >>> wardrobe.open_wardrobe()
        """


class Car:
    def __init__(self, color: str, power: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param color: Цвет автомобиля
        :param power: Мощность в лошадиных силах

        Примеры:
        >>> car = Car('white', 210)
        """
        self.color = color
        self.power = power

    def change_color_car(self, new_color: str) -> str:
        """
        Функция позволяет перекрасить автомобиль
        :param new_color: Новый цвет для покраски
        :return: Новый цвет автомобиля

        Примеры:
        >>> car = Car('white', 210)
        >>> car.change_color_car('red')
        'red'
        """
        self.color = new_color
        return self.color

    def tax_calculation_car(self) -> float:
        """
        Функция рассчитывает налогову ставку
        :return: Налоговую ставку для автомобиля

        Примеры:
        >>> car = Car('white', 210)
        >>> car.tax_calculation_car()
        7.5
        """
        if self.power <= 100:
            return 2.5
        elif self.power <= 150:
            return 3.5
        elif self.power <= 200:
            return 5
        elif self.power <= 250:
            return 7.5
        else:
            return 15


class Region:
    def __init__(self, name: str, population: int):
        """
        Создание и подготовка к работе объекта "Города РФ"
        :param name: Наименование города
        :param population: Численность жителей

        Примеры:
        >>> region = Region('Spb', 4991000)
        """
        self.name = name
        self.population = population

    def capital_region(self) -> bool:
        """
        Функция проверяет является ли введенный город столицей
        :return: Является ли этот город столицей

        Примеры:
        >>> region = Region('Spb', 4991000)
        >>> region.capital_region()
        False
        """
        if self.name == 'Moscow':
            return True
        else:
            return False

    def size_region(self) -> str:
        """
        Функция проверяет является ли введенный регион городом
        :return: Является городом или поселком

        Примеры:
        >>> region = Region('Spb', 4991000)
        >>> region.size_region()
        'city'
        """
        if self.population <= 50000:
            return 'village'
        else:
            return 'city'


if __name__ == "__main__":
    wardrobe = Wardrobe(5, 3)
    car = Car('white', 210)
    car.change_color_car('red')
    region = Region('Spb', 4991000)
    doctest.testmod()
    pass
