class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True
        self.borrowed_by = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by.name}"
        return f"ID: {self.book_id} | {self.title} | {self.author} | {self.genre} | {status}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"ID: {self.member_id} | {self.name}"
