from catalogue import Catalogue
from wishlist import Wishlist
from borrow_queue import BorrowQueue
from return_desk import ReturnDesk


class Library:
    def __init__(self, books, members):
        self.catalogue = Catalogue(books)
        self.members = list(members)
        self.borrow_queue = BorrowQueue()
        self.return_desk = ReturnDesk()
        self.__wishlists = {member.member_id: Wishlist() for member in self.members}

    def get_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.get_member_by_id(member_id)
        book = self.catalogue.get_book_by_id(book_id)
        if member is None or book is None:
            print("Member or book not found.")
            return False
        if book.is_available:
            book.is_available = False
            book.borrowed_by = member
            member.borrowed_books.append(book)
            print(f"{member.name} borrowed '{book.title}'.")
            return True
        self.borrow_queue.submit_request(member, book)
        print(f"'{book.title}' is unavailable. {member.name} has been added to the request queue.")
        return False

    def return_book(self, member_id, book_id):
        member = self.get_member_by_id(member_id)
        book = self.catalogue.get_book_by_id(book_id)
        if member is None or book is None:
            print("Member or book not found.")
            return False
        if book.borrowed_by is not member:
            print("This member is not currently borrowing this book.")
            return False
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
        book.borrowed_by = None
        book.is_available = True
        next_request = self.borrow_queue.process_next(book_id)
        assigned_member = None
        if next_request is not None:
            assigned_member = next_request.member
            book.is_available = False
            book.borrowed_by = assigned_member
            assigned_member.borrowed_books.append(book)
            print(f"Queue processed: {assigned_member.name} borrowed '{book.title}'.")
        self.return_desk.log_return(book, member, assigned_member)
        print(f"{member.name} returned '{book.title}'.")
        return True

    def undo_last_return(self):
        record = self.return_desk.undo_last_return()
        if record is None:
            print("There are no returns to undo.")
            return False
        book = record.book
        if record.assigned_member is not None:
            assigned = record.assigned_member
            if book in assigned.borrowed_books:
                assigned.borrowed_books.remove(book)
        previous = record.previous_member
        if book not in previous.borrowed_books:
            previous.borrowed_books.append(book)
        book.is_available = False
        book.borrowed_by = previous
        print(f"Last return of '{book.title}' was undone. It is now borrowed by {previous.name} again.")
        return True

    def get_wishlist(self, member_id):
        return self.__wishlists.get(member_id)


