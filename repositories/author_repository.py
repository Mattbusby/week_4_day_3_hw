from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def save(author):
    sql = "INSERT INTO authors (full_name, age) VALUES (%s, %s) RETURNING *"
    values = [author.full_name, author.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['full_name'], row['age'], row['id'] )
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['full_name'], result['age'], result['id'] )
    return author

def books(author):
    books = []

    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    results = run_sql(sql, values)

    for row in results:
        book = Book(row['title'], row['author_id'], row['id'] )
        books.append(book)
    return books

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)