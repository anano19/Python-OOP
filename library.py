class Library:

    def __init__(self, list_of_books):
        self.avaliable_books = list_of_books

    def display_books(self):
        for book in self.avaliable_books:
            print(book)

    def lend_books(self, requested_book):
        if requested_book in self.avaliable_books:
            print("you have now borrowed the book")
            self.avaliable_books.remove(requested_book)
        else:
            print("sorry that book is not available")

    def add_book(self, returned_book):
        self.avaliable_books.append(returned_book)
        print("thanks for returning the book")



class Customer:
    def request_book(self):
        self.book = input("enter a book you want ")
        return self.book

    def return_book(self):
        self.book = input("what book are you returning? ")
        return self.book


library = Library(["book1", "book2", "book3"])
customer = Customer()


while True:
    print("enter 1 to display the books")
    print("enter 2 to request a boook")
    print("enter 3 to return a book")
    print("enter 4 to exit")

    choice = int(input())

    if choice == 1:
        library.display_books()
    elif choice == 2:
        requested_book = customer.request_book()
        library.lend_books(requested_book)
    elif choice == 3:
        return_book = customer.request_book()
        library.add_book(return_book)
    elif choice == 4:
        quit()