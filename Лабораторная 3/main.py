class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Book"
        :param name: название книги
        :param author: автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """
        Свойство, которое не позволяет изменять название книги
        :return: защищённый атрибут
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Свойство, которое не позволяет изменять автора книги
        :return: защищённый атрибут
        """
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс. """
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "PaperBook"
        :param name: название книги, которое наследуется из базового класса
        :param author: автор книги, который наследуется из базового класса
        :param pages: количество страниц
        """
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError("Kоличество страниц должно быть int")
        if pages <= 0:
            raise ValueError("Kоличество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс. """
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе объекта "AudioBook"
        :param name: название книги, которое наследуется из базового класса
        :param author: автор книги, который наследуется из базового класса
        :param duration: продолжительность
        """
        super().__init__(name, author)

        if not isinstance(duration, float):
            raise TypeError("Продолжительность должнa быть float")
        if duration <= 0:
            raise ValueError("Продолжительность должнa быть положительным числом")
        self.duration = duration

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
