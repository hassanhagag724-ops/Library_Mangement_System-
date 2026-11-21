class WishlistNode:
    def __init__(self, book):
        self.book = book
        self.prev = None
        self.next = None


class Wishlist:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def add_urgent(self, book):
        node = WishlistNode(book)
        if self.__head is None:
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        self.__size += 1

    def add_normal(self, book):
        node = WishlistNode(book)
        if self.__tail is None:
            self.__head = self.__tail = node
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node
        self.__size += 1

    def remove_book(self, book_id):
        current = self.__head
        while current:
            if current.book.book_id == book_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.__head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.__tail = current.prev
                self.__size -= 1
                return current.book
            current = current.next
        return None

    def display(self):
        if self.__head is None:
            print("Wishlist is empty.")
            return
        current = self.__head
        position = 1
        while current:
            print(f"{position}. {current.book.title} (ID: {current.book.book_id})")
            position += 1
            current = current.next

    def is_empty(self):
        return self.__size == 0
