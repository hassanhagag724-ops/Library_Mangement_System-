class Catalogue:
    def __init__(self, books=None):
        self.__books = list(books) if books else []

    def add_book(self, book):
        if self.get_book_by_id(book.book_id) is not None:
            return False
        self.__books.append(book)
        return True

    def get_book_by_id(self, book_id):
        for book in self.__books:
            if book.book_id == book_id:
                return book
        return None

    def display_books(self):
        for book in sorted(self.__books, key=lambda item: item.book_id):
            print(book)

    def filter_by_genre(self, genre):
        matches = [book for book in self.__books if book.genre.lower() == genre.lower()]
        for book in sorted(matches, key=lambda item: item.book_id):
            print(book)
        return matches

    def get_all_books(self):
        return list(self.__books)
