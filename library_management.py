books = []

    
def add_book():

    add_title = input("Enter the title of the book :")
    add_author = input("Enter the author of the book :")
    for book in books:
        if book["title"].lower() == add_title.lower():
            print("Book already exists.")
            return
    book_added = {
        "title" : add_title,
        "author" : add_author,
        "availability" : True 
    }
    books.append(book_added)
    print("Book added successfully")


def view_books():
    if len(books) == 0:
        print("No books available")
    else:
        for number, book in enumerate(books, start=1):
            print(f"{number}. {book['title']}")
            print(f"Author: {book['author']}")

            if book["availability"]:
                print("Status: Available")
            else:
                print("Status: Borrowed")

            print()   


            

def borrow_book():
    found = False
    ask = input("Enter the title of the book you want to borrow: ")
    for book in books:
        if ask.lower() == book["title"].lower():
            found = True
            if book["availability"]:
                book["availability"] = False
                print("Success")
                print()
                break

            else:
                print("The book is already borrowed")
                break
       
    if not found:
        print("No book found")            






def return_book():
    found = False
    ask = input("Enter the title of the book you want to return: ")
    for book in books:
        if ask.lower() == book["title"].lower():
            found = True
            if not book["availability"]:
                book["availability"] = True
                print("Success")
                print()
                break
            else:
                print("The book is already returned")
                break
    if not found:
        print("No book found") 

def remove_book():
    found = False
    ask = input("Enter the title of the book you want to remove: ")
    for book in books:
        if ask.lower() == book["title"].lower():
            found = True
            books.remove(book)
            print("Book removed successfully")
            print()
            break
        
    if not found:
        print("No book found") 

while True:
    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        remove_book()
    elif choice == "6":
        print("Thank you for using Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
  



