from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title":"Title one", "author":"Author one", "category":"science"},
    {"title":"Title two", "author":"Author two", "category":"history"},
    {"title":"Title three", "author":"Author three", "category":"math"},
    {"title":"Title four", "author":"Author four", "category":"science"},
    {"title":"Title five", "author":"Author five", "category":"history"},
    {"title":"Title six", "author":"Author two", "category":"math"},
]
@app.get('/books')
async def read_all_books():
    return BOOKS

@app.get('/books/{book_title}')
async def get_book(book_title:str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
        
@app.get('/books/')
async def read_book_by_query(category:str):
    books_to_retun = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_retun.append(book)
    return books_to_retun

@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put('/books/updated_book')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break