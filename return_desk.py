class ReturnRecord:
    def __init__(self, book, previous_member, assigned_member=None):
        self.book = book
        self.previous_member = previous_member
        self.assigned_member = assigned_member


class ReturnNode:
    def __init__(self, record):
        self.record = record
        self.next = None


class ReturnDesk:
    def __init__(self):
        self.__top = None
        self.__count = 0

    def log_return(self, book, previous_member, assigned_member=None):
        node = ReturnNode(ReturnRecord(book, previous_member, assigned_member))
        node.next = self.__top
        self.__top = node
        self.__count += 1

    def undo_last_return(self):
        if self.__top is None:
            return None
        record = self.__top.record
        self.__top = self.__top.next
        self.__count -= 1
        return record

    def return_count(self):
        return self.__count

    def is_empty(self):
        return self.__top is None
