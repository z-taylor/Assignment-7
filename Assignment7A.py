# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment7A.py

class book():
    def __init__(self, title, author, isBorrowed = False):
        self.title, self.author, self.isBorrowed, self.borrowedBy = title, author, isBorrowed, ""
    def borrow(self, name):
        if not self.isBorrowed:
            self.isBorrowed = True
            self.borrowedBy = name
            return "success"
        else:
            return "fail"
    def returnBook(self, name):
        if self.isBorrowed and name == self.borrowedBy:
            self.isBorrowed = False
            return "success"
        else:
            return "fail"
        
books = [book("Alice In Wonderland", "Lewis Carrol"),
        book("A Wrinkle In Time", "Madeleine L'Engle"),
        book("1984", "George Orwell"),
        book("The Romulan Way", "Diane Duane"),
        book("Harry Potter", "J.K. Rowling"),
        book("To Kill A Mockingbird", "Harper Lee"),
        book("The Catcher In The Rye", "J.D. Salinger"),
        book("Pride And Prejudice", "Jane Austen")
]

print("\nBooks available to borrow from this library: ")
for book_ in books:
    print(f"{book_.title} by {book_.author}")

class member():
    def __init__(self, name):
        self.name, self.borrowList = name, []
    def borrow(self, title, books):
        for book in books:
            title = title.title()
            if book.title == title:
                self.borrowList.append(book)
                if len(self.borrowList) <= 3:
                    attempt = book.borrow(self.name)
                    if attempt == "success":
                        print(f"{book.title} by {book.author} borrowed successfully")
                    else:
                        print("Book is already borrowed.")
                        self.borrowList.remove(book)
                else:
                    print(f"{self.name} has already borrowed 3 books. They must return 1 before borrowing another")
    def return_(self, title, books):
        for book in books:
            title = title.title()
            if book.title == title:
                attempt = book.returnBook(self.name)
                if attempt == "success":
                    print(f"{book.title} by {book.author} borrowed successfully")
                    self.borrowList.remove(book)
                else:
                    print("Book has not been borrowed or is borrowed by another person.")

members = [
    member("John doe"),
    member("Jack Taylor"),
    member("Marcus Sission"),
    member("Stephanie Palmer")
]

print("\nActive members in this library: ")
for member_ in members:
    print(member_.name)

run, action, continue_, memberFound, bookFound = True, "", "", False, False
while run:
    member_ = input("Type the name of the member you want to borrow or return for: ").lower()
    for memberI in members:
        if memberI.name.lower() == member_:
            workingMember = memberI
            print(f"Working with {workingMember.name}")
            memberFound = True
    if not memberFound:
        print("Member not found")
        member_ = ""
        continue
    action = input('Type "borrow" if you want to borrow a book, or "return" if you want to return a book: ').lower()
    if (action != "borrow") and (action != "return"):
        print("Invalid action")
        continue
    title = input(f"Type the name of a book you want to {"borrow" if action=="borrow" else "return"}: ").lower()
    for book_ in books:
        currentBook = book_.title
        currentBook = currentBook.lower()
        if title == currentBook:
            bookFound = True
            if action == "borrow":
                workingMember.borrow(title, books)
            elif action == "return":
                workingMember.return_(title, books)
    if not bookFound:
        print(f"Book {title} not found")
        continue
    continue_ = input("Type Q to quit, M to see the members list again, B to see the books list again, or any other key to continue: ").lower()
    bookFound, memberFound = False, False
    if continue_=="q":
        run = False
        break
    elif continue_=="m":
        for member_ in members:
            print(member_.name)
    elif continue_=="b":
        for book_ in books:
            print(f"{book_.title} by {book_.author}")
    else:
        continue
print("Thank you for visiting our library, please come again soon!")