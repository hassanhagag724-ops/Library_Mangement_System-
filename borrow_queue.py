class BorrowRequest:
    def __init__(self, member, book):
        self.member = member
        self.book = book


class QueueNode:
    def __init__(self, request):
        self.request = request
        self.next = None


class BorrowQueue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__size = 0

    def submit_request(self, member, book):
        node = QueueNode(BorrowRequest(member, book))
        if self.__rear is None:
            self.__front = self.__rear = node
        else:
            self.__rear.next = node
            self.__rear = node
        self.__size += 1

    def process_next(self, book_id=None):
        if self.__front is None:
            return None
        if book_id is None or self.__front.request.book.book_id == book_id:
            node = self.__front
            self.__front = node.next
            if self.__front is None:
                self.__rear = None
            self.__size -= 1
            return node.request
        previous = self.__front
        current = self.__front.next
        while current:
            if current.request.book.book_id == book_id:
                previous.next = current.next
                if current is self.__rear:
                    self.__rear = previous
                self.__size -= 1
                return current.request
            previous = current
            current = current.next
        return None

    def has_requests_for(self, book_id):
        current = self.__front
        while current:
            if current.request.book.book_id == book_id:
                return True
            current = current.next
        return False

    def display_pending(self):
        if self.__front is None:
            print("No pending borrowing requests.")
            return
        current = self.__front
        position = 1
        while current:
            request = current.request
            print(f"{position}. {request.member.name} -> {request.book.title} (ID: {request.book.book_id})")
            position += 1
            current = current.next

    def is_empty(self):
        return self.__size == 0
