import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author('Terry Pratchett', 78)
author_repository.save(author1)
author2 = Author('J.R.R. Tolkein', 99)
author_repository.save(author2)

author_repository.select_all()

book1 = Book('The colour of magic', author1)
book_repository.save(book1)
book2 = Book('The light fantastic', author1)
book_repository.save(book2)
book3 = Book('The Hobbit', author2)
book_repository.save(book3)

book_repository.select_all()

pdb.set_trace()