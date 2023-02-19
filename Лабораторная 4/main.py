from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, number: int):
        """
        Создание и подготовка к работе объекта "Transport"
        :param number: номер маршрута
        """
        if not isinstance(number, int):
            raise TypeError("Номер транспорта должен быть целым числом")
        if number <= 0:
            raise ValueError("Номер транспорта должен быть положительным числом")
        self.number = number

    def __str__(self) -> str:
        """
        Метод возвращает строку с номером транспорта
        :return: Номер транспорта: №...
        """
        return f'Номер транспорта: №"{self.number}"'

    def __repr__(self) -> str:
        """
        Метод возвращает валидную python строку,
        :return: Transport(number=...)
        """
        return f'Transport(number={self.number})'

    @staticmethod
    def payment() -> str:
        """
        Метод возвращает стоимость проезда
        :return: Проезд стоит 65 рублей.
        """
        return f'Проезд стоит 65 рублей.'

    @abstractmethod
    def road_repair(self):
        ...


class Bus(Transport):
    def __str__(self) -> str:
        """
        Метод возвращает строку с номером автобуса
        :return: Номер автобуса: №...
        """
        return f'Номер автобуса: №"{self.number}"'

    def __repr__(self) -> str:
        """
        Метод возвращает валидную python строку,
        :return: Bus(number=...)
        """
        return f'{self.__class__.__name__}(number={self.number})'

    def road_repair(self) -> str:
        """
        Метод возвращает изменения маршрута следования автобуса при ремонте дороги
        :return: Автобус №... едет по новому маршруту, объезжая ремонт дороги.
        """
        return f'Автобус №"{self.number}" едет по новому маршруту, объезжая ремонт дороги.'


class Tram(Transport):
    def __str__(self) -> str:
        """
        Метод возвращает строку с номером трамвая
        :return: Номер трамвая: №...
        """
        return f'Номер трамвая: №"{self.number}"'

    def __repr__(self) -> str:
        """
        Метод возвращает валидную python строку,
        :return: Tram(number=...)
        """
        return f'{self.__class__.__name__}(number={self.number})'

    def road_repair(self) -> str:
        """
        Метод возвращает изменения маршрута следования трамвая при ремонте дороги
        :return: Трамай № отменен из-за ремонта дороги.
        """
        return f'Трамай №"{self.number}" отменен из-за ремонта дороги.'


if __name__ == "__main__":
    bus = Bus(275)
    tram = Tram(61)
    print(bus)
    print(tram)
    print(repr(bus))
    print(repr(tram))
    print(bus.payment())
    print(tram.payment())
    print(bus.road_repair())
    print(tram.road_repair())
    pass
