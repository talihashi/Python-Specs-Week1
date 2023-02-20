### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def create_new_book(bookshelf):
    try:
        title = str(input("\nWhat is the name of the book you'd like to add? - "))
    except:
        title = str(input("\nI need the name of the book you'd like to add? - "))
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

    with open(bookshelf, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def get_books(bookshelf):
    print("\nHere are your books:\n")

    with open(bookshelf, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
def get_books_as_list_of_dictionaries(bookshelf):
    books_list = []
    with open(bookshelf, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

def get_book_printed(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")

def get_highest_rated_book(bookshelf):
    list = get_books_as_list_of_dictionaries(bookshelf)
    return max(list, key=lambda x: int(x["rating"]))

def get_lowest_rated_book(bookshelf):
    list = get_books_as_list_of_dictionaries(bookshelf)
    return min(list, key=lambda x: int(x["rating"]))

def main_menu(bookshelf):
    
    while True:
        choice = input("Enter 1 to add a new book, 2 to see all books, 3 to delete all books, 4 to see your highest rated book, 5 to see your lowest rated book, or 0 to exit: ")
        
        if choice == "1":
            create_new_book(bookshelf)
        elif choice == "2":
            get_books(bookshelf)
        elif choice == "3":
            with open(bookshelf, "w") as file:
                pass
        elif choice == "4":
            print("\nHere is your highest rated book...\n")
            get_book_printed(get_highest_rated_book(bookshelf))
        elif choice == "5":
            print("\nHere is your lowest rated book...\n")
            get_book_printed(get_lowest_rated_book(bookshelf))
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu("bookshelf.txt")