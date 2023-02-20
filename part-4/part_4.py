### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def create_new_book():
#     title = input("What is the name of the book you'd like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     year = input("What year was this book published? - ")
#     rating = input("What rating out of 5 would you give this book? - ")
#     pages = input("What is the page count of the book? - ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(create_new_book())


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_new_book():
#     title = str(input("What is the name of the book you'd like to add? - "))
#     author = str(input("Who is the author of the book you would like to add? - "))
#     year = int(input("What year was this book published? - "))
#     rating = float(input("What rating out of 5 would you give this book? - "))
#     pages = int(input("What is the page count of the book? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(create_new_book())



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
def create_new_book():
    try:
        title = str(input("What is the name of the book you'd like to add? - "))
    except:
        title = str(input("I need the name of the book you'd like to add? - "))
    try:
        author = str(input("Who is the author of the book you'd like to add? - "))
    except:
        author = str(input("I need the author of the book you'd like to add? - "))
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("I need the year this was book published? - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = float(input("I need a rating out of 0 - 5 for this book? - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("I need the page count of the book? - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

print(create_new_book())



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
favorite_books = ["The Eye of The World", "The Wise Man's Fear", "Legacies"]

# def main_menu():
#     bookshelf = []
#     try:
#         add_new = bool(input("Would you like to add a new book?"))
#     except:
#         add_new = bool(input("the answer must be 'True' or 'False', Would you like to add a new book?"))
#     see_books = bool(input("Would you like to see what's on our shelf?"))
#     if add_new == True:
#         bookshelf.append(create_new_book())
#     elif see_books == True:
#         print("Books on the bookshelf:")
#         for book in bookshelf:
#             print(book)
#     else:
#         pass



### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
def main_menu():
    bookshelf = []
    
    while True:
        choice = input("Enter 1 to add a new book, 2 to see all books, or 0 to exit: ")
        
        if choice == "1":
            new_book = create_new_book()
            bookshelf.append(new_book)
            print("New book added to the bookshelf.")
        
        elif choice == "2":
            if not bookshelf:
                print("No books on the bookshelf.")
            else:
                print("Books on the bookshelf:")
                for book in bookshelf:
                    print(book)
        
        elif choice == "0":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

main_menu()