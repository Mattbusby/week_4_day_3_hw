from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository
from models.book import Book

library_blueprint = Blueprint("books", __name__)

@library_blueprint. route("/books")
def books():
    books = book_repository.select_all()
    return render_template("index.html", all_books = books)

@library_blueprint.route("/books/new", methods =['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("/new.html", all_authors = authors)


@library_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, author)
    book_repository.save(book)
    return redirect('/books')


