my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def get_book_info(book):
    book_string = f"{book.get('title')} was written by {book.get('author')} in the year {book.get('year')}. It's got a rating of {book.get('rating')} and is {book.get('pages')} pages long."
    return book_string

get_book_info(my_book)
print(get_book_info(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def get_title(book):
    book_title = book.get('title')
    return book_title

def get_author(book):
    book_author = book.get('author')
    return book_author

def get_year(book):
    book_year = book.get('year')
    return book_year

def get_rating(book):
    book_rating = book.get('rating')
    return book_rating
    
def get_pages(book):
    book_pages = book.get('pages')
    return book_pages

print(get_title(my_book))
print(get_author(my_book))
print(get_year(my_book))
print(get_rating(my_book))
print(get_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
def change_rating(book, amount):
    book['rating'] += amount
    return f"New rating: {book['rating']}"

def update_name(book, new_name):
    book['author'] = new_name
    return f"The authors name has been changed to {book['author']}"

def get_summary(book):
    print(f"{book['title']} by {book['author']}, {book['pages']} pages")

print(change_rating(my_book, .3))
print(update_name(my_book, 'Silvia Stealthless'))
print(get_summary(my_book))