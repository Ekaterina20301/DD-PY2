BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Book"
        :param id_: идентификатор книги
        :param name: название книги
        :param pages:  количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
         Метод возвращает строку с названием книги
        :return: Книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
         Метод возвращает валидную python строку,
         по которой можно инициализировать точно такой же экземпляр
        :return: Book(id_=..., name='...', pages=...)
        """
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, books: list = []):
        """
        Создание и подготовка к работе объекта "Library"
        :param books: cписок книг
        """
        if books is not None:
            self.books = books
        else:
            self.books = []

    def get_next_book_id(self) -> int:
        """
         Метод возвращает идентификатор для добавления новой книги в библиотеку
        :return:  идентификатор для новой книги
        """
        if len(self.books) == 0:
            next_book_id = 1
        else:
            next_book_id = len(self.books)+1
        return next_book_id

    def get_index_by_book_id(self, id_: int) -> int:
        """
        Метод возвращает индекс книги в списке,
        который хранится в атрибуте экземпляра класса
        :param id_: идентификатор книги
        :return: индекс книги
        """
        if id_ <= len(self.books):
            for index_book, book in enumerate(self.books):
                if book.id_ == id_:
                    return index_book
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
