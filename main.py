from library import Library
from data import BOOKS, MEMBERS


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None


def show_members(library):
    for member in library.members:
        print(member)


def main():
    library = Library(BOOKS, MEMBERS)

    while True:
        print("\n========== InstantLib ==========")
        print("1. Display Catalogue")
        print("2. Filter Books by Genre")
        print("3. Search Book by ID")
        print("4. Add Book to Wishlist")
        print("5. Remove Book from Wishlist")
        print("6. Display Member Wishlist")
        print("7. Borrow Book")
        print("8. Display Borrowing Queue")
        print("9. Return Book")
        print("10. Undo Last Return")
        print("11. Display Members")
        print("12. Return Count")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            library.catalogue.display_books()
        elif choice == "2":
            genre = input("Enter genre: ").strip()
            results = library.catalogue.filter_by_genre(genre)
            if not results:
                print("No books found for this genre.")
        elif choice == "3":
            book_id = read_int("Enter book ID: ")
            if book_id is not None:
                book = library.catalogue.get_book_by_id(book_id)
                print(book if book else "Book not found.")
        elif choice == "4":
            member_id = read_int("Enter member ID: ")
            book_id = read_int("Enter book ID: ")
            if member_id is not None and book_id is not None:
                member = library.get_member_by_id(member_id)
                book = library.catalogue.get_book_by_id(book_id)
                wishlist = library.get_wishlist(member_id)
                if member is None or book is None or wishlist is None:
                    print("Member or book not found.")
                else:
                    urgent = input("Add as urgent? (y/n): ").strip().lower()
                    if urgent == "y":
                        wishlist.add_urgent(book)
                    else:
                        wishlist.add_normal(book)
                    print("Book added to wishlist.")
        elif choice == "5":
            member_id = read_int("Enter member ID: ")
            book_id = read_int("Enter book ID to remove: ")
            if member_id is not None and book_id is not None:
                wishlist = library.get_wishlist(member_id)
                if wishlist is None:
                    print("Member not found.")
                else:
                    removed = wishlist.remove_book(book_id)
                    print("Book removed." if removed else "Book was not found in this wishlist.")
        elif choice == "6":
            member_id = read_int("Enter member ID: ")
            if member_id is not None:
                wishlist = library.get_wishlist(member_id)
                if wishlist is None:
                    print("Member not found.")
                else:
                    wishlist.display()
        elif choice == "7":
            member_id = read_int("Enter member ID: ")
            book_id = read_int("Enter book ID: ")
            if member_id is not None and book_id is not None:
                library.borrow_book(member_id, book_id)
        elif choice == "8":
            library.borrow_queue.display_pending()
        elif choice == "9":
            member_id = read_int("Enter member ID: ")
            book_id = read_int("Enter book ID: ")
            if member_id is not None and book_id is not None:
                library.return_book(member_id, book_id)
        elif choice == "10":
            library.undo_last_return()
        elif choice == "11":
            show_members(library)
        elif choice == "12":
            print(f"Total logged returns: {library.return_desk.return_count()}")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
